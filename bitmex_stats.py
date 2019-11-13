import requests as r
import locale
import wypok_bot_lib as w

locale.setlocale(locale.LC_ALL, "pl_PL.UTF-8")


def get_stats(*args):
    url = "https://www.bitmex.com/api/v1/" + args[0]
    try:
        response = r.get(url)
    except:
        entry = 'err_'
    else:
        if response.status_code == 200:
            content = response.json()
            for entry_ in content:
                if entry_ ['rootSymbol'] == "XBT":
                    t24 = locale.format_string(f="%.0f", val=entry_["turnover24h"], grouping=True)
                    t365 = locale.format_string(f="%.0f", val=entry_["turnover365d"], grouping=True)
                    t = locale.format_string(f="%.0f", val=entry_["turnover"], grouping=True)
                    entry = f'{"Turnover":>13} : {t} USD\n' \
                            f'{"Turnover365":>13} : {t365} USD\n' \
                            f'{"Turnover24":>13} : {t24} USD\n\n'
        else:
            entry = 'err'
    return entry


def main():
    urls = ["stats/historyUSD", "stats"]
    e = get_stats(urls[0])
    entry = "Bitmex statistics:\n\n"
    end_ = "\n\nŻródło: https://www.bitmex.com/"
    if e != 'err':
        entry  += e
        entry += end_
        img = ''
        print(entry)
        # w.add_entry(entry, img)
    else:
        print("err")


main()