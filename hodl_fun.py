from halving import get_halving_info
from coinbasepro_auth import get_ask_price
import logging
import datetime
import wypok_bot_lib as w

target_path = ""

logging.basicConfig(filename=target_path + 'logs.log', level=logging.INFO,
                    format='%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s|%(message)s')

def calculate_initial_amounts(invested_amount_pln, rate_usdpln, initial_price_btc, initial_price_eth ):
    invested_amount_usd = round(float(invested_amount_pln / rate_usdpln), 4)
    amount_btc =  round(float(invested_amount_usd / initial_price_btc), 8)
    amount_eth = round(float(invested_amount_usd / initial_price_eth), 8)
    return (invested_amount_usd, amount_btc, amount_eth)

def calculate_roi(initial_amounts):

    current_pricebtc = get_ask_price("BTC-USD")
    current_priceeth = get_ask_price("ETH-USD")

    if current_pricebtc != "err":
        current_value_btc = round(float(initial_amounts[1]) * float(current_pricebtc), 4)
        roi_btc = round(((current_value_btc - float(initial_amounts[0])) / current_value_btc) * 100, 4)
    else:
        roi_btc = 'err'

    if current_priceeth != "err":
        current_value_eth = round(float(initial_amounts[2]) * float(current_priceeth), 4)
        roi_eth = round(((current_value_eth - float(initial_amounts[0])) / current_value_eth)* 100, 4)
    else:
        roi_eth = 'err'
    return current_pricebtc, roi_btc, current_priceeth, roi_eth

def create_entry():
    investment_date = datetime.date(2020,1, 7)
    today = datetime.date.today()
    fun_days = today - investment_date

    price_btc = 7894.21
    price_eth = 142.81
    amount_pln = 100000
    rate = 3.8

    initial_amounts = calculate_initial_amounts(amount_pln, rate, price_btc, price_eth )
    roi= calculate_roi(initial_amounts)
    info = get_halving_info()
    if roi[0] != 'err' and info['hinfo'] != "err":

        if float(roi[1]) > 0 and float(roi[3]) > 0:
            img = "moon_indicator.png"
        elif float(roi[1]) < 0 and float(roi[3]) < 0:
            img = "rekt_indicator.png"
        else:
            img = "neutral_indicator.png"

        entry = f"HODL {fun_days.days} dzień zabawy.\n" \
               f"Zainwestowano po 100 000 PLN w BTC i ETH w dniu {investment_date}\n" \
               f"ROI BTC: {roi[1]}%\n" \
               f"ROI ETH: {roi[3]}%\n" \
               f"{info['hinfo']}\n\n" \
               f"Szczegóły:\n" \
               f"Cena BTC w $: wejścia: {price_btc} bieżąca: {roi[0]}\n" \
               f"Cena ETH w $: wejścia: {price_eth} bieżąca: {roi[2]}\n" \
               f"Kurs wejścia USD-PLN: {rate}\n" \
               f"Ilość BTC: {initial_amounts[1]}\n" \
               f"Ilość ETH: {initial_amounts[2]}\n\n" \
               f"Ceny z https://api.pro.coinbase.com/"
    else:
        entry = "err"
        img = ""
    return entry, img

def main():
    wpis = create_entry()
    if wpis[0] != 'err':
       w.add_entry(wpis[0], target_path + wpis[1], 1)

main()
