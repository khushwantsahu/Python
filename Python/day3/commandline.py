import sys
def  main():
    #print("hello, "+sys.argv[1])
    cmd_line_arg()

def cmd_line_arg():
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:   #list slice
            print("hello, "+arg) 
    elif len(sys.argv) < 2:
        sys.exit("not enough argument")


main()