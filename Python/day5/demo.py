#tuple
t = (10,59)
print(t)

#XXXXXXXXXXXX
#t[0]=64
#print(t)
#XXXXXXXXXXXX

#Immutable Data Storage , Storing Heterogeneous Data
t1 = ("hello",1,2,4,"world ","rahul")
print(t1)

#Dictionary Keys:Tuples are hashable and can be used as dictionary keys, unlike lists.
t3 = {
    ("india","delhi"): "parliament",
    ("uae","dubai"):"burj khalifa"
}
print(t3[("uae","dubai")])


#set | & - operations
#set1 = set([23 ,34,54,34,23])
a = [23 ,34,54,34,23]
set1  = set(a)
print(set1)  #duplicates are removed automatically

set1.add(45)  #add element to the set
print(set1)

set1.remove(23)
print(set1)

set2 = set([5,6,3,4,23,45,54])
print(set2)
print(set1 | set2) #union of two sets

print()
print(set1 & set2) #intersection of two sets
print()
print(set1 - set2)

#dectionary

dict = {
    "name":"annu",
    "class":"10th",
    "age":16
}

print(dict["class"])

dict["age"] = 15

print(dict["age"])
print(dict)

dict["school"] = "any school"  #add new key value pair
print(dict)

dict1 = [
    {"name":"annu","class":"11th"},
    {"name":"khushi","class":"9th"}
]

print(dict1)
print(dict1[0]["name"])

#iteration
for  key in dict:
    print(f"{key} : {dict[key]}")

print()

for i in dict1:
    for key in i:
        print(f"{key} - {i[key]} ")

print()

for key in dict:
    print(key)

print()

for value in dict.values():
    print(value)

print()

for key , value in dict.items():
    print(key,value)

dict2 = {
    "s1":{"name":"rahul","marks":80},
    "s2":{"name":"khusi","marks":78}
}

for key in dict2:
    print(f"{key} : {dict2[key]}")

print(dict2["s1"]["name"])

dict3 = {}
dict3["name"] = "rahul"

print(dict3)