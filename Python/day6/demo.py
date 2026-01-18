'''str1 = "hello world whats up"
str2 = 'nothing just chilling'
str3 = '"oh , ohk go fun"'
str4 = """ oohk , nuce "alright" """

print(str1)
print(str2)
print(str3)
print(str4)
'''
#indexing and slicing
ch = "hello_world"
print(ch[0])
print(ch[1])
print(ch[-1])
print(ch[3:])
print(ch[:3])
print(ch[0:10:2]) #[start:stop:step]

print(len(ch)) #length of string

ch1 = "hiiiiii"
print(ch+" "+ch1) #concatenate two strings

x = "hello give me"
y = 5
z = "rupee"
print(x+" "+str(y)+" "+z)

#print(ch.__dir__()) #list of all methods available for string

#help(ch.replace)

first,second = "rahul","aman"

both = first+" or "+second
print(both)
print("\t")

print(both.replace(" or "," and "))
print("\t")

print(both.split())
print(" & ".join(both.split(" or ")))

print(both.find("aman"))

print(both.upper())

print(both.center(50,"-"))

print(dir(str))

print(both.__sizeof__())  #size of the string in bytes

# formating

print("hello"+ " "+"world")

print("{} {} a {} text ".format("this","is","formatted"))

val = 43.8344893
print("{x:f} {x:.2f} {y:f} {y:g} ".format(x = val,y = val +834))

print("{0} hello {1} is {2} ".format(6,8,8*7))


print(both.count("l"))
print(both.capitalize())
print(both.upper())
print(both.lower())
print(both.isupper())
print(both.islower())
print(both.title())
print(both.isalpha())
print(both.split())
print(both.strip())
print(both.startswith("r"))
print(both.endswith("n"))
print(both.find("aman"))
print(both.isdigit())
print(both.index("aman"))


#csv
import csv
with open("cust.csv","r")as f:
    read = csv.reader(f)
    for row in read:
        print(row)