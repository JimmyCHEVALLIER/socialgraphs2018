from langdetect import detect
import glob, os
import goslate

gs = goslate.Goslate()

accountWithoutTweets = 0
accountWithTweets = 0
languagesForTweets = {}

os.chdir("./Data/Tweets/")
for file in glob.glob("*.txt"):
    f = open("/Users/jimmy/Desktop/Social_Graph_Git/Data/Tweets/"+file,"r")
    str = f.read()
    if str != "":
        accountWithTweets += 1
        lang = detect(str)
        if lang not in languagesForTweets.keys():
            languagesForTweets[lang] = 0

        languagesForTweets[lang] += 1

        if lang == 'es':
            """
            f.close()
            str = gs.translate(str,'en')
            f = open("/Users/jimmy/Desktop/Social_Graph_Git/Data/Tweets/" + file, "w")
            print(file)
            print("-> translating --------->")
            f.write(str)
            print("done")
            f.close()
            """

            print(file)

    else:
        accountWithoutTweets +=1
        print("------_>",file)

for key in languagesForTweets:
    print(key, languagesForTweets[key])

print("without tweets ->", accountWithoutTweets)
print("with tweets ->",accountWithTweets)