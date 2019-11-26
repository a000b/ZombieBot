import requests
import json
import os
import wypok_auth as w
import logging
target_path = ""
logging.basicConfig(filename=target_path + 'logs.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(filename)s:%(funcName)s:%(message)s')

def load_parms():
    pickle_f = 'parms.pickle'
    parms = w.load_file(target_path + pickle_f)
    if w.check_usrkey_isvalid(parms) == False:
        w.update_usr_key(target_path + pickle_f, parms)
    return parms



def add_entry(text, img, mode=0):
    my_pickle = load_parms()
    podpis = "\n\nhttps://github.com/a000b/ZombieBot\n\n"
    tagi = "#bitcoin #kryptowaluty #zombiebot"
    entry = text + podpis + tagi
    url = f"https://a2.wykop.pl/Entries/Add/appkey/{my_pickle['appkey']}/token/{my_pickle['usrkey']}/userkey/{my_pickle['usrkey']}/"

    if mode == 0:
        data = {'body': entry,
                'embed' : img}
        tajny = f"{my_pickle['secret']}{url}{entry},{img}"
        try:
            r = requests.post(url, data=data, headers=w.sign_data(tajny))
            logging.info(f"{text[:5]}")
        except Exception as e:
            logging.error(f"{e}{text[:5]}")
    else:
        myfiles = {'embed': (img, open(img ,'rb'), 'image/png')}
        data = {'body': entry}
        tajny = f"{my_pickle['secret']}{url}{entry}"
        try:
            r = requests.post(url, data=data, files=myfiles, headers=w.sign_data(tajny))
            logging.info(f"{text[:5]}")
        except Exception as e:
            logging.error(f"{e}{text[:5]}")



