import requests
from bs4 import BeautifulSoup

# Get and parse specific list in socialblade
# return an iterator (zip)
def getSocialBladeList(link):
    res = {}
    f = requests.get(link)
    soup = BeautifulSoup(str(f.text), 'html.parser')
    parsedTable = list(filter(lambda x: x != '\n',[ line for line in soup.find("div", {"class": "content-module-wide"})]))
    parsedTable = [line.text for line in parsedTable]
    for celebrity in zip(*[iter(parsedTable)]*6):
        res[celebrity[2]] = {"rank" : celebrity[0], "tweetsCount": celebrity[3], "followersCount": celebrity[4], "friendCount": celebrity[5]}
    return res

#link = "https://socialblade.com/twitter/top/500/followers"
#res = getSocialBladeList(link)
#print(res)

