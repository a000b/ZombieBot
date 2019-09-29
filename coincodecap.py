import requests as r
import wypok_bot_lib

def main():    
    w = wypok_bot_lib
    symbol = ('Grin','BTC', 'ETH')
    for s in symbol:
        entry = str(new_entry(s))
        if entry != 'err':
            w.add_entry(entry)
        else:
            pass
    
def get_info(coin):
    url = 'https://api.coincodecap.com/v1/details/' + coin
    try:
        response = r.get(url)
        content = response.json()
    except:
        content = 'err'
    return content

def new_entry(arg):
    info = get_info(arg)[0]
    if info != 'e':
        items ="Statystki projektu\n\n"
        for item in info:
            items += str(item) +  " : " + str(info[item]) + "\n"

        entry = items.replace('_', ' ')
        url = '\nŹródło : https://api.coincodecap.com\n\n'
        entry = entry + url
    else:
        entry = 'err'       
    return(entry)

main()
