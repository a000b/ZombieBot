import requests
import price
import wypok_bot_lib as w
import logging

target_path = ""
logging.basicConfig(filename=target_path + 'logs.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(filename)s:%(funcName)s:%(message)s')

def get_fee(coin):
    if coin == 'eth':
        try:
            url = "https://ethgasstation.info/json/ethgasAPI.json"
            r = requests.get(url)
            content = r.json()
        except Exception as e:
            logging.error(e)
            content = 'err'
    elif coin == 'btc':
        try:
            url = "https://mempool.space/api/v1/fees/recommended"
            r = requests.get(url)
            content = r.json()
        except Exception as e:
            logging.error(e)
            content = 'err'
    return content

def eth_fee(dane):
    size = 21000
    s = 10**9
    if dane != 'err':
        pricee = price.get_price('eth')
        if pricee != 'err':
            p = 'Price (Coinbase) : ' + str(pricee) + ' USD\n'
            fcost = str(round((float(dane['fast']) / 10)  * size * pricee / s,4)) + ' USD'
            ffcost = str(round((float(dane['fastest']) / 10) * size * pricee / s,4)) + ' USD'
            scost = str(round((float(dane['safeLow']) / 10) * size * pricee / s,4)) + ' USD'

            w = p + 'ETH recommended gas price.\nTx size 21000 gas:\n\n'
            fastesteth = f"< 30 seconds : {str(float(dane['fastest']) / 10):>8} gwei : ~{ffcost:>8}\n"
            fasteth = f"< 2 minutes  : {str(float(dane['fast']) / 10):>8} gwei : ~{fcost:>8}\n"
            safeloweth = f"< 30 minutes : {str(float(dane['safeLow']) / 10):>8} gwei : ~{scost:>8}\n\n"
            k = "https://ethgasstation.info/\n"
            entry = w + fastesteth + fasteth + safeloweth + k
        else:
            entry = 'err'
            logging.warning(f'Brak ceny ETH')
    else:
        entry ='err'
    return entry

def btc_fee(dane):
    size = 140
    s = 10**8
    if dane != 'err':
        priceb = price.get_price('btc')
        if priceb != 'err':
            p = 'Price (Coinbase) : ' + str(priceb) + ' USD\n'
            fcost = str(round(float(dane['fastestFee']) * size * priceb / s,4)) + ' USD'
            hcost = str(round(float(dane['halfHourFee']) * size * priceb / s,4)) + ' USD'
            ocost = str(round(float(dane['hourFee']) * size * priceb / s,4)) + ' USD'

            w = p + 'BTC recommended fee.\nTx size 140 VBytes:\n\n'
            fastestbtc = f"< 30 minutes : {str(dane['fastestFee']):>8} sat/VB : ~{fcost:>8}\n"
            halfhbtc = f"  30 minutes : {str(dane['halfHourFee']):>8} sat/VB : ~{hcost:>8}\n"
            onehbtc = f"     1 hour  : {str(dane['hourFee']):>8} sat/VB : ~{ocost:>8}\n\n"
            k = "https://mempool.space/"
            entry = w + fastestbtc + halfhbtc + onehbtc + k
        else:
            entry = 'err'
            logging.warning(f'Brak ceny BTC')
    else:
        entry = 'err'
    return entry

def main():
   b =  btc_fee(get_fee('btc'))
   e =  eth_fee(get_fee('eth'))
   if b != 'err' and e != 'err':
       entry = b + "\n\n" + e +"\n"
       img = ''
       print(entry)
       w.add_entry(entry, img)

main()