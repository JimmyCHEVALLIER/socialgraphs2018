import twitter

# doc - > https://github.com/bear/python-twitter
# rate limitation https://developer.twitter.com/en/docs/basics/rate-limits.html

def getFriendsList(pApi,screen_name):
    users = pApi.GetFriends(screen_name=screen_name)
    return [u.screen_name for u in users]

api = twitter.Api(consumer_key='l4NaOuQuFJvlnIk7m5bPMmZMv',
                      consumer_secret='mBjW1X0MuArkDA1mgjIKkbzSecEJAHq8znCFxkHTMXxzjcNcwv',
                      access_token_key='1057560959202590720-OvqC7RRuJe4wRJwTXEH5CZmcSLq7E7',
                      access_token_secret='tUzMR9K8HKIhyuasSXPSpWWVmkkixk3V7wGt4ILOrDS6a')

# get user info
def getUserInfo(screenName):
    return api.GetUser(screen_name=screenName)

def getUsersInfo(screenNames):
    return api.LookupFriendship(screen_name=screenNames)


#print(getUserInfo("Drake"))

# get friend list
#print(getFriendsList("theroots"))

'''
res = getUsersInfo(['Xfinity', 'donaldglover', 'LateNightSeth', 'theaafca','Xfinity', 'donaldglover', 'LateNightSeth', 'theaafca','Xfinity', 'donaldglover', 'LateNightSeth', 'theaafca','Xfinity', 'donaldglover', 'LateNightSeth'])
print(res)
for i in res:
    print(i)
    print(type(i.name))

print(api.CheckRateLimit("/friends/list.json").remaining)
'''

#print(api.CheckRateLimit("/friends/list.json").remaining)
#print(getUserInfo('Earth_Pics')) # rank "418"
#print(getUserInfo('Lmao')) # rank "478"
#print(getUserInfo('girlposts')) # rank "334"


#for i in range(2):
#    getFriendsList("Drake")
#    print(api.CheckRateLimit("/friends/list.json"))


#print(api.CheckRateLimit("friends/ids"))
# get last posted tweets
#statuses = api.GetUserTimeline(screen_name="Drake")
#print([s.text for s in statuses])
