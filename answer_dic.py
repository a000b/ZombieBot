import unicodedata
from typing import Dict
import logging

target_path: str = "/home/maciej/myfiles/"

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
    ANSWERS_DICT['gdzie jest cyber'] = "Cyber dzban dostał ban XD"
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
    ANSWERS_DICT['wraca cyber'] = "cyberreturn"
    ANSWERS_DICT['powrot cybera'] = "cyberreturn"
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
    return ANSWERS_DICT


def remove_polish_chars(text: str) -> str:
    """ Changing to ascii characters"""
    return str(unicodedata.normalize('NFKD', text)
               .replace(u'ł', 'l').replace(u'Ł', 'L').
               encode('ascii', 'ignore'))


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


