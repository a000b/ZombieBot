import asyncio
from pyppeteer import launch
# import os
import wypok_bot_lib

async def get_img(url, output_file):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    element = await page.querySelector("#dominance-percentage-graph")
    await element.screenshot({'path': output_file})
    await browser.close()


def main():
    url = 'https://coinmarketcap.com/charts/'
    img = "btc_d.png"
#     z = asyncio.get_event_loop().run_until_complete(get_img(url, img))
    w = wypok_bot_lib
    text = 'Źródło : ' + url +'\n\n'
    w.add_entry(text, img, 1)


main()