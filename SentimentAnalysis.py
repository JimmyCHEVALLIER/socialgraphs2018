import glob, os
import json

documents = {}

with open('./Data/data.txt') as f:
    data = json.load(f)

#Create one big str per category
os.chdir("./Data/Tweets/")
for celebrity in glob.glob("*.txt"):
    f = open("/Users/jimmy/Desktop/Social_Graph_Git/Data/Tweets/"+celebrity,"r")
    celebrity = celebrity.replace(".txt","")
    str = f.read()
    if str != "":
        if data[celebrity]['category'] in documents.keys():
            documents[data[celebrity]['category']] += str + " "
        else:
            documents[data[celebrity]['category']] = ""

        if data[celebrity]['category'] == 'PoliticalParties':
            print("=== ",celebrity)



