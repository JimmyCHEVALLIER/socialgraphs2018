import json


with open('data.txt') as f:
    data = json.load(f)

#Category
resCategorie = {}
for celebrity in data.keys():
    category = data[celebrity]['category']
    resCategorie[category] = 0
for celebrity in data.keys():
    category = data[celebrity]['category']
    data[celebrity]['category'] = category.replace('\n','')
    if celebrity == "halsey":
        print('halsey ---------->',data[celebrity]['category'])
    #if category == "Governmentalbodies":
        #data[celebrity]['category']= "GovernmentalBodies"

    resCategorie[category] += 1

f = open('data.txt', 'r+')
f.truncate(0)  # need '0' when using r+
f.close()

with open('data.txt', 'w') as file:
    file.write(json.dumps(data))  # use `json.loads` to do the reverse


countCategory = 0
for key in resCategorie.keys():
    print(key,  resCategorie[key])
    countCategory += resCategorie[key]

#FriendList
count = 0
for celebrity in data.keys():
    if "friendList" in data[celebrity].keys():
        count+=1
    else:
        pass

print("\n number of categories", len(resCategorie), " | total count -> ",countCategory)
print("\n people with a friendList", count)
print("\n total ", len(data.keys()))

# number of nodes 484
# friend list blocked 13
# account blocked

#test 1 => 123 categorie DK
#test 2 => 220 categorie EN not found 66
#test 3 => 126 categorie not found 77

