import requests, json, wypok_bot_lib

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
    if dane != 'err':
        w = 'ETH recommended gas price:\n\n'
        fasteth =  'fast < 2 minutes : ' + str(float(dane['fast']) /10 ) + ' gwei\n'
        fastesteth = 'fastest < 30 seconds : ' + str(float(dane['fastest']) /10 ) + ' gwei\n'
        safeloweth = 'safelow < 30 minutes : ' + str(float(dane['safeLow']) /10 ) + ' gwei\n\n'
        k = "https://ethgasstation.info/"
        entry = w + fastesteth + fasteth + safeloweth + k
    else:
        entry ='err'
    return entry

def btc_fee(dane):
    if dane != 'err':
        w = 'BTC recommended fee:\n\n'
        fastestbtc =  'fastest : ' + str(dane['fastestFee']) + ' sat\n'
        halfhbtc = 'half hour : ' + str(dane['halfHourFee']) + ' sat\n'
        onehbtc = 'one hour : ' + str(dane['hourFee']) + ' sat\n\n'
        k = "https://mempool.space/"
        entry = w + fastestbtc + halfhbtc + onehbtc + k
    else:
        entry = 'err'
    return entry

def main():
   b =  btc_fee(get_fee('btc'))
   e =  eth_fee(get_fee('eth'))
   if b != 'err' and e != 'err':
       entry = b + "\n\n" + e
       w = wypok_bot_lib
       w.add_entry(entry)

main()