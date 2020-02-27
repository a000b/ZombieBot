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
    provider = Web3(Web3.HTTPProvider(data))
    return provider

def create_new_eth_account(provider):
    try:
        account = provider.eth.account.create()
    except Exception as e:
        account = None
        logging.error(e)
    return account

def connect_2_contract(provider, contract_address):
    contract = provider.eth.contract(address=provider.toChecksumAddress(contract_address),
                                     abi=read_file(f'{target_path}bot_contract_abi.json'))
    return contract


def get_answer_from_blokchain(question):
    data = read_file(f'{target_path}infura.api.json')
    contract = connect_2_contract(prepare_provider(data['rinkeby_url']), data["contract_bot_rinkeby"])
    return contract.functions.getAnswer(question).call()

def prepare_contract_url(contract_address):
    return f'https://rinkeby.etherscan.io/address/{contract_address}#code'

def get_contract_url():
    return prepare_contract_url(read_file(f'{target_path}infura.api.json')['contract_bot_rinkeby'])

def prepare_answer():
    new_account = create_new_eth_account(prepare_provider(read_file(f'{target_path}infura.api.json')['rinkeby_url']))
    if new_account is not None:
        priv_key = new_account.privateKey.hex()
        address = new_account.address
        return f'Twoje konto:\nhttps://rinkeby.etherscan.io/address/{address}\nKlucz prywatny: {priv_key[2:]}'
    else:
        return f'Coś poszło nie tak ;('
