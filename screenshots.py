import wypok_bot_lib as w
import scr_lib, sys

def main():
    text = ''
    if sys.argv[1] == 'dominance':
        url = 'https://coinmarketcap.com/charts/'
        selector = "#dominance-percentage"
    elif sys.argv[1] == 'cme':
        url = "https://www.cmegroup.com/trading/equity-index/us-index/bitcoin_quotes_volume_voi.html"
        selector = "#quotesProductPanel"
#         url = 'https://www.cmegroup.com/trading/equity-index/us-index/bitcoin_quotes_globex.html'
#         selector = "#quotesFuturesProductTable1"
    elif sys.argv[1] == 'binance_futures':
        url = "https://www.coingecko.com/en/exchanges/binance_futures"
        selector = "table"
    elif sys.argv[1] == 'google_trends':
        url = 'https://trends.google.pl/trends/explore?q=bitcoin'
        selector = "html"
    elif sys.argv[1] == 'volatility_btc':
        url = 'https://www.buybitcoinworldwide.com/volatility-index/'
        selector = "#highchart_simple_div"
        text += "BTC volatility / price index.\n\n"
    elif sys.argv[1] == 'defi_pulse':
        url = 'https://defipulse.com/'
        # selector = "div.defi-chart"
        selector = "table.defi-table"
    else:
        pass

    scr_lib.take_scr(url, 'scr.png', selector)
    text += 'Źródło : ' + url +'\n\n'
    w.add_entry(text,'scr.png', 1)



main()