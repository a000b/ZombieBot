import wypok_bot_lib
import bakkt_lib



def new_entry(*args):
    data = args[0][0]
    mesg = f"BAKKT stats:\n\n"
    for i in range(0, len(data), 6):
        z = data[i:i + 6]
        mesg += (
        f"Kontrakt : {z[0]}\n"
        f"Wolumen : {z[4]} BTC\n"
        f"Czas : {z[2]}\n"
        f"Cena : {z[1]}\n"
        f"Zmiana : {z[3]}%\n\n"
        )
        
    mesg += (
        f"Źródło : {args[0][1]}\n\n"
        )

    return(mesg)

def main():
    b = bakkt_lib.get_info('monthly')
    if b != 'err':
#         print(new_entry(b))
        img = ''
        wypok_bot_lib.add_entry((new_entry(b), img))
    else:
        print('err')

main()

