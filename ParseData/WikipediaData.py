import wikipedia
from bs4 import BeautifulSoup
import urllib
import re

# Get infobox in wikipedia for celebrities
# return a dictionary key/value
def getWikiArticle(strTitle):
    res = wikipedia.WikipediaPage(title=strTitle) # get HTML content of the article
    soup = BeautifulSoup(res.html(), 'html.parser')
    res = [ tag for tag in soup.find_all("table") if "class" in tag.attrs and "infobox" in tag.attrs['class']]
    parsedTable = [[urllib.parse.unquote(th.text), urllib.parse.unquote(td.get_text("|"))] for line in res[0].find_all('tr') for th in line('th') for td in line('td')]
    contentDict = {str(item[0]).replace("\xa0", " "): list(filter(lambda x: x not in ['(', ' (', '', ' ', ')', ' )', ', '], re.sub(r" ?\([^)]+\)", "", re.sub(r" ?\[[^)]+\]", "", item[1:][0])).replace(r"\(.*\)", "").replace("\n","").replace("\xa0", " ").split("|"))) for item in parsedTable}
    print(contentDict)

# get wiki article
#getWikiArticle('Kim_Kardashian') #Rihanna