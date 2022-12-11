import httpx
import sys
import datetime
import random
from bs4 import BeautifulSoup


def call_website(url):

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