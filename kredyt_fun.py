import wypok_bot_lib
from nbp_api import queryNBP, build_url
from price import get_price
from typing import Any
import pickle
import logging

target_path = ''
fname = 'loan'

logging.basicConfig(filename=target_path + 'logs.log', level=logging.INFO,
                    format='%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s|%(message)s')

def load_pickle(fname: str = 'data') -> Any:
    plk = []
    try:
        with open(f'{target_path}/{fname}.plk', 'rb') as f:
            while True:
                plk.append(pickle.load(f))
    except EOFError:
        return plk
    except Exception as e:
        logging.error(f'Pickle loading error:\n{e}')


def save2pickle(data: Any, fname: str = 'loan') -> bool:
    """Save data to pikle file.
    :param data
    :param fname file name, default value - data
    :returns bool True if success, False if doesn't"""
    try:
        with open(f'{target_path}/{fname}.plk', "wb") as p:
            pickle.dump(data, p)
    except Exception as e:
        logging.error(f'Pickle writing error:\n{e}')
    else:
        return True

def main():
    try:
        price = float(get_price('btc'))
    except:
        price = 'err'

    try:
        rate = float(queryNBP(build_url(selector='usd'))[1]['rates'][0]['mid'])
    except:
        rate = 'err'


    if price != 'err' and rate != 'err':

        flat = float(2538.29)
        # flat = 0
        loan = float(121838.15)

        my_plk = load_pickle(fname)
        print(my_plk)
        btc_plk = float(my_plk[0]['btc_current'])
        mc_plk = int(my_plk[0]['mc'])
        loan_plk = float(my_plk[0]['loan_current'])

        flat_dollars = float(flat / rate)
        exchange_fee = 0.005 * flat_dollars
        flat_dollars += exchange_fee
        flat_btc = flat_dollars / price

        new_btc = round(float(btc_plk - flat_btc),10)
        new_mc = mc_plk + 1
        new_loan = loan_plk - flat
        new_btc_pln = new_btc * price * rate

        new_data = {'mc': new_mc, 'btc_current': new_btc, 'loan_current': new_loan, 'btc_pl': new_btc_pln}
        save2pickle(new_data)

        w = wypok_bot_lib
        entry = f"Kredyt na BTC fun.\n" \
                f"W dniu 29 maja 2020 za poradą @rysiekryszard wzięto 100 000 PLN kredytu na zakup BTC.\n" \
                f"10 każdego miesiąca, z zakupionych BTC, będzie spłacana rata kredytu.\n" \
                f"Oznacza, to sprzedaż BTC o wartości równej racie + 0.5% prowizji giełdowej.\n" \
                f"Tym samym pomniejszenie ilości BTC.\n\n" \
                f"Całkowity koszt kredytu: {loan:.2f} PLN\n" \
                f"Bieżąca wartość BTC: {new_btc_pln:.4f} PLN\n" \
                f"Bieżąca ilość BTC: {new_btc}\n" \
                f"Rata numer: {mc_plk}\n" \
                f"Cena BTC Coinbase: {price} $\n" \
                f"Kurs USD NBP: {rate}\n" \
                f"Wartość raty: {flat} PLN, {flat_dollars:.4f} $, {flat_btc:8f} BTC"
        w.add_entry(entry, f'{target_path}/rysiek_investment.png', 1)

    else:
        logging.error(f'Stopped')

main()

# data = {'mc': 0, 'btc_current': 2.58913925, 'loan_current': 121838.15, 'btc_pln': 99500 }
# save2pickle(data=data)
# print(load_pickle(fname))