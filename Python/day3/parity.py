def main():    
    x = int(input("enter a number = "))
    if is_even(x) :
        print(x,"is even number")
    else:
        print(x,"is odd number")


def is_even(x):
    if x % 2 == 0 :
        return True
    else:
        return False

    #return True if x % 2 == 0 else False
    #return n % 2 == 0

main()