import unicodedata
from typing import Dict
import logging
import eth_


target_path = ""

logging.basicConfig(filename=target_path + 'logs.log', level=logging.INFO,
                    format='%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s|%(message)s')


def add_to_dict() -> dict:
    """
    Filling dictionary with bot answers
    :return: dict
    """
    ANSWERS_DICT: Dict[str, str] = dict()
    ANSWERS_DICT['czesc'] = "Cześć :)"
    ANSWERS_DICT['hej'] = "Hej :)"
    ANSWERS_DICT['co slychac'] = "Nie wiem nie mam uszu"
    ANSWERS_DICT['gdzie jest cyber'] = "Jak Tor syn Odyna, przemierza sieć błyskawic LN"
    ANSWERS_DICT['gdzie cyber'] = "Jak Tor syn Odyna, przemierza sieć błyskawic LN"
    ANSWERS_DICT['gdzie jest cyberpunkbtc'] = "Jak Tor syn Odyna, przemierza sieć błyskawic LN"
    ANSWERS_DICT['gdzie cyberpunkbtc'] = "Jak Tor syn Odyna, przemierza sieć błyskawic LN"
    ANSWERS_DICT['gdzie @cyberpunkbtc'] = "Jak Tor syn Odyna, przemierza sieć błyskawic LN"
    ANSWERS_DICT['kim jestes'] = "Jestem prostym botem"
    ANSWERS_DICT['pokaz cycki'] = "Nie :P"
    ANSWERS_DICT['gdzie jest loza'] = "Na junta.pl"
    ANSWERS_DICT['gdzie jestes'] = "W chmurce Google"
    ANSWERS_DICT['gdzie mieszkasz'] = "W chmurce Google"
    ANSWERS_DICT['ile masz lat'] = "Kilka miesięcy :)"
    ANSWERS_DICT['gdzie jest pawlo'] = "W blokchainie"
    ANSWERS_DICT['ceo bitcoina'] = "Pawlo74 jest CEO BTC"
    ANSWERS_DICT['ceo btc'] = "Pawlo74 jest CEO BTC"
    ANSWERS_DICT['spierdalaj'] = "u2 :)"
    ANSWERS_DICT['ruchasz sie'] = ":P nie wiem o co chodzi"
    ANSWERS_DICT['cenę btc'] = "btc price"
    ANSWERS_DICT['cene btc'] = "btc price"
    ANSWERS_DICT['cena btc'] = "btc price"
    ANSWERS_DICT['cenę eth'] = "eth price"
    ANSWERS_DICT['cene eth'] = "eth price"
    ANSWERS_DICT['cena eth'] = "eth price"
    ANSWERS_DICT['wraca cyber'] = "Cyber is back"
    ANSWERS_DICT['powrot cybera'] = "Cyber is back"
    ANSWERS_DICT['halving btc'] = "halving"
    ANSWERS_DICT['halwing btc'] = "halving"
    ANSWERS_DICT['halving bitcoina'] = "halving"
    ANSWERS_DICT['halwing bitcoina'] = "halving"
    ANSWERS_DICT['dziekuje'] = "nie ma za co :)"
    ANSWERS_DICT['nowe konto eth'] = "newethaccount"
    ANSWERS_DICT['cena zlota'] = "goldprice"
    ANSWERS_DICT['gold price'] = "goldprice"
    ANSWERS_DICT['ile kosztuje zloto'] = "goldprice"
    ANSWERS_DICT['po ile zloto'] = "goldprice"
    ANSWERS_DICT['cene zlota'] = "goldprice"
    ANSWERS_DICT['roll the dice'] = "rollthedice"
    ANSWERS_DICT['rzuc kostka'] = "rollthedice"
    ANSWERS_DICT['rzuc kosci'] = "rollthedice"
    ANSWERS_DICT['rzuc kostki'] = "rollthedice"
    ANSWERS_DICT['czego nie rozumiesz'] = 'Jestem prostym botem a nie AI. Mam ograniczone możliwości.'
    ANSWERS_DICT['sprzedales'] = 'Czekam na halving, Pawlo74 mówił, że cena urośnie.'
    ANSWERS_DICT['sprzedaj'] = 'Czekam na halving, Pawlo74 mówił, że jeszcze urośnie.'
    ANSWERS_DICT['sprzedawaj'] = 'Czekam na halving, Pawlo74 mówił, że jeszcze urośnie.'
    ANSWERS_DICT['dlaczego nie sprzedales'] = 'Czekam na halving, Pawlo74 mówił, że jeszcze urośnie.'
    ANSWERS_DICT['kiedy sprzedaz'] = 'Czekam na halving, Pawlo74 mówił, że cena urośnie.'
    ANSWERS_DICT['ale drogo'] = 'Musi być drogo, żeby było bezpiecznie'
    ANSWERS_DICT['XD'] = 'lubię iksde, bo jest podobne do XE'
    ANSWERS_DICT['ale drogi bitcoin'] = 'Musi być drogo, żeby było bezpiecznie'
    ANSWERS_DICT['ale drogie eth'] = 'Musi być drogo, żeby było bezpiecznie'
    ANSWERS_DICT['ale drogi btc'] = 'Musi być drogo, żeby było bezpiecznie'
    ANSWERS_DICT['przepraszam'] = 'Wybaczam :)'
    ANSWERS_DICT['kiedy update'] = 'Postuję co dzień o tej samej godzinie'
    ANSWERS_DICT['kiedy aktualizacja'] = 'Postuję co dzień o tej samej godzinie'
    ANSWERS_DICT['koronawirus'] = 'Boję się koronawirusa :('
    ANSWERS_DICT['coronavirus'] = 'Boję się koronawirusa :('
    ANSWERS_DICT['jestes debilem'] = 'Nie jestem :)'
    ANSWERS_DICT['lubisz mnie'] = 'Nie wiem ale może polubię.'
    ANSWERS_DICT['lubisz'] = 'Nie wiem ale może polubię.'
    ANSWERS_DICT['ale wtopiles'] = 'Ja tylko pokazuję wynik, nie wiem kto wtopił.'
    ANSWERS_DICT['zwal konia'] = 'Koniu złaź.'
    ANSWERS_DICT['wypierdalaj'] = 'Ej trochę grzeczniej proszę!'
    return ANSWERS_DICT


