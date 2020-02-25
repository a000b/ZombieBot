# API w linku https://github.com/blockstream/esplora/blob/master/API.md

import requests
import pickle
import wypok_bot_lib as w
import logging


target_path = ""
logging.basicConfig(filename=target_path + 'logs.log', level=logging.INFO,
                    format='%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s|%(message)s')

addr_list = []
addr_list.append("1BitcoinEaterAddressDontSendf59kuE")
addr_list.append("1CounterpartyXXXXXXXXXXXXXXXUWLpVr")
addr_list.append("1QLbz7JHiBTspS962RLKV8GndWFwi5j6Qr")
addr_list.append("1111111111111111111114oLvT2")
entry_list = []


def getbalance(addresses):
    entry = {}
    entry_balance = {}
    balance = 0
    content = 'err'
    for addr in addresses:
        try:
            response = requests.get('https://blockstream.info/api/address/' + addr)
        except Exception as e:
            logging.error(e)
        else:
            if response.status_code == 200:
                try:
                    content = response.json()
                    balance = (int(content['chain_stats']['funded_txo_sum']) - int(content['chain_stats']['spent_txo_sum'])) / 10**8
                    entry_balance = {'link' : 'https://blockstream.info/address/' + addr, 'balance' : balance}
                    txs_entry = getx(addr)
                    entry = {**entry_balance, **txs_entry}
                    entry_list.append(entry)
                except Exception as e:
                    logging.error(e)
                    logging.error(content)
    return entry_list

def getx(address):
    content = 'err'
    entry_tx = {}
    try:
        response = requests.get('https://blockstream.info/api/address/' + address + "/txs")
    except Exception as e:
        logging.error(e)
    else:
        if response.status_code == 200:
            try:
                content = response.json()
                entry_tx = {"last txid" : content[0]["txid"], 'block_height': content[0]["status"]["block_height"], "address" : address}
            except Exception as e:
                logging.error(e)
                logging.error(content)
    return entry_tx


def save_file(dane):
    with open(target_path + "balance.pickle", "wb") as plik:
        pickle.dump(dane, plik)


def read_file():
    with open(target_path + "balance.pickle", "rb") as plik:
        list_read = pickle.load(plik)
    return list_read

def find_text(search_string):
    existing_list = read_file()
    for s in existing_list:
        found = str(s).find(search_string)
        if found != -1:
            return s['block_height'], s['balance']


def main():
    lista_wpis = []
    my_mesg = "Palenie BTC\nSprawdzenie znanych bogus(martwych) adresów\nCzęstotliwość sprawdzenia 1xweek\n\n"
    entries = getbalance(addr_list)

    if len(entries) != 0:
        for entry in entries:
            search_ = find_text(entry["address"])
            if entry['block_height'] != search_[0]:
                diff_ = float(entry['balance']) - float(search_[1])
                entry.update({'change': f'{diff_:10.8f}' })
                lista_wpis.append(entry)
        if len(lista_wpis) != 0:
            for m in lista_wpis:
                my_mesg += f"Adres : {m['address']}\n" \
                    f"Balance : {m['balance']}\n" \
                    f"Zmiana  : {m['change']}\n" \
                    f"Last block tx : {m['block_height']}\n" \
                    f"Link : {m['link']} \n\n"
            img = ''
            w.add_entry(my_mesg, img)

    save_file(entries)

main()
