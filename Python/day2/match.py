
name = input("Enter color = ")

match name:
    case "red"|"grean"|"blue" :
        print("this are RGB color")
    case "pink" :
        print("it's an pink color")
    case _:
        print("restart")