from requests_html import HTMLSession

def get_info(period):
    
    if period == 'monthly':
        url = 'https://www.theice.com/products/72035464/Bakkt-Bitcoin-USD-Monthly-Futures-Contract/data?marketId=6137541'
    elif period == 'daily':
         url = 'https://www.theice.com/products/72035483/Bakkt-Bitcoin-USD-Daily-Futures-Contract/data'
         
    l = {}
    session = HTMLSession()
    try:
        r = session.get(url)
        r.html.render()

        data = [element.text for element in r.html.find('td')]
        data[2] = data[2].replace("\n", " ")
        data[5] = url
    except:
        data ='err'
    return(data)


