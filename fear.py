import wypok_bot_lib

def main():    
    w = wypok_bot_lib
    url = "https://alternative.me/crypto/fear-and-greed-index"
    img = url + ".png"
    text = "Fear Index\nŹródło : " + url + "\n\n"
    w.add_entry(text, img)

main()
