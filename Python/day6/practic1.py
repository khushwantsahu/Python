#read a text file
import sys
def main():
    read_file(sys.argv[1])

def read_file(file):
    with open(file,"r") as f:
        text = f.read()
        print(text)

main()