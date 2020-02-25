from web3 import Web3
import logging
import json


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

def prepare_provider(data):
    infura_url = data['rinkeby_url']
    provider = Web3(Web3.HTTPProvider(infura_url))
    return provider

def create_new_eth_account(provider):
    try:
        account = provider.eth.account.create()
    except Exception as e:
        account = None
        logging.error(e)
    return account


def prepare_answer():
    new_account = create_new_eth_account(prepare_provider(read_file(f'{target_path}infura.api.json')))
    if new_account is not None:
        priv_key = new_account.privateKey.hex()
        address = new_account.address
        return f'Twoje konto:\nhttps://rinkeby.etherscan.io/address/{address}\nKlucz prywatny: {priv_key[2:]}'
    else:
        return f'Coś poszło nie tak ;('
