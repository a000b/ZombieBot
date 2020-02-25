import requests, json, datetime, os
import wypok_bot_lib

def read_file(filename):
    with open(filename, "r", encoding='utf-8') as f:
        d = json.load(f)
    return d

def search_yt_latest_vid(searchtext, dn):
    global API_KEY
    fpath = str(os.getcwd() + '/myfiles/' + "client_secret.json")
    API_KEY = read_file(fpath)["key"]
    dzis = datetime.date.today()
    data_od = str(dzis - datetime.timedelta(int(dn)))
    data_do = str(dzis)
    
    search_url = f"https://www.googleapis.com/youtube/v3/search?" \
                 + f"part=snippet&maxResults=5&order=viewCount&publishedAfter" \
                 + f"={data_od}T00%3A00%3A00Z&publishedBefore={data_do}T00%3A00%3A00Z&q={searchtext}" \
                 + f"&type=video&fields=items(id(channelId%2CvideoId)%2Csnippet(publishedAt%2Ctitle))&key={API_KEY}"
    try:
        r = requests.get(search_url)
        content = r.json()['items']
    except:
        print(r.status_code)
        content = 'err'

    return content

def get_stats(videoid):
    url =  f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={videoid}" \
          + f"&fields=items%2Fstatistics&key={API_KEY}"
    try:
        r = requests.get(url)
        content = r.json()['items']
    except:
        print(r.status_code)
        content = 'err'

    return content
    
def create_entry(dane, stext):
    wstep = "The most viewed on YT during last 7 days.\nSearch = " + "'" + stext + "'\n\n"
    main_url = "https://www.youtube.com/watch?v="
    e = {}
    entry = wstep
    i = 0

    if dane != 'err':
        for i, d in enumerate(dane, 1):
            try:
                e['url'] =  main_url + d['id']['videoId']
                e['pos'] = "No. " + str(i)
                e['title'] = d["snippet"]["title"]
                e['publishedAt'] = str(d["snippet"]["publishedAt"]).replace("T", " ")[:19]
                
                st = get_stats(d['id']['videoId'])
                
                if st != 'err':
                    for s in st:
                        e['stats'] = "Views : " + str(s['statistics']['viewCount']) + " Likes : " + str(s['statistics']['likeCount'])
                else:
                    e['stats'] = ''
                entry += str(e['pos']) + "\n" + str(e['title']) + "\n" + "Published at : " + str(e['publishedAt']) + \
                     "\n" + str(e['stats']) + "\n" + str(e['url']) + "\n\n"
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
       img = ''
#       print(entry)
       w = wypok_bot_lib
       w.add_entry(entry, img)
main()