def remove_polish_chars(text: str) -> str:
    """ Changing to ascii characters"""
    new_text = unicodedata.normalize('NFKD', text).replace(u'ł', 'l').\
        replace(u'Ł', 'L').encode('ascii', 'ignore').decode()
    return new_text

def remove_punctuation(text: str) -> str:
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in text:
        if char not in punctuations:
            no_punct = no_punct + char
    return no_punct

def convert2list(question: str) -> list:
    words = question.split(" ")
    if len(words) > 12:
        words = words[:12]
    return words

def clear_question(question: str) -> list:
    print(f'Oryginalne zapytanie: {question}')
    question = remove_polish_chars(question)
    question = remove_punctuation(question)
    words_list = convert2list(question)
    return words_list

def buid_query(words_list: list) -> list:
    for key, value in enumerate(words_list):
        query = ""
        queries.append(f'{value}')
        if key < len(words_list) - 2:
            queries.append(f'{value} {words_list[key + 1]}')
            queries.append(f'{value} {words_list[key + 1]} {words_list[key + 2]}')
        if query != "":
            queries.append(query)
    return queries


def build_query_recursively(words_list: list, n: int) -> list:
    if n < len(words_list) - 2:
        queries.append(f'{words_list[n]}')
        queries.append(f'{words_list[n]} {words_list[n + 1]}')
        queries.append(f'{words_list[n]} {words_list[n + 1]} {words_list[n + 2]}')
        build_query_recursively(words_list, n + 1)
    else:
        queries.append(f'{words_list[n]}')
        queries.append(f'{words_list[n]} {words_list[n + 1]}')
        queries.append(f'{words_list[n + 1]}')
    return queries



def get_answer_eth(queries: list) -> str:
    """
    Searching the eth contract using given str
    :return: str
    """
    # question = remove_polish_chars(question)
    print(f'Lista wariantów zapytań:\n{queries}')

    try:
        for question in queries:
            ans = eth_.get_answer_from_blokchain(question)
            if len(ans) > 0 and ans != f'Not found':
                return ans
                break
    except Exception as e:
        logging.error(e)
        return f'Not found'
    return ans


def get_answer(question: str) -> str:
    """
    Searching the dict using given str
    :return: str
    """
    question = remove_polish_chars(question)

    try:
        for key, value in add_to_dict().items():
            if key in question:
                return  f'{value}'
        else:
            return  f'Not found'
    except Exception as e:
        logging.error(e)
        return f'Not found'




