import requests
import json
import os
import wypok_auth as w
import logging


target_path = ""
logging.basicConfig(filename=target_path + 'logs.log', level=logging.INFO,
                    format='%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s|%(message)s')

def load_parms():
    pickle_f = 'parms.pickle'
    parms = w.load_file(target_path + pickle_f)
    check = w.check_usrkey_isvalid(parms)
    if  check == 0:
        return parms
    elif check == 1:
        if w.update_usr_key(target_path + pickle_f, parms) == True:
            parms_updated = w.load_file(target_path + pickle_f)
            return parms_updated
        else:
            return "err"
    else:
        return 'err'


def add_entry(text, img, mode=0):
    my_pickle = load_parms()
    if my_pickle != 'err':
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
                logging.info(f"{text[:10]} |https://www.wykop.pl/wpis/{r.json()['data']['id']}/")
            except Exception as e:
                logging.error(f"{e}{text[:10]}")
        else:
            myfiles = {'embed': (img, open(img ,'rb'), 'image/png')}
            data = {'body': entry}
            tajny = f"{my_pickle['secret']}{url}{entry}"
            try:
                r = requests.post(url, data=data, files=myfiles, headers=w.sign_data(tajny))
                logging.info(f"{text[:10]} |https://www.wykop.pl/wpis/{r.json()['data']['id']}/")
            except Exception as e:
                logging.error(f"{e}{text[:10]}")
    else:
        logging.error(f"Nie udało sie {text[:10]}")


def read_notifications():
    my_pickle = load_parms()
    if my_pickle != "err":
        url = f"https://a2.wykop.pl/Notifications/Index/page/1/{my_pickle['login']}/appkey/{my_pickle['appkey']}/userkey/{my_pickle['usrkey']}/"
        tajny = f"{my_pickle['secret']}{url}"
        try:
            r = requests.get(url, headers=w.sign_data(tajny))
            text = r.text
            content = r.json()['data']
            count_mesgs = len(content)
           # logging.info(f"{count_mesgs} notifications on page")
        except Exception as e:
            logging.error(f"{e}")
            content = "err"
        return content
    else:
        return "err"


def add_comments(user, commented_post, text, img, mode=0):
    my_pickle = load_parms()
    if my_pickle != "err":
        entry = text
        url = f"https://a2.wykop.pl/Entries/CommentAdd/{commented_post}/appkey/{my_pickle['appkey']}/token/{my_pickle['usrkey']}/userkey/{my_pickle['usrkey']}/"

        if mode == 0:
            data = {'body': entry,
                    'embed': img}
            tajny = f"{my_pickle['secret']}{url}{entry},{img}"
            try:
                r = requests.post(url, data=data, headers=w.sign_data(tajny))
                logging.info(f"{user} |https://www.wykop.pl/wpis/{commented_post}/#comment-{r.json()['data']['id']}/")
            except Exception as e:
                logging.error(f"{e} {user} {commented_post}")
        else:
            myfiles = {'embed': (img, open(img, 'rb'), 'image/png')}
            data = {'body': entry}
            tajny = f"{my_pickle['secret']}{url}{entry}"
            try:
                r = requests.post(url, data=data, files=myfiles, headers=w.sign_data(tajny))
                logging.info(f"{user} |https://www.wykop.pl/wpis/{commented_post}/#comment-{r.json()['data']['id']}/")
            except Exception as e:
                logging.error(f"{e} {user} {commented_post}")


def mark_as_read_notifications():
    my_pickle = load_parms()
    if my_pickle != "err":
        url = f"https://a2.wykop.pl/Notifications/ReadAllNotifications/{my_pickle['login']}/appkey/{my_pickle['appkey']}/userkey/{my_pickle['usrkey']}/"
        tajny = f"{my_pickle['secret']}{url}"
        try:
            r = requests.get(url, headers=w.sign_data(tajny))
           # logging.info(f"All marked as read: ok")
            text = r.text
            status = r.json()
        except Exception as e:
            logging.error(f"{e} {text}")
            status = 'err'
        return status
    else:
        return "err"

def get_comment(commentid):
    my_pickle = load_parms()
    if my_pickle != "err":
        url = f"https://a2.wykop.pl/Entries/Comment/{commentid}/{my_pickle['login']}/appkey/{my_pickle['appkey']}/userkey/{my_pickle['usrkey']}/"
        tajny = f"{my_pickle['secret']}{url}"
        try:
            r = requests.get(url, headers=w.sign_data(tajny))
           # logging.info(f"All marked as read: ok")
            text = r.text
            status = r.json()
        except Exception as e:
            logging.error(f"{e} {text}")
            status = 'err'
        return status
    else:
        return "err"

def get_entry(entryid):
    my_pickle = load_parms()
    if my_pickle != "err":
        url = f"https://a2.wykop.pl/Entries/Entry/{entryid}/{my_pickle['login']}/appkey/{my_pickle['appkey']}/userkey/{my_pickle['usrkey']}/"
        tajny = f"{my_pickle['secret']}{url}"
        try:
            r = requests.get(url, headers=w.sign_data(tajny))
           # logging.info(f"All marked as read: ok")
            text = r.text
            status = r.json()
        except Exception as e:
            logging.error(f"{e} {text}")
            status = 'err'
        return status
    else:
        return "err"