from typing import Dict
import logging

target_path: str = ""
target_path = ""
logging.basicConfig(filename=target_path + 'logs.log', level=logging.INFO,
                    format='%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s|%(message)s')


def add_to_dict() -> dict:
    """
    Filling dictionary with bot answers
    :return: dict
    """
    ANSWERS_DICT: Dict[str, str] = dict()
    ANSWERS_DICT['cześć'] = "Cześć :)"
    ANSWERS_DICT['hej'] = "Hej :)"
    ANSWERS_DICT['co słychać'] = "Nie wiem nie mam uszu"
    ANSWERS_DICT['gdzie jest cyber'] = "Cyber dzban dostał ban XD"
    ANSWERS_DICT['kim jesteś'] = "Jestem prostym botem"
    ANSWERS_DICT['pokaż cycki'] = "Nie :P"
    ANSWERS_DICT['gdzie jest loża'] = "Na junta.pl"
    ANSWERS_DICT['gdzie jesteś'] = "W chmurce Google"
    ANSWERS_DICT['gdzie mieszkasz'] = "W chmurce Google"
    ANSWERS_DICT['ile masz lat'] = "Kilka miesięcy :)"
    ANSWERS_DICT['gdzie jest pawlo'] = "W blokchainie"
    ANSWERS_DICT['ceo bitcoina'] = "Pawlo74 jest CEO BTC"
    ANSWERS_DICT['ceo btc'] = "Pawlo74 jest CEO BTC"
    ANSWERS_DICT['spierdalaj'] = "u2 :)"
    ANSWERS_DICT['ruchasz się'] = ":P nie wiem o co chodzi"
    ANSWERS_DICT['cenę btc'] = "btc price"
    ANSWERS_DICT['cene btc'] = "btc price"
    ANSWERS_DICT['cena btc'] = "btc price"
    ANSWERS_DICT['cenę eth'] = "eth price"
    ANSWERS_DICT['cene eth'] = "eth price"
    ANSWERS_DICT['cena eth'] = "eth price"
    ANSWERS_DICT['wraca cyber'] = "cyberreturn"
    ANSWERS_DICT['powrót cybera'] = "cyberreturn"
    ANSWERS_DICT['powrót cyberzejba'] = "cyberreturn"
    ANSWERS_DICT['halving btc'] = "halving"
    ANSWERS_DICT['halwing btc'] = "halving"
    ANSWERS_DICT['halving bitcoina'] = "halving"
    ANSWERS_DICT['halwing bitcoina'] = "halving"
    ANSWERS_DICT['dziękuję'] = "nie ma za co :)"
    ANSWERS_DICT['nowe konto eth'] = "newethaccount"
    ANSWERS_DICT['cena złota'] = "goldprice"
    ANSWERS_DICT['gold price'] = "goldprice"
    ANSWERS_DICT['ile kosztuje złoto'] = "goldprice"
    ANSWERS_DICT['po ile złoto'] = "goldprice"
    ANSWERS_DICT['cenę złota'] = "goldprice"
    return ANSWERS_DICT


def get_answer(question: str) -> str:
    """
    Searching the dict using given str
    :return: str
    """

    try:
        for key, value in add_to_dict().items():
            if key in question:
                return  f'{value}'
        else:
            return  f'Not found'
    except:
        return f'Not found'



