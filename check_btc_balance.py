# API w linku https://github.com/blockstream/esplora/blob/master/API.md

import requests
import pickle
import wypok_bot_lib as w


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
    for addr in addresses:
        try:
            response = requests.get('https://blockstream.info/api/address/' + addr)
        except Exception as e:
            pass
        else:
            if response.status_code == 200:
                content = response.json()
                balance = (int(content['chain_stats']['funded_txo_sum']) - int(content['chain_stats']['spent_txo_sum'])) / 10**8
                entry_balance = {'link' : 'https://blockstream.info/address/' + addr, 'balance' : balance}
                txs_entry = getx(addr)
                entry = {**entry_balance, **txs_entry}
                entry_list.append(entry)
                print(entry_list)
            else:
                pass
    return entry_list

def getx(address):
    try:
        response = requests.get('https://blockstream.info/api/address/' + address + "/txs")
    except Exception as e:
        pass
    else:
        if response.status_code == 200:
            content = response.json()
            for k, e in enumerate(content):
                entry_tx = {"last txid" : content[0]["txid"], 'block_height': content[0]["status"]["block_height"], "address" : address}
        else:
            pass
    return entry_tx


def save_file(dane):
    with open("balance.pickle", "wb") as plik:
        pickle.dump(dane, plik)


def read_file():
    with open("balance.pickle", "rb") as plik:
        list_read = pickle.load(plik)
    return list_read

def find_text(search_string):
    existing_list = read_file()
    for s in existing_list:
        found = str(s).find(search_string)
        if found != -1:
            return s['block_height'], s['balance']
        else:
            pass


def main():
    lista_wpis = []
    my_mesg = "Palenie BTC;\nsprawdzenie znanych bogus addresses;\nczęstotliwość sprawdzenia 1x24h\n\n"
    entries = getbalance(addr_list)

    if len(entries) != 0:
        for entry in entries:
            print(entry)
            search_ = find_text(entry["address"])
            if entry['block_height'] != search_[0]:
                diff_ = float(entry['balance']) - float(search_[1])
                entry.update({'change': f'{diff_:10.8f}' })
                lista_wpis.append(entry)
        if len(lista_wpis) != 0:
            for m in lista_wpis:
                my_mesg += f"Adres :{m['address']}\n" \
                    f"Balance :{m['balance']}\n" \
                    f"Zmiana  :{m['change']}\n" \
                    f"Last block tx :{m['block_height']}\n" \
                    f"Link : {m['link']} \n\n"
            img = ''
            w.add_entry(my_mesg, img)
    else:
        print('err')
    save_file(entries)

main()