import requests, json, datetime, wypok_bot_lib

def read_file(filename):
    with open(filename, "r", encoding='utf-8') as f:
        d = json.load(f)
    return d

def search_yt_latest_vid(searchtext, dn):
    API_KEY = read_file("client_secret.json")["key"]
    dzis = datetime.date.today()
    data_od = str(dzis - datetime.timedelta(int(dn)))
    data_do = str(dzis)
    
    search_url = f"https://www.googleapis.com/youtube/v3/search?" \
                 + f"part=snippet&maxResults=5&order=viewCount&publishedAfter" \
                 + f"={data_od}T00%3A00%3A00Z&publishedBefore={data_do}T00%3A00%3A00Z&q={searchtext}" \
                 + f"&fields=items(id(channelId%2CvideoId)%2Csnippet(publishedAt%2Ctitle))&key={API_KEY}"
    try:
        r = requests.get(search_url)
        content = r.json()['items']
    except:
        print(r.status_code)
        content = 'err'

    return content

def create_entry(dane, stext):
    wstep = "The most viewed on YT; last 7 days; search = " + "'" + stext + "'\n\n"
    main_url = "https://www.youtube.com/watch?v="
    e = {}
    entry = wstep

    if dane != 'err':
        for i, d in enumerate(dane, 1):
            try:
                e['url'] =  main_url + d['id']['videoId']
                e['title'] = d["snippet"]["title"]
                e['publishedAt'] = str(d["snippet"]["publishedAt"]).replace("T", " ")[:19]
                entry += str(e['title']) + "\n" + "Published at : " + str(e['publishedAt']) + \
                     "\n" + str(e['url']) + "\n\n"
            except KeyError:
                pass
    else:
        entry = 'err'
    return entry

def main():
    st = 'cryptocurrency'
    yt = create_entry(search_yt_latest_vid(st, 7), st)
    if yt != 'err':
       entry = yt +"\n\n"
       w = wypok_bot_lib
       w.add_entry(entry)
       
main()