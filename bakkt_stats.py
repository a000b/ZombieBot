import bakkt_lib

def save_stats(dane):
    with open('bakkt_stats.csv', 'a') as f:
        f.write(dane + '\n')
        
def main():
    vol = 0
    b = bakkt_lib.get_info('monthly')[0]
    for i in range(0, len(b), 6):
        z = b[i:i + 6]
        vol += int(z[4])
        
    if b != 'err':
        save_stats(b[2] + "," + str(vol))
    else:
        pass
main()
