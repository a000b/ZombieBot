import requests
import json
import logging
import wypok_bot_lib

target_path = ""
target_path = ""

logging.basicConfig(filename=target_path + 'logs.log', level=logging.INFO,
                    format='%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s|%(message)s')


def read_file(filename):
    try:
        f = open(filename, "r", encoding='utf-8')
    except Exception as e:
        logging.error(e)
        d = 'err'
    else:
        d = json.load(f)
    finally:
        f.close()
    return d

def get_data(token):
    global API_KEY
    API_KEY = read_file(target_path + "loanscan_secret.json")["x-api-key"]
    search_url = f"https://api.loanscan.io/v1/interest-rates?tokenFilter={token}"
    headers = {"x-api-key": API_KEY}

    try:
        r = requests.get(search_url, headers=headers)
        content = r.json()
    except Exception as e:
        logging.error(e)
        content = 'err'
    return content


def create_entry():

    wstep = "Earn interest rates: \n\n"
    url = "https://loanscan.io/"
    tokens = []
    providers = []
    tokens.append('USDC')
    tokens.append("DAI")
    tokens.append("SAI")
    providers.append('CompoundV2')
    providers.append('dYdX')
    providers.append('MakerDaoV2')
    entry = wstep
    success_rate = 0

    for token in tokens:
        token_data = get_data(token)
        if token_data != 'err':
            for item in token_data:
                if (item['provider'] in providers):
                    try:
                        irate = round(float(item['supply'][0]['rate']) * 100, 2)
                        text = f"{item['supply'][0]['symbol']} {item['provider']} : {irate} %\n"
                        success_rate += 1
                    except IndexError:
                        logging.warning(f"{item['provider']} {token} Nie listowany")
                    except Exception as e:
                        logging.error(f"{item['provider']} {token} {e}")
                    else:
                        entry += text

    if success_rate > 0:
        entry += f"\nŹródło: {url}"
    else:
        entry = "err"
    return entry

def main():
    entry = create_entry()
    if entry != 'err':
       entry = entry +"\n\n"
       img = ''
       print(entry)
       # w = wypok_bot_lib
       # w.add_entry(entry, img)

main()