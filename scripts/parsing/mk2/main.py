import json
import sys
import datetime
from parser import callWebsite, findDataKey


if __name__ == '__main__':

    # We find all the bags we need to parse, and randomize it to not create any path that will help the website to find us
    mk2_website = callWebsite("https://www.mk2.com/")