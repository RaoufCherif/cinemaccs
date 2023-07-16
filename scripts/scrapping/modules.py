import httpx
import sys
import datetime
import random
from bs4 import BeautifulSoup


def call_website(url):
    """
    GET data from a website, with multiple headers possible

    input:
        - url: url of the website, starting with http or https

    output:
        - content of the webpage
    """

    headers = [
        {"user-agent": "my-app/0.0.1"},
    ]

    is_finished = False
    i = random.randint(0, len(headers) - 1)
    response = httpx.get(url, headers=headers[i])

    if response.status_code == 200:
        is_finished = True
        return response.text

    if is_finished == False:
        sys.exit(
            f"{datetime.datetime.now()} - ERROR - Cannot access {url} : {response}"
        )


def find_data_key(content):
    """
    Retrieve the data key in the source code of the website

    input:
        - content: source code of the website
    output:
        - data key
    """
    soup = BeautifulSoup(content, features="html.parser")
    detect_data_key_path = [
        "_buildManifest.js",
        "_ssgManifest.js",
        "_middlewareManifest.js",
    ]

    for head in soup.find("head"):
        for dkp in range(len(detect_data_key_path)):
            if detect_data_key_path[dkp] in str(head):
                split_path = str(head).split("/")
                detect_position = [
                    i
                    for i in range(len(split_path))
                    if detect_data_key_path[dkp] in split_path[i]
                ]
                return split_path[detect_position[0] - 1]


def list_all_movies(content):
    """
    Retrieve all the movies in the source code

    input:
        - content: source code of the website
    output:
        - list of movie names
    """
    soup = BeautifulSoup(content, features="html.parser")

    list_movies = []

    for a in soup.find_all("a", href=True):
        if "/film/" in a["href"]:
            movie_name = a["href"].split("/")
            movie_name.reverse()
            list_movies.append(movie_name[0])
    return list_movies

def get_movies_session(url, movie_name):
    """
    GET movie sessions

    input:
        - url: url of the website, starting with http or https
        - movie_name: movie name in lower in the URL

    output:
        - movie data
    """

    headers = [
        {"user-agent": "my-app/0.0.1"},
    ]

    is_finished = False
    i = random.randint(0, len(headers) - 1)
    response = httpx.get(f"{url}/{movie_name}", headers=headers[i])

    if response.status_code == 200:
        is_finished = True
        return response.text

    if is_finished == False:
        sys.exit(
            f"{datetime.datetime.now()} - ERROR - Cannot access {url} : {response}"
        )