import wypok_bot_lib
import scr_lib, sys

def main():
    if sys.argv[1] == 'd':
        url = 'https://coinmarketcap.com/charts/'
        selector = "#dominance-percentage-graph"
    elif sys.argv[1] == 'c':
        url = "https://www.cmegroup.com/trading/equity-index/us-index/bitcoin_quotes_volume_voi.html"
        selector = "#quotesProductPanel"
#         url = 'https://www.cmegroup.com/trading/equity-index/us-index/bitcoin_quotes_globex.html'
#         selector = "#quotesFuturesProductTable1"
    elif sys.argv[1] == 'b':
        url = "https://www.coingecko.com/en/exchanges/binance_futures"
        selector = "table"
    else:
        pass


    z = scr_lib.take_scr(url, 'scr.png', selector)
    w = wypok_bot_lib
    text = 'Źródło : ' + url +'\n\n'
    w.add_entry(text, img, 1)



main()