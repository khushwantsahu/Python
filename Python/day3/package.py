import cowsay    #package  module
import sys
def main():
    if len(sys.argv) < 2:
        sys.exit("not enough arguments")
    else:
        great_name()
    
def great_name():
    for arg in sys.argv[1:]:
        great(arg)

def great(name):
    print(cowsay.trex("hello, "+name))
main()