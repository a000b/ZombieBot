import pickle
import requests
import hashlib
import logging

target_path = ""
logging.basicConfig(filename=target_path + 'logs.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(filename)s:%(funcName)s:%(message)s')

def check_usrkey_isvalid(kwargs):
    check = get_pm_conversation(kwargs)
    if check == 11:
        r = False
    elif check == 'err':
        logging.error('Błąd przy pobieraniu konwersacji')
    else:
        r = True
        logging.info('Wypok token aktualny')
    return r

def sign_data(data):
    headers ={}
    hash_d = hashlib.md5(data.encode())
    headers = {'apisign': hash_d.hexdigest()}
    return headers


def get_token(kwargs):
    url = f"https://a2.wykop.pl/Login/Index/appkey/{kwargs['appkey']}/"
    tajny = f"{kwargs['secret']}{url}{kwargs['login']},{kwargs['password']},{kwargs['acckey']}"
    data = {'login': kwargs['login'], 'password': kwargs['password'], 'accountkey': kwargs['acckey']}

    try:
        r = requests.post(url, data=data, headers=sign_data(tajny))
        content = r.json()
        userkey = content['data']['userkey']
    except Exception as e:
        userkey = 'err'
        logging.error(f'{e},{content}')
    return userkey


def get_pm_conversation(kwargs):
    url = f"https://a2.wykop.pl/Pm/ConversationsList/{kwargs['login']}/appkey/{kwargs['appkey']}/userkey/{kwargs['usrkey']}/"
    tajny = f"{kwargs['secret']}{url}"
    try:
        r = requests.get(url, headers=sign_data(tajny))

        if r.status_code == 200:
            content = r.json()
        else:
            content = r.json()['error']['code']
            logging.error(f"{content}")
            # print('Err :', r.status_code)
    except Exception as e:
        content = 'err'
        logging.error(f'{e}')

    return content


def load_file(fname):
    with open(fname, "rb", ) as p:
        auth_data = pickle.load(p)
    return auth_data


def save_file(fname, new_parms):
    with open(fname, "wb") as p:
        pickle.dump(new_parms, p)


def update_usr_key(fname, kwargs):
    newkey = get_token(kwargs)
    if newkey != 'err':
        kwargs['usrkey'] = newkey
        save_file(fname, kwargs)
        logging.info(f'Wypok token updated')

