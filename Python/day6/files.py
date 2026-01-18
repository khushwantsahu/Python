'''
#read
file = open("demo.txt","r")
text = file.read()
print(text)
file.close()

#readline
file = open("demo.txt","r")
line = file.readline()
while line:
    print(line,end= "")
    line = file.readline()

file.close()

#readlines
file = open("demo.txt","r")
line = file.readlines()
print(line)
file.close()
'''
'''
#write
file = open("ex.txt","w")
file.write("hello this is me")
file.close()

#writelines
lines= "this is first \n this is second \n this is third \n"
file = open("ex.txt","w")
file.writelines(lines)
file.close()

#append
file = open("ex.txt","a")
file.write("\n this is fourth line ")
file.close()

#help(open)
with open("ex.txt","r") as file:
    print(file.read())

with open("ex.txt","w") as file:
    file.write("overwritten"  )

with open("ex.txt","r") as f:
    f.seek(5)
    print(f.tell())
    line = f.read(5)
    print(line)

'''

import os
from pathlib import Path

print(os.getcwd())  #get current working directory

f_path = os.path.join("day6","ex.txt")
print(f_path)

path = Path("day6") / "ex.txt"
print(path)

#exception
try:
    with open("ex.txt","r") as file:
        text = file.read()
        print(text) 
except FileNotFoundError:
    print("error")
except IOError:
    print("IO error")

#csv basic