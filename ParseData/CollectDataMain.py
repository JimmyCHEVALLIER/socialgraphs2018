import json

from ParseData import TwitterData, SocialbladeData

link = "https://socialblade.com/twitter/top/500/followers"
res = SocialbladeData.getSocialBladeList(link)

count = 0
countCelebrity = 0

keys = list(res.keys())
CelebrityLists = [keys[i:i+100] for i in range(0, len(keys), 100)]

with open('data.txt') as f:
    data = json.load(f)

for Celebrity in list(data.keys()):
    if "friendList" in data[Celebrity]:
        count+=1

print("All fiends readed -------------->")

for Celebrity in list(data.keys()):
    with open('data.txt') as f:
        data = json.load(f)

    count=0
    for C in list(data.keys()):
        if "friendList" in data[C]:
            count += 1

    if "friendList" not in data[Celebrity]:
        api = TwitterData.twitter.Api(consumer_key='27SrdTVBoHpyAooSFK8gtzEe5',
                                      consumer_secret='LZZ6aETKpKRjIQKJ0cpsgEQGFNV9ES3r0lJo7rGF9GL7eK4NP3',
                                      access_token_key='393343462-ifPqT3spGAj2yKnMJNcZaFq4XoLTj5yZRdR1Crr3',
                                      access_token_secret='k2EfNUGqeEE4Jv6aJgyfXGcZxFwWvI2rAL0b4wxBcU46P')
        print(Celebrity)
        twitterFriends = TwitterData.getFriendsList(api, data[Celebrity]['screen_name'])

        if twitterFriends != []:
            data[Celebrity].update({"friendList": twitterFriends})
            count +=1
            f = open('data.txt', 'r+')
            f.truncate(0) # need '0' when using r+
            f.close()
            with open('data.txt', 'w') as file:
                file.write(json.dumps(data))  # use `json.loads` to do the reverse
            print(count, " / ", len(data.keys()), " computed")
        else:
            print("not computed, friendList returned []")


print("All data writed -------------->")

"""
        api = TwitterData.twitter.Api(consumer_key='l4NaOuQuFJvlnIk7m5bPMmZMv',
                                consumer_secret='mBjW1X0MuArkDA1mgjIKkbzSecEJAHq8znCFxkHTMXxzjcNcwv',
                                access_token_key='1057560959202590720-OvqC7RRuJe4wRJwTXEH5CZmcSLq7E7',
                                access_token_secret='tUzMR9K8HKIhyuasSXPSpWWVmkkixk3V7wGt4ILOrDS6a')
"""

#create a text file with one line containing one celebrity name
with open('data.txt') as f:
    data = json.load(f)

f= open("celebrityList.txt","w+")
for celebrity in data.keys():
    f.write(celebrity+"\n")
f.close()