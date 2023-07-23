import json
import requests
import pandas as pd
from dagster import (
    DailyPartitionsDefinition,
    Definitions,
    Failure,
    MetadataValue,
    Output,
    SkipReason,
    asset,
    get_dagster_logger,
)
import json
import pandas as pd
from .modules import (
    call_website,
    find_data_key,
    list_all_movies,
    next_dates,
    get_sessions_theaters,
    extract_movie_id,
)
from .mappings import MAP_THEATER, remap_keys, MAP_MOVIE, MAP_SESSION
import datetime
import concurrent.futures


logger = get_dagster_logger()
mk2_home = "https://www.mk2.com"
all_movies = "https://www.mk2.com/films/tous-les-films"
api_url = "http://localhost:8000/api"
movie_url = "https://prod-paris.api.mk2.com/films"
theaters_url = "https://prod-paris.api.mk2.com/cinema-complex"


@asset(group_name="all", description="Get MK2 DataKey")
def getMK2DataKey():
    mk2_home_content = call_website(mk2_home)
    data_key = find_data_key(mk2_home_content)
    return data_key


@asset(group_name="theaters", description="Scrape mk2 theaters")
def scrapeMK2Theaters(getMK2DataKey):
    theater_json = json.loads(
        call_website(f"{mk2_home}/_next/data/{getMK2DataKey}/salles.json")
    )
    theaters = theater_json.get("pageProps").get("cinemaGroups")[0].get("cinemas")
    df = pd.DataFrame(theaters)
    return Output(
        value=df,
        metadata={
            "num_rows": len(df),
            "preview": MetadataValue.md(df.head().to_markdown()),
        },
    )


@asset(group_name="theaters", description="Theaters dataframe to JSON")
def jsonMK2Theaters(scrapeMK2Theaters):
    scrapeMK2Theaters["company_name"] = "MK2"
    scrapeMK2Theaters.rename(columns=MAP_THEATER, inplace=True)
    df = scrapeMK2Theaters[MAP_THEATER.values()]  # To keep only renamed columns
    """
    with open("data.json", "w") as json_file:
        json_file.write(df.to_json(orient = 'records'))  
    """
    return df.to_json(orient="records")


@asset(group_name="theaters", description="Upload Theaters with the API")
def uploadMK2Theaters(jsonMK2Theaters):
    r = requests.request("POST", f"{api_url}/theater/", data=jsonMK2Theaters)
    logger.info(r.text)


@asset(group_name="sessions", description="Get sessions from theaters")
def getMK2TheatersSessions(scrapeMK2Theaters):
    next_session_date = next_dates()
    all_movies_sessions = []

    df = scrapeMK2Theaters["complexSlug"]
    df = df.drop_duplicates()
    theaters_list = df.values.tolist()
    logger.info(theaters_list)

    num_threads = 10

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [
            executor.submit(
                get_sessions_theaters,
                theaters_url,
                theater,
                next_session_date,
            )
            for theater in theaters_list
        ]

        for future in concurrent.futures.as_completed(futures):
            result = json.loads(future.result())
            for sub in result:
                all_movies_sessions.append(sub)

    df = pd.DataFrame(all_movies_sessions)
    df["movieId"] = df["scheduledFilmId"].apply(extract_movie_id)
    df["session_time"] = pd.to_datetime(df["showTime"], unit="ms")
    return Output(
        value=df,
        metadata={
            "num_rows": len(df),
            "preview": MetadataValue.md(df.head().to_markdown()),
        },
    )


@asset(group_name="sessions", description="Post sessions from theaters")
def jsonMK2Sessions(getMK2TheatersSessions):
    logger.info(getMK2TheatersSessions.to_json(orient="records"))
    getMK2TheatersSessions["company_name"] = "MK2"
    getMK2TheatersSessions.rename(columns=MAP_SESSION, inplace=True)
    df = getMK2TheatersSessions[MAP_SESSION.values()]  # To keep only renamed columns
    logger.info(df)
    return df.to_json(orient="records")


@asset(group_name="sessions", description="Upload Sessions with the API")
def uploadMK2Sessions(jsonMK2Sessions):
    r = requests.request("POST", f"{api_url}/sessions/", data=jsonMK2Sessions)
    logger.info(r.text)


@asset(group_name="movies", description="Scrape mk2 movies")
def scrapeMK2Movies(getMK2DataKey):
    """
    1. Récupérer tous les films
    2. Récupérer toutes les séances liées au film, uploader le film dans la base ainsi que ses séances, en liant la séance à l'id d'un cinéma qu'on a récupéré au moment du post ou alors il faudra aussi faire un GET
    """
    all_movies_content = call_website(all_movies)
    list_of_movies = list_all_movies(all_movies_content)
    allMovies = []
    for i in range(len(list_of_movies)):
        movie_json = json.loads(
            call_website(
                f"https://www.mk2.com/_next/data/{getMK2DataKey}/default/film/{list_of_movies[i]}.json"
            )
        )
        allMovies.append(movie_json.get("pageProps").get("film"))
    df = pd.DataFrame(allMovies)
    return Output(
        value=df,
        metadata={
            "num_rows": len(df),
            "preview": MetadataValue.md(df.head().to_markdown()),
        },
    )


@asset(group_name="movies", description="Movie dataframe to JSON")
def jsonMK2Movies(scrapeMK2Movies):
    scrapeMK2Movies["company_name"] = "MK2"
    scrapeMK2Movies.rename(columns=MAP_MOVIE, inplace=True)
    df = scrapeMK2Movies[MAP_MOVIE.values()]  # To keep only renamed columns
    return df.to_json(orient="records")


@asset(group_name="movies", description="Upload Movies with the API")
def uploadMK2Movies(jsonMK2Movies):
    r = requests.request("POST", f"{api_url}/movie/", data=jsonMK2Movies)
    logger.info(r.text)
