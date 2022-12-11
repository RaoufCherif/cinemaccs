import json
from theater_parser import call_website, find_data_key

website = "https://www.mk2.com/"

if __name__ == '__main__':

    # We find all the bags we need to parse, and randomize it to not create any path that will help the website to find us
    mk2_website = call_website(website)
    data_key = find_data_key(mk2_website)
    theater_json = json.loads(call_website(f'{website}_next/data/{data_key}/default/recherche.json'))
    print(theater_json)