import wypok_bot_lib
import bakkt_lib
import logging


target_path = ""
logging.basicConfig(filename=target_path + 'logs.log', level=logging.INFO,
                    format='%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s|%(message)s')


def new_entry(*args):
    data = args[0][0]
    mesg = f"BAKKT stats:\n\n"
    status = 'ok'
    for i in range(0, len(data), 6):
        z = data[i:i + 6]
        try:
            vol = int(z[4])
            logging.info(f"Konwersja !{z[4]}!, udana")
        except Exception as e:
            vol = 0
            logging.error(f"Konwersja {z[4]}, nieudana, e")
        try:
            if vol > 0:
                mesg += (f"Kontrakt : {z[0]}\n" 
                         f"Wolumen : {z[4]} BTC\n"
                         f"Czas : {z[2]}\n"
                         f"Cena : {z[1]}\n"
                         f"Zmiana : {z[3]}%\n\n")
            else:
                status = 'err'
                logging.warning(f"Kontrakt : {z[0]}: Brak danych")
        except Exception as e:
            logging.error(f"{e}")

    mesg += (f"Źródło : {args[0][1]}\n\n")
    return(mesg, status)

def main():
    b = bakkt_lib.get_info('monthly')
    if b != 'err':
        m = new_entry(b)
        if m[1] != 'err':
            img = ''
            wypok_bot_lib.add_entry(m[0], img)
    else:
        pass

main()
