import pickle
import requests
import hashlib
import logging

target_path = ""
logging.basicConfig(filename=target_path + 'logs.log', level=logging.INFO,
                    format='%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s|%(message)s')

def check_usrkey_isvalid(kwargs):
    check = get_pm_conversation(kwargs)
    if check == 'ok':
        r = True
        logging.info('Wypok token aktualny')
    elif check == 11:
        r = False
        logging.info('Proba aktualizacji tokenu')
    elif check == 'err':
        logging.error('Status err przerywam')
    else:
        logging.error('Dunno przerywam')
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
            status = 'ok'
        elif r.status_code == 401:
            try:
                content = r.json()
                status = content['error']['code']
                logging.warning(f"Token nieaktualny {content['error']['message_en']}")
            except Exception as e:
                logging.error(f"Dunno {e}")
                status = 'err'
        else:
            content = r.json()
            logging.warning(f"Dunno {content}")
            status = 'err'
    except Exception as e:
        status = 'err'
        logging.error(f'{e}')

    return status


def load_file(fname):
    try:
        f = open(fname, "rb", )
    except Exception as e:
        logging.error(f"{e}")
        auth_data = ""
    else:
        auth_data = pickle.load(f)
        logging.info(f'Otwarto plik {fname}')
        f.close()
    return auth_data


def save_file(fname, new_parms):
    try:
        with open(fname, "wb") as p:
            pickle.dump(new_parms, p)
            logging.info(f'Zapisano plik {fname}')
    except Exception as e:
        logging.error(f"{e}")

def update_usr_key(fname, kwargs):
    newkey = get_token(kwargs)
    if newkey != 'err':
        kwargs['usrkey'] = newkey
        save_file(fname, kwargs)
        logging.info(f'Wypok token updated')

