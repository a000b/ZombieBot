import requests, json


def get_price(coin):
    if coin == 'btc':
        url ="https://api.coinbase.com/v2/prices/BTC-USD/buy"
        try:
            r = requests.get(url)
            c = r.json()
            content = float(c['data']['amount'])
        except:
            content = 'err'
    elif coin == 'eth':
        url = "https://api.coinbase.com/v2/prices/ETH-USD/buy"
        try:
            r = requests.get(url)
            c = r.json()
            content = float(c['data']['amount'])
        except:
            content = 'err'
    return content
