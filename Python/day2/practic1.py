n = int(input("Enter number = "))

#square pattern
for _ in range(n):
    print("* "*n)


#triangle pattern
for i in range(n):
    for j in range(i+1):
        print("# ",end="")
    print()

print()


#reverse trinagle pattern
for i in range(n):
    for j in range(n-i-1):
        print("  ",end="")
    for j in range(i+1):
        print("# ",end="")
    print()

#half diamond pattern
for i in range(n):
    for j in range(i+1):
        print("# ",end="")
    print()
for i in range(n):
    for j in range(n-i):
        print("# ",end="")
    print()

#print()
#diamond pattern
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("# ",end="")
    print()
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(n-i):
        print("# ",end="")
    print()


#hollow square pattern
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print("# ",end="")
        else:
            print("  ",end="")
    print()

print()
#rhombus pattern
for i in range(n):
    for j in range(i):
        print(" ",end="")
    print("# " * n)

print()

#reverse right half pyramid
for i in range(n):
    for j in range(n-i):
        #print(j+1," ",end="")
        print("# ",end="")
    print()

print()

#reverse left half pyramid
for i in range(n):
    for j in range(i):
       #print("  ",end="")
        print(" ",end="") #for reverse pyramid
    for j in range(n-i):
        print("# ",end="")
    print()

print()




print()