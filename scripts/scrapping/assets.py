import json

import httpx
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
    get_sessions_movies,
    get_sessions_theaters,
)
from .mappings import MAP_THEATER, remap_keys, MAP_MOVIE, MAP_SESSION
import httpx
import datetime
import concurrent.futures

from .mappings import MAP_MOVIE, MAP_SESSION, MAP_THEATER, remap_keys
from .modules import call_website, find_data_key, get_movies_session, list_all_movies

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
    scrapeMK2Theaters.rename(columns=MAP_THEATER, inplace=True)
    df = scrapeMK2Theaters[MAP_THEATER.values()]  # To keep only renamed columns
    with open("data.json", "w") as json_file:
        json_file.write(df.to_json(orient = 'records')) 
    return df.to_json(orient = 'records')


@asset(group_name="theaters", description="Upload Theaters with the API")
def uploadMK2Theaters(scrapeMK2Theaters):
    for i in range(len(scrapeMK2Theaters)):
        theater_post = remap_keys(scrapeMK2Theaters[i], MAP_THEATER, discard=True)
        theater_post["company_name"] = "MK2"
        r = httpx.post(f"{api_url}/theater/", data=theater_post)
        logger.info(r.text)


@asset(group_name="movies", description="Get sessions from theaters")
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

    return Output(
        value=all_movies_sessions,
        metadata={
            "num_rows": len(df),
            "preview": MetadataValue.md(df.head().to_markdown()),
        },
    )


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
        value=allMovies,
        metadata={
            "num_rows": len(df),
            "preview": MetadataValue.md(df.head().to_markdown()),
        },
    )



@asset(group_name="movies", description="Upload Movies with the API")
def uploadMK2Movies(scrapeMK2Movies):
    for i in range(len(scrapeMK2Movies)):
        movie_post = remap_keys(scrapeMK2Movies[i], MAP_MOVIE, discard=True)
        movie_post["company_name"] = "MK2"
        r = httpx.post(f"{api_url}/movie/", data=movie_post)
        logger.info(r.text)


@asset(group_name="movies", description="Get mk2 movies sessions")
def getMK2Sessions(scrapeMK2Movies):
    """
    Peut être qu'on devrait ajouter la possibilité de filtrer sur les films "updated" cette semaine courrante, pour ne pas chercher sur mk2 tous les films mais uniquement ceux qui sont actuellement sur le site de mk2
    Pour l'instant je me base sur le retour de scrapeMK2Movies mais on ajoutera ici un appel à l'API ou un asset à part suivant le fonctionnement, besoin d'avoir l'id du film retourné par l'API pour pouvoir renvoyer l'info à o'API
    Tester: https://prod-paris.api.mk2.com/films/les-algues-vertes?cinema-group=ile-de-france&show-time_gt=2023-07-16
    """
    for i in range(len(scrapeMK2Movies)):
        logger.info(f"----- {scrapeMK2Movies[i]['slug']} -----")
        movie_sessions = json.loads(get_movies_session(movie_url, scrapeMK2Movies[i]["slug"]))
        movie_sessions_cinema = movie_sessions.get("sessionsByCinema")
        for j in range(len(movie_sessions_cinema)):
            #logger.info(movie_sessions_cinema[j])
            df = pd.DataFrame(movie_sessions_cinema[j].get("sessions"))
            # Il y a l'id du cinéma dans le sessions (cinemaId)
            # Il y a plusieurs attributs, regarder le "shortname" de ces attributs qui correspond aux infos comme 2D, VF
            # Showtime est la date de la séance du film en ISO-8601; correspond à l'heure de la séance à UTC, le Z indiquant que c'est UTC
            logger.info(df)