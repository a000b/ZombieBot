import requests, hashlib, json, os

def main():
    global login
    global password
    global appkey
    global secret
    global acckey
    global usrkey
    global main_url
    global request_type
    global appkey_param 
    global acckey_param
    global usrkey_param
    global token_param
    
    parms = load_parms("auth_wykop.json")
 
    login = parms['login']
    password = parms['password']
    appkey = parms['appkey']
    secret = parms['secret']
    acckey = parms['acckey']
    usrkey = parms['usrkey']
    
    main_url = 'https://a2.wykop.pl/'
    request_type = 'Login/Index/'
    appkey_param = f'appkey/{appkey}/'
    acckey_param = f'accountkey/{acckey}/'
    usrkey_param = f'userkey/{usrkey}/'
    token_param = f'token/{usrkey}/'
    
    newkey = signin()
    if newkey != 'err':
        parms['usrkey'] = newkey
        usrkey = parms['usrkey']
        usrkey_param = f'userkey/{usrkey}/'
        token_param = f'token/{usrkey}/'
        print(token_param)

def load_parms(filename):
    with open(filename, "r", encoding='utf-8') as f:
        d = json.load(f)
    return d

def sign_data(data):
    headers ={}
    hash_d = hashlib.md5(data.encode())
    headers = {'apisign': hash_d.hexdigest()}
    return headers

def signin():
    url = f"{main_url}{request_type}{appkey_param}"
    tajny = f"{secret}{url}{login},{password},{acckey}"
    data = {'login': login, 'password': password, 'accountkey': acckey}

    try:
        r = requests.post(url, data=data, headers=sign_data(tajny))
        content = r.json()
        userkey = content['data']['userkey']
    except:
        userkey = 'err'
        print(r.json())
    return userkey

def add_entry(text, img, mode=0):
    podpis = "https://github.com/a000b/ZombieBot\n\n"
#     tagi = "#bitcoin #kryptowaluty #zombiebot"
    entry = text + podpis #+ tagi
    url = f'https://a2.wykop.pl/Entries/Add/{appkey_param}{token_param}{usrkey_param}'

    if mode == 0:
        data = {'body': entry,
                'embed' : img}
        tajny = f'{secret}{url}{entry},{img}'
        try:
            r = requests.post(url, data=data, headers=sign_data(tajny))
        except:
            print(r.json())
    else:
        myfiles = {'embed': (img, open(img ,'rb'), 'image/png')}
        data = {'body': entry}
        tajny = f'{secret}{url}{entry}'
        try:
            r = requests.post(url, data=data, files=myfiles, headers=sign_data(tajny))
        except:
            print(r.json())


main()


