import requests
import logging
import datetime
from blockstream_info import blockstream_tools as btools


target_path = ''
logging.basicConfig(filename=target_path + 'logs.log', level=logging.INFO,
                    format='%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s|%(message)s')

next_halving_height = 630000

def getlastblock():
    lastblock_height = "err"
    try:
        response = requests.get('https://blockstream.info/api/blocks/tip/height')
    except Exception as e:
        logging.error(e)
    else:
        if response.status_code == 200:
            content = response.json()
            try:
                lastblock_height = int(content)
            except Exception as e:
                logging.error(e)
                logging.error(content)
    return lastblock_height

def calculate_remaining_blocks(last_block):
    return int(next_halving_height - last_block)

def calculate_remaining_days(remained_blocks):
    return int(remained_blocks // 144)

def calculate_remaining_minutes(remained_blocks):
    return int((remained_blocks - (remained_blocks // 144 * 144)) * 10)

def calculate_halving_date(days_to_halving, minutes):
    return (datetime.datetime.now() + datetime.timedelta(days=days_to_halving, minutes=minutes)).strftime('%A, %d %B %Y, godz. %H:%M UTC')

def get_halving_info():
    halving_info = {}
    block = getlastblock()
    # block = 630000
    if block != "err":
        blocks_left = calculate_remaining_blocks(block)
        if int(blocks_left) > 0:
            days_left = calculate_remaining_days(blocks_left)
            minutes_left = calculate_remaining_minutes(blocks_left)
            halving_date = calculate_halving_date(days_left, minutes_left)
            halving_info["hinfo"] =  f"Do halvingu pozostało {blocks_left} bloków, {days_left} dni i {minutes_left} minut.\n" \
                                     f"Przewidywana data: {halving_date}"
        # else:
        #     halving_info["hinfo"] =  f"{'HALVING'.center(20, '!')}"
        else:
            _block = '000000000000000000024bead8df69990852c202db0e0097c1a12ea637d7e96d'

            block_timestamp = btools.query_blockstream(btools.get_url
                                                       (selector='block', block_hash=_block))['timestamp']
            halving_time = datetime.datetime.fromtimestamp(block_timestamp)
            time_from_halving = btools.time_diff(halving_time, datetime.datetime.now() )


            halving_info["hinfo"] =  f"Od halvingu upłynęło {abs(blocks_left)} bloków;\n" \
                                     f" {time_from_halving}"
    else:
        halving_info = {"hinfo": f"err"}

    return halving_info

