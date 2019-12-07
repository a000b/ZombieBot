import asyncio
import time
from pyppeteer import launch
from pyppeteer.page import Page
import logging


target_path = ""

logging.basicConfig(filename=target_path + 'logs.log', level=logging.INFO,
                    format='%(asctime)s|%(levelname)s|%(filename)s|%(funcName)s|%(message)s')


async def get_img(*args):
    browser = await launch(options=None)
    page: Page = await browser.newPage()

    try:
        await page.setViewport({'width': 2048, 'height': 1536});
        # await page.goto(args[0][0], {'waitUntil' : 'networkidle2'})
        await page.goto(args[0][0], {'timeout': '100000'})
        time.sleep(5)
    except Exception as e:
        logging.error(f"File not saved for {args[0][2]} - {e}")
        status = False
    else:
        element = await page.querySelector(args[0][2])
        await element.screenshot({'path': args[0][1]})
        status = True
        logging.info(f"File saved for {args[0][2]} ")
    finally:
        await page.close()
        await browser.close()
    return status

def take_scr(*args):
    z = asyncio.get_event_loop().run_until_complete(get_img(args))
    return z
