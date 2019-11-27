import requests
import logging

target_path = ""
logging.basicConfig(filename=target_path + 'logs.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(filename)s:%(funcName)s:%(message)s')

def get_price(coin):
    if coin == 'btc':
        url ="https://api.coinbase.com/v2/prices/BTC-USD/buy"
        try:
            r = requests.get(url)
            c = r.json()
            content = float(c['data']['amount'])
        except Exception as e:
            logging.error(e)
            content = 'err'
    elif coin == 'eth':
        url = "https://api.coinbase.com/v2/prices/ETH-USD/buy"
        try:
            r = requests.get(url)
            c = r.json()
            content = float(c['data']['amount'])
        except Exception as e:
            logging.error(e)
            content = 'err'
    return content
