import bakkt_lib

def save_stats(dane):
    with open('bakkt_stats.csv', 'a') as f:
        f.write(dane + '\n')
def main():
    b = bakkt_lib.get_info('monthly')
    vol = str(int(b[4]) + int(b[10]))
    if b != 'err':
        save_stats(b[2] + "," + vol)
    else:
        pass
main()
