import wypok_bot_lib
import scr_lib

def main():
    url = 'https://coinmarketcap.com/charts/'
    img = "btc_d.png"
    selector = "#dominance-percentage-graph"
    z = scr_lib.take_scr(url, img, selector)
    w = wypok_bot_lib
    text = 'Źródło : ' + url +'\n\n'
    w.add_entry(text, img, 1)


main()