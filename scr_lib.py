import asyncio
import time
from pyppeteer import launch
from pyppeteer.page import Page
import logging


target_path = ""
logging.basicConfig(filename=target_path + 'logs.log', level=logging.INFO,
                    format='%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s|%(message)s')


async def get_img(*args):
    try:
        browser = await launch(options = None)
        page: Page = await browser.newPage()
        await page.setViewport({'width': 2048, 'height': 1536});
        await page.goto(args[0][0], {'waitUntil': 'networkidle2'})
        time.sleep(5)
        element = await page.querySelector(args[0][2])
        await element.screenshot({'path': args[0][1]})
        await browser.close()
    except Exception as e:
        logging.error(e)


def take_scr(*args):
    z = asyncio.get_event_loop().run_until_complete(get_img(args))
    return z
