import wypok_bot_lib as w
import scr_lib
import sys
import logging

target_path = ""


logging.basicConfig(filename=target_path + 'logs.log', level=logging.INFO,
                    format='%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s|%(message)s')
def main():
    text = ''
    try:
        if sys.argv[1] == 'dominance_graph':
            url = 'https://coinmarketcap.com/charts/'
            selector = "#dominance-percentage"
            text += "BTC dominance graph.\n\n"
        elif sys.argv[1] == 'volatility_btc':
            url = 'https://www.buybitcoinworldwide.com/volatility-index/'
            selector = "#highchart_simple_div"
            text += "BTC volatility / price index.\n\n"
        else:
            logging.error(f"Zly parametr: {sys.argv[1]}")
    except Exception as e:
        logging.error(e)
    else:
        try:
            pic = scr_lib.take_scr(url, target_path + 'scr.png', selector)
        except Exception as e:
            logging.error(e)
        else:
            if pic == True:
                text += 'Źródło : ' + url +'\n\n'
                w.add_entry(text, target_path + 'scr.png', 1)

main()