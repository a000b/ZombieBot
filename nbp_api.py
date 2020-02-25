import requests
import logging

target_path: str = ""
target_path = ""
logging.basicConfig(filename=target_path + 'logs.log', level=logging.INFO,
                    format='%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s|%(message)s')


def build_url(selector: str, days: int = 1)  -> str:
    host_url: str = "https://api.nbp.pl/api"
    if selector == "goldprice":
        url = f'{host_url}/cenyzlota/last/{days}/?format=json'
    else:
        url = "Not found"
    return url


def queryNBP(url: str) -> list:
    result: list = list()

    if url != "Not found":
        try:
            r = requests.get(url)
            content = r.json()
        except Exception as e:
            logging.error(f"{e}")
            result.append("err")
        else:
            if r.status_code == 200:
                result.append('ok')
                result.append(content)
            else:
                logging.error(content)
                result.append('err')
    else:
        result.append("err")
    return result

