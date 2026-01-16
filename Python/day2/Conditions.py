def main():
    x = int(input("enter number = "))
    y = int(input("enter number = "))
    compare(x,y)
    isequal1(x,y)
    isequal2(x,y)


def compare(a,b):
    if a > b :
        print(a,"is greater then",b)
    elif b > a:
        print(b,"is greater then",a)
    else :
        print(a,"is equal to ",b)

def isequal1(a,b):
    if a > b or a < b :
        print(a,b,"is not equal")
    else:
        print(a,"is equal to ",b)

def isequal2(a,b):
    if a != b :
        print(a,b,"is not equal")
    else:
        print(a,"is equal to ",b)
main()