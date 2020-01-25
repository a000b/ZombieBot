import requests
import logging
import json

target_path = ""

logging.basicConfig(filename=target_path + 'logs.log', level=logging.INFO,
                    format='%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s|%(message)s')


def read_file(filename):
    with open(target_path + filename, "r", encoding='utf-8') as f:
        d = json.load(f)
    return d

API_URL = "https://www.googleapis.com/customsearch/v1?"

def google_search_wypok(query):
    auth = read_file("cs_yt.json")
    API_KEY = auth["API_KEY"]
    WYPOK_CX = auth["WYPOK_CX"]
    url = f'{API_URL}q={query}&dateRestrict=m6&cx={WYPOK_CX}&key={API_KEY}'
    content = "err"
    try:
        r = requests.get(url)
    except Exception as e:
        logging.error({e})
    else:
        content = r.json()
    return content

def parse_response(text):
    counter = 0
    links = ""
    if text != "err":
        try:
            responses = text['items']
        except Exception as e:
            logging.error(f'{e}{text}')
            links = "err"
        else:
            for item in responses:
                if counter < 3:
                    try:
                        links += str(item["link"]) + "\n"
                    except Exception as e:
                        logging.error({e})
                    else:
                        counter += 1
    return links

