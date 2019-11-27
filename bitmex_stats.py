import requests as r
import locale
import wypok_bot_lib as w
import pickle
import logging

target_path = ""
logging.basicConfig(filename=target_path + 'logs.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(filename)s:%(funcName)s:%(message)s')
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

def save_file(dane):
    with open("turnover.pickle", "wb") as plik:
        pickle.dump(dane, plik)


def read_file():
    with open("turnover.pickle", "rb") as plik:
        list_read = pickle.load(plik)
    return list_read

def get_stats(*args):
    url = "https://www.bitmex.com/api/v1/" + args[0]
    try:
        response = r.get(url)
    except Exception as e:
        logging.error(e)
        entry = 'err'
    else:
        if response.status_code == 200:
            content = response.json()
            for entry_ in content:
                if entry_ ['rootSymbol'] == "XBT":
                    diff = round((int(entry_["turnover24h"]) - read_file()) / read_file() * 100, 1)
                    t24 = locale.format_string(f="%.0f", val=entry_["turnover24h"], grouping=True)
                    t365 = locale.format_string(f="%.0f", val=entry_["turnover365d"], grouping=True)
                    t = locale.format_string(f="%.0f", val=entry_["turnover"], grouping=True)
                    entry = f'{"Turnover"} : {t} USD\n' \
                            f'{"Turnover365"} : {t365} USD\n' \
                            f'{"Turnover24"} : {t24} USD | {"Change24"} : {diff} %\n\n'
                    entry = entry.replace(",", " ")
                    save_file(entry_["turnover24h"])
        else:
            logging.warning("Problem z danymi Bitmex")
            entry = 'err'
    return entry


def main():
    urls = ["stats/historyUSD", "stats"]
    e = get_stats(urls[0])
    entry = "Bitmex statistics\nXBT turnover\n\n"
    end_ = "\n\nŻródło: https://www.bitmex.com/"
    if e != 'err':
        entry  += e
        entry += end_
        img = ''
        w.add_entry(entry, img)

main()
