import wypok_bot_lib
import scr_lib, sys

def main():
    text = ''
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
    elif sys.argv[1] == 't':
        url = 'https://trends.google.pl/trends/explore?q=bitcoin'
        selector = "html"
    elif sys.argv[1] == 'vp':
        url = 'https://www.buybitcoinworldwide.com/volatility-index/'
        selector = "#highchart_simple_div"
        text += "BTC volatility / price index.\n\n"
    else:
        pass


    z = scr_lib.take_scr(url, 'scr.png', selector)
    w = wypok_bot_lib

    text += 'Źródło : ' + url +'\n\n'
    # print(text)
    w.add_entry(text,'scr.png', 1)



main()