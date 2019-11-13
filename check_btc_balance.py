# API w linku https://github.com/blockstream/esplora/blob/master/API.md

import requests
import pickle
import pprint as pp
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
            # print(e)
            pass
        else:
            if response.status_code == 200:
                content = response.json()
                # pprint(content)
                balance = (int(content['chain_stats']['funded_txo_sum']) - int(content['chain_stats']['spent_txo_sum'])) / 10**8
                entry_balance = {'link' : 'https://blockstream.info/address/' + addr, 'balance' : balance}
                txs_entry = getx(addr)
                entry = {**entry_balance, **txs_entry}
                entry_list.append(entry)
            else:
                # print(response.status_code)
                pass
    return entry_list

def getx(address):
    try:
        response = requests.get('https://blockstream.info/api/address/' + address + "/txs")
    except Exception as e:
        # print(e)
        pass
    else:
        if response.status_code == 200:
            content = response.json()
            entry_tx = {"last txid" : content[0]["txid"], 'block_height': content[0]["status"]["block_height"], "address" : address}
            # print(content)
            # pp.pprint(content[0])
        else:
            # print(response.status_code)
            pass
    return entry_tx


def save_file(dane):
    with open("balance.pickle", "wb") as plik:
        pickle.dump(dane, plik)


def read_file():
    # list_read = []
    with open("balance.pickle", "rb") as plik:
        list_read = pickle.load(plik)
    return list_read

def find_text(search_string):
    existing_list = read_file()
    for k, s in enumerate(existing_list):
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
            search_ = find_text(entry["address"])
            if entry['block_height'] != search_[0]:
                diff_ = float(entry['balance']) - float(search_[1])
                # print(f'{diff_:10.8f}')
                entry.update({'change': f'{diff_:10.8f}' })
                lista_wpis.append(entry)
        if len(lista_wpis) != 0:
            for m in lista_wpis:
                my_mesg += f"Adres :{m['address']}\n" \
                    f"Balance :{m['balance']}\n" \
                    f"Zmiana  :{m['change']}\n" \
                    f"Last block tx :{m['block_height']}\n" \
                    f"Link : {m['link']} \n\n"
                # mesg += str(pp.pformat(m).replace('"','').replace("'", "").\
                #     replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace(",", "") ) + "\n\n"
            print(my_mesg)
            img = ''
            w.add_entry(my_mesg, img)
    else:
        print('err')
    save_file(entries)

main()
# b = {'link': 'https://blockstream.info/address/1BitcoinEaterAddressDontSendf59kuE', 'balance': 12.22480954, 'last txid': '585d11c224013b2521425b0733fe9f3de92d4d13019410c44c3ee3951f1b97df', 'block_height': 603310, 'address': '1BitcoinEaterAddressDontSendf59kuE'}, {'link': 'https://blockstream.info/address/1CounterpartyXXXXXXXXXXXXXXXUWLpVr', 'balance': 1130.87119421, 'last txid': '90212248b1753724b66d7994dd8c03e7c8b702b12851ec53b8e57edb092a78e8', 'block_height': 602920, 'address': '1CounterpartyXXXXXXXXXXXXXXXUWLpVr'}, {'link': 'https://blockstream.info/address/1QLbz7JHiBTspS962RLKV8GndWFwi5j6Qr', 'balance': 0.01249, 'last txid': '6240f61bbaeac66cd623e921a153addaf5f379a996f2de0f0c6506d628fe3812', 'block_height': 417350, 'address': '1QLbz7JHiBTspS962RLKV8GndWFwi5j6Qr'}, {'link': 'https://blockstream.info/address/1111111111111111111114oLvT2', 'balance': 9.44623692, 'last txid': 'b6332d101b1f21a02b50645c09b62644fed0064ce60fa5569f23ef6bfd27819a', 'block_height': 603480, 'address': '1111111111111111111114oLvT2'}
# save_file(b)
# print(read_file())