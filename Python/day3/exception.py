#1
try :
    x = int(input("Enter x = "))
    print("x =",x)
except ValueError:
    print("invalid value")

#2
try :
    x = int(input("enter x = "))
except ValueError:
    print("invalid value")
else :
    print("x =",x)

def main():
    x = get_num_int("Enter x = ")
    print("x =",x)

def get_num_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            pass

main()