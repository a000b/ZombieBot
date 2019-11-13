import requests
import json
import os
import wypok_auth as w


def load_parms():
    target_path = ""
    pickle_f = 'parms.pickle'
    parms = w.load_file(target_path + pickle_f)
    if w.check_usrkey_isvalid(parms) == False:
        w.update_usr_key(target_path + pickle_f, parms)
    print(parms)
    return parms



def add_entry(text, img, mode=0):
    my_pickle = load_parms()
    podpis = "\n\nhttps://github.com/a000b/ZombieBot/blob/master/check_btc_balance.py\n" \
            "https://github.com/a000b/ZombieBot\n\n"
    tagi = "#bitcoin #kryptowaluty #zombiebot"
    entry = text + podpis + tagi
    url = f"https://a2.wykop.pl/Entries/Add/appkey/{my_pickle['appkey']}/token/{my_pickle['usrkey']}/userkey/{my_pickle['usrkey']}/"
    print(url)

    if mode == 0:
        data = {'body': entry,
                'embed' : img}
        tajny = f"{my_pickle['secret']}{url}{entry},{img}"
        try:
            r = requests.post(url, data=data, headers=w.sign_data(tajny))
            print(r.text)
        except:
            print(r.json())
    else:
        myfiles = {'embed': (img, open(img ,'rb'), 'image/png')}
        data = {'body': entry}
        tajny = f"{my_pickle['secret']}{url}{entry}"
        try:
            r = requests.post(url, data=data, files=myfiles, headers=w.sign_data(tajny))
        except:
            print(r.json())



