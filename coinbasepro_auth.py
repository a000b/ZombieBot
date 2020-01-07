import json, hmac, hashlib, time, requests, base64
from requests.auth import AuthBase
import logging


target_path = ""
logging.basicConfig(filename=target_path + 'logs.log', level=logging.INFO,
                    format='%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s|%(message)s')


class CoinbaseExchangeAuth(AuthBase):
    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase

    def __call__(self, request):
        timestamp = str(time.time())
        message = timestamp + request.method + request.path_url + (request.body or b'').decode()
        hmac_key = base64.b64decode(self.secret_key)
        signature = hmac.new(hmac_key, message.encode(), hashlib.sha256)
        signature_b64 = base64.b64encode(signature.digest()).decode()

        request.headers.update({
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
            'CB-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        })
        return request


def read_file(filename):
    try:
        f = open(filename, "r", encoding='utf-8')
    except Exception as e:
        logging.error(e)
        d = "err"
    else:
        d = json.load(f)
    finally:
        f.close()
    return d

def get_auth_params():
    auth_file = read_file("auth_coinbasepro.json")

    if auth_file != "err":
        API_KEY = auth_file["API_KEY"]
        API_SECRET = auth_file["API_SECRET"]
        API_PASS = auth_file["API_PASS"]
        try:
            auth = CoinbaseExchangeAuth(API_KEY, API_SECRET, API_PASS)
        except Exception as e:
            logging.error(e)
            auth = "err"
    else:
        auth = 'err'
    return auth

def get_ask_price(currency_pair):
    productid = currency_pair
    api_url = 'https://api.pro.coinbase.com/'
    auth_parms = get_auth_params()
    if auth_parms != "err":
        try:
            r = requests.get(f"{api_url}/products/{productid}/book", auth=auth_parms)
        except Exception as e:
            logging.error(e)
            ask = "err"
        else:
            try:
                ask = r.json()['asks'][0][0]
            except Exception as e:
                logging.error(e)
                ask = "err"
    return ask
