import wypok_bot_lib as w
import logging
from bs4 import BeautifulSoup
from coinbasepro_auth import get_ask_price
import CS_YT as cs
import datetime
import halving
import answer_dic


target_path = ""
logging.basicConfig(filename=target_path + 'logs.log', level=logging.INFO,
                    format='%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s|%(message)s')

def calculate_remining_days(year, month, day):
    return (datetime.date(year,month,day) - datetime.date.today()).days


def get_notifications():
    mesgs = w.read_notifications()
    new = False

    if mesgs != "err":
        for m in mesgs:
            id = m['id']
            user = f"@{m['author']['login']}"
            post = m['item_id']
            new = m['new']
            try:
                commentid = m['subitem_id']
                type = 1
            except Exception as e:
                commentid = ""
                type = 2

            if new == True:

                if type == 1:
                    logging.info(f'{id} {user} {post} {commentid}')
                    replay = parse_comment(w.get_comment(commentid))
                elif type == 2:
                    logging.info(f'{id} {user} {post} ')
                    replay = parse_comment(w.get_entry(post))

                if replay[0] == "cyberreturn":
                    days = calculate_remining_days(2020, 3, 7)
                    entry = f"@cyberpunkbtc wraca za {days} dni"
                elif replay[0] == "halving":
                    info = halving.get_halving_info()
                    entry = info["hinfo"]
                elif replay[0] == "btc price":
                    current_pricebtc = get_ask_price("BTC-USD")
                    if current_pricebtc != "err":
                        entry = f'Ostania cena ask BTC na coinbase pro: {current_pricebtc} $ '
                    else:
                        entry = f'Coś poszło nie tak, nie mogę ściągnąć ceny ;( '
                elif replay[0] == "eth price":
                    current_priceeth = get_ask_price("ETH-USD")
                    if current_priceeth != "err":
                        entry = f'Ostania cena ask ETH na coinbase pro: {current_priceeth} $ '
                    else:
                        entry = f'Coś poszło nie tak, nie mogę ściągnąć ceny ;( '
                elif  replay[0] == "Not found":
                    answer = cs.parse_response(cs.google_search_wypok(replay[1]))
                    if answer != "err":
                        entry = f'{user}: Dziękuję za komentarz/pytanie.\n' \
                                f'Niestety nie rozumiem jego treści.\n' \
                                f'Może tu znajdziesz odpowiedzi:\n' \
                                f'{answer}\n' \
                                f'Serdecznie pozdrawiam :)'
                    else:
                        entry = f'{user}: Dziękuję za komentarz/pytanie.\n' \
                                f'Niestety nie rozumiem jego treści.\n' \
                                f'Serdecznie pozdrawiam :)'
                else:
                    entry = f'{user}: {replay[0]}'
                w.add_comments(user, post, entry, img='')
    else:
        logging.info(f'Error podczas czytania powiadomien')
    # print(entry)
    #if new == False:
     #   logging.info(f'No new notifications')

def parse_comment(comment):
    body =  comment['data']['body']
    newbody = BeautifulSoup(body, "lxml").text.lower()
    cleanbody = newbody.replace("@atari_xe:","").replace("#bitcoin", "").\
        replace("#kryptowaluty", "").replace("#zombiebot","").\
        replace(":", "").strip()
    answer = answer_dic.get_answer(f'{cleanbody}')
    return (answer, cleanbody)


def main():
    get_notifications()
    w.mark_as_read_notifications()

main()
