x = 0
while x < 5 :
    print("hello")
    x += 1      #i=i+1   

print()

for i in [0,1,2]:
    print("hello")

print()
for i in range(5):
    print("hello")

print()
for _ in range(5):   # we cant use the i latter so we use underscore
    print("hello")
print()
print("hello\n"*3,end="")


students = ["raj","mohan","rohan","rahul"]
for name in students :
    print(name)

#len is use for length
for i in range(len(students)) :
    print(i,students[i])