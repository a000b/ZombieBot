import requests as r
import wypok_bot_lib

def main():    
    w = wypok_bot_lib
    symbol = ('Grin','BTC', 'ETH')
    for s in symbol:
        w.add_entry(str(new_entry(s)))
    
def get_info(coin):
    url = 'https://api.coincodecap.com/v1/details/' + coin
    response = r.get(url)
    
    if response.status_code == 200:
        content = response.json()
    else:
        content = response.status_code
    return content

def new_entry(arg):

    info = get_info(arg)[0]
    items ="Statystki projektu\n\n"
    for item in info:
        items += str(item) +  " : " + str(info[item]) + "\n"

    entry = items.replace('_', ' ')
    url = '\nŹródło : https://api.coincodecap.com\n\n'
    tagi = '#bitcoin #kryptowaluty'
    entry = entry + url + tagi
            
    return(entry)

main()
