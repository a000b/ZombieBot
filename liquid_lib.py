import blockstream_tools as btools
import logging
import wypok_bot_lib

target_path = ""
logging.basicConfig(filename=target_path + 'logs.log', level=logging.INFO,
                    format='%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s|%(message)s')

def get_asset_stats(asset: str = 'lbtc') -> str:

    if asset == 'lbtc':
        ticker = 'L-BTC'
        asset_id = '6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d'
    else:
        ticker = 'L-BTC'
        asset_id = '6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d'

    respons = btools.query_blockstream(btools.get_url(selector='asset', asset_id=asset_id))

    if respons:
        asset_info = f'Bitcoin jest wolny?, drogi? i nieanonimowy?. ' \
                     f'Nie jesteś już na niego skazany !!!!\n' \
                     f'Statystyki dla sieci Liquid - the future of Bitcoin :)\n\n' \
                     f'Ticker: {ticker}\nAsset_id :{asset_id}\n\n' \
                     f'Pegged in  : {respons["chain_stats"]["peg_in_count"]} txs - ' \
                     f'{respons["chain_stats"]["peg_in_amount"] / 10**8} BTC\n' \
                     f'Pegged out : {respons["chain_stats"]["peg_out_count"]} txs - ' \
                     f'{respons["chain_stats"]["peg_out_amount"]  / 10**8} BTC\n' \
                     f'Burned   : {respons["chain_stats"]["burn_count"]} txs - ' \
                     f'{respons["chain_stats"]["burned_amount"]  / 10**8} BTC\n\n' \
                     f'WTF is burned??? dunno...don\'t ask me.\n\n' \
                     f'https://blockstream.info/liquid/asset/6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d'

    return asset_info

def main():
    entry = get_asset_stats()
    if entry != 'err':
       entry = entry +"\n\n"
       img = ''
       print(entry)
       # w = wypok_bot_lib
       # w.add_entry(entry, img)

main()