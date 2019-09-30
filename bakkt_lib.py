from requests_html import HTMLSession

def get_info(period):
    
    if period == 'monthly':
        url = 'https://www.theice.com/products/72035464/Bakkt-Bitcoin-USD-Monthly-Futures-Contract/data'
    elif period == 'daily':
         url = 'https://www.theice.com/products/72035483/Bakkt-Bitcoin-USD-Daily-Futures-Contract/data'
         
    l = {}
    session = HTMLSession()
    try:
        r = session.get(url)
        r.html.render()
        data = [element.text for element in r.html.find('td')]
        data[2] = data[2].replace("\n", " ")
        if len(data) > 6:
            data[8] = data[8].replace("\n", " ")
    except:
        data ='err'
    return(data, url)



