import wypok_bot_lib
import bakkt_lib

def new_entry(data):
    mesg1 = (
        f"BAKKT stats:\n\n"
        f"Kontrakt : {data[0]}\n"
        f"Wolumen : {data[4]} BTC\n"
        f"Czas : {data[2]}\n"
        f"Cena : {data[1]}\n"
        f"Zmiana : {data[3]}%\n\n"
        )
    if len(data) > 6:
        mesg2 = (
            f"Kontrakt : {data[6]}\n"
            f"Wolumen : {data[10]} BTC\n"
            f"Czas : {data[8]}\n"
            f"Cena : {data[7]}\n"
            f"Zmiana : {data[9]}%\n\n"
            )
    else:
        mesg2 = ''
        
    mesg3 = (
        f"Źródło : {data[5]}\n\n"
        )
    mesg = mesg1 + mesg2 + mesg3
    
    return(mesg)

def main():
    b = bakkt_lib.get_info('monthly')
    if b != 'err':
        wypok_bot_lib.add_entry((new_entry(b)))
    else:
        print('err')

main()

