import wypok_bot_lib as w
import scr_lib

def main():
    url = 'https://coinmarketcap.com/charts/'
    img = "scr.png"
    selector = "#dominance-percentage"
    z = scr_lib.take_scr(url, img, selector)
    text = 'Źródło : ' + url +'\n\n'
    # w.add_entry(text, img, 1)


main()