import requests, json, price
import wypok_bot_lib

def get_fee(coin):
    if coin == 'eth':
        try:
            url = "https://ethgasstation.info/json/ethgasAPI.json"
            r = requests.get(url)
            content = r.json()
        except:
            content = 'err'
    elif coin == 'btc':
        try:
            url = "https://mempool.space/api/v1/fees/recommended"
            r = requests.get(url)
            content = r.json()
        except:
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
        else:
            p = '\n'
            fcost = ''
            ffcost = ''
            scost = ''
        w = p + 'ETH recommended gas price, koszt policzony dla tx 21000 gas:\n\n'
        fastesteth = 'fastest < 30 seconds : ' + str(float(dane['fastest']) /10 ) + ' gwei : ~' + ffcost + ' za tx 21000 gas\n'
        fasteth =  'fast    < 2 minutes  : ' + str(float(dane['fast']) /10 ) + ' gwei ; ~' + fcost + ' za tx 21000 gas\n'
        safeloweth = 'safelow < 30 minutes : ' + str(float(dane['safeLow']) /10 ) + ' gwei : ~' + scost + ' za tx 21000 gas\n\n'
        k = "https://ethgasstation.info/\n"
        entry = w + fastesteth + fasteth + safeloweth + k
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
        else:
            p = '\n'
            fcost = ''
            hcost = ''
            ocost = ''
        w = p + 'BTC recommended fee, koszt policzony dla tx 140 VBytes:\n\n'
        fastestbtc =  'fastest   : ' + str(dane['fastestFee']) + ' sat/VB : ~' + fcost + ' za tx 140VB\n'
        halfhbtc = 'half hour : ' + str(dane['halfHourFee']) + ' sat/VB  : ~' + hcost + ' za tx 140VB\n'
        onehbtc = 'one hour  : ' + str(dane['hourFee']) + ' sat/VB : ~' + ocost + ' za tx 140VB\n\n'
        k = "https://mempool.space/"
        entry = w + fastestbtc + halfhbtc + onehbtc + k
    else:
        entry = 'err'
    return entry

def main():
   b =  btc_fee(get_fee('btc'))
   e =  eth_fee(get_fee('eth'))
   if b != 'err' and e != 'err':
       entry = b + "\n\n" + e +"\n"
       w = wypok_bot_lib
       w.add_entry(entry)

main()