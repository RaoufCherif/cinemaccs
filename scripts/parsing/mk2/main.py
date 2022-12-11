import json
import httpx
from theater_parser import call_website, find_data_key, list_all_movies
from mappings import MAP_THEATER, remap_keys


mk2_home = "https://www.mk2.com"
all_movies = "https://www.mk2.com/films/tous-les-films"

if __name__ == "__main__":

    mk2_home_content = call_website(mk2_home)
    data_key = find_data_key(mk2_home_content)
    theater_json = json.loads(
        call_website(f"{mk2_home}/_next/data/{data_key}/salles.json")
    )
    theaters = theater_json.get("pageProps").get("cinemaGroups")[0].get("cinemas")
    for i in range(len(theaters)):
        theater_post = remap_keys(theaters[i], MAP_THEATER, discard=True)
        theater_post["company_name"] = "MK2"
        r = httpx.post("http://localhost:8000/api/theater/", data=theater_post)
        print(r.text)

    """
    all_movies_content = call_website(all_movies)
    list_of_movies = list_all_movies(all_movies_content)
    for i in range(len(list_of_movies)):
        movie_json = json.loads(
            call_website(
                f"https://www.mk2.com/_next/data/{data_key}/default/film/{list_of_movies[i]}.json"
            )
        )
        movie = movie_json.get("pageProps").get("film")
    """
