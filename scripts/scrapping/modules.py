from dagster import (
    asset,
    get_dagster_logger,
    Definitions,
    DailyPartitionsDefinition,
    Output,
    MetadataValue,
    SkipReason,
    Failure,
)

import requests
import sys
import datetime
import random
import sys
from bs4 import BeautifulSoup
import json
import pandas as pd
import time


logger = get_dagster_logger()


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
    try:
        response = requests.request("GET", url, headers=headers[i])
    except Exception as ex:
        logger.info(f"{ex} - {url}")

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


def get_movies_session(url, movie_name, dateSessions):
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
    complete_url = f"{url}/{movie_name}?show-time_gt={dateSessions}"
    timeout = 0
    time_sleep = 5
    while is_finished == False:
        response = requests.request("GET", complete_url, headers=headers[i])

        if response.status_code == 200:
            is_finished = True
            return response.text
        else:
            logger.info(f"ERROR - Cannot access {complete_url} - Retry in 5 seconds")
            time.sleep(time_sleep)
            timeout += time_sleep
            if timeout == 60:
                sys.exit(
                        f"{datetime.datetime.now()} - ERROR - Cannot access {url} : {response}"
                    )



def next_dates():
    weekday_idx = 2
    now = datetime.datetime.now()
    days_delta = weekday_idx - now.weekday()
    if days_delta <= 0:
        days_delta += 7
    next_tuesday = now + datetime.timedelta(days_delta)
    list_dates = []
    while now != next_tuesday:
        list_dates.append(now.strftime("%Y-%m-%d"))
        now = now + datetime.timedelta(1)
    return list_dates


def get_shortname_if_starts_with_v(row):
    for item in row:
        if item.get("shortName", "").startswith("V"):
            return item.get("shortName")
    return None


def get_sessions_movies(movie_url, movie_slug, next_session_date):
    all_sessions = []
    for h in range(len(next_session_date)):
        movie_sessions = json.loads(
            get_movies_session(movie_url, movie_slug, next_session_date[h])
        )
        movie_sessions_cinema = movie_sessions.get("sessionsByCinema")
        for k in range(len(movie_sessions_cinema)):
            sessions = movie_sessions_cinema[k].get("sessions")
            for l in range(len(sessions)):
                all_sessions.append(sessions[l])
    df = pd.DataFrame(all_sessions)
    if len(df) > 0:
        try:
            df["language"] = df["attributes"].apply(get_shortname_if_starts_with_v)
        except Exception as Ex:
            logger.info(f"ERROR - {movie_slug} - {Ex}")
            logger.info(df)
        df["showTime"] = pd.to_datetime(df["showTime"])
        df.drop_duplicates
        df["slug"] = movie_slug
        # Il y a l'id du cinéma dans le sessions (cinemaId)
        logger.info(f"INFO - {movie_slug} - {len(df)} sessions")
        return df.values.tolist()

def get_sessions_theaters(theaters_url, theater_slug, next_session_date):
    all_sessions = []
    for h in range(len(next_session_date)):
        movie_sessions = json.loads(
            get_movies_session(theaters_url, theater_slug, next_session_date[h])
        )
        movie_sessions_cinema = movie_sessions.get("sessionsByType")[0].get("sessionsByFilmAndCinema")
        for j in range(len(movie_sessions_cinema)):
            sessions = movie_sessions_cinema[j].get("sessions")
            for l in range(len(sessions)):
                all_sessions.append(sessions[l])
    df = pd.DataFrame(all_sessions)
    if len(df) > 0:
        try:
            df["language"] = df["attributes"].apply(get_shortname_if_starts_with_v)
        except Exception as Ex:
            logger.info(f"ERROR - {theater_slug} - {Ex}")
            logger.info(df)
        df["showTime"] = pd.to_datetime(df["showTime"])
        df.drop_duplicates
        df["slug"] = theater_slug
        # Il y a l'id du cinéma dans le sessions (cinemaId)
        logger.info(f"INFO - {theater_slug} - {len(df)} sessions")
        return df.to_json(orient = 'records')