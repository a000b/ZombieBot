import bakkt_lib

def save_stats(dane):
    with open('bakkt_stats.csv', 'a') as f:
        f.write(dane + '\n')

b = bakkt_lib.get_info('monthly')
if b != 'err':
    save_stats(b[2] + "," + b[4])
else:
    pass