import asyncio
from pyppeteer import launch

async def get_img(*args):
    print(args[0][2])
    browser = await launch()
    page = await browser.newPage()
    await page.goto(args[0][0])
    element = await page.querySelector(args[0][2])
    await element.screenshot({'path': args[0][1]})
    await browser.close()
    
def take_scr(*args):
    z = asyncio.get_event_loop().run_until_complete(get_img(args))
    return z