import twitter
import os
import re

if not os.path.exists("Tweets"):
    os.makedirs("Tweets")

f = open("celebrityList.txt", "r")

for _ in range(249):
    f.readline()
for i in range(248):
    celebrity = f.readline().replace("\n", "")
    exists = os.path.isfile("Tweets/" + celebrity + ".txt")
    if not exists:
        CelebrityFile = open("Tweets/" + celebrity + ".txt", "w+")
        print(i ," collected ---->", celebrity)
        api = twitter.Api(consumer_key='27SrdTVBoHpyAooSFK8gtzEe5',
                                      consumer_secret='LZZ6aETKpKRjIQKJ0cpsgEQGFNV9ES3r0lJo7rGF9GL7eK4NP3',
                                      access_token_key='393343462-ifPqT3spGAj2yKnMJNcZaFq4XoLTj5yZRdR1Crr3',
                                      access_token_secret='k2EfNUGqeEE4Jv6aJgyfXGcZxFwWvI2rAL0b4wxBcU46P')
        statuses = api.GetUserTimeline(screen_name=celebrity, count=200)
        [CelebrityFile.write(s.text.replace("\n","") + "\n") for s in statuses]
        CelebrityFile.close()
    else:
        print(i , " already -> ", celebrity)

f.close()

# VineCreators S1dharthM
