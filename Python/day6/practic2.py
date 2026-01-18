#analyze 1. word count 2. most frequent word
from email.mime import text
import sys
def main():
    count_word(sys.argv[1])
    most_frequent_word(sys.argv[1])


def count_word(file):
    with open(file,"r") as f:
        text = f.read()
        word = text.split()
        print(f"total word count = {len(word)}")
       
def most_frequent_word(file):
    dict = {}
    with open(file,"r") as f:
        text = f.read()
        word = text.split()
        #most = max(word,key=word.count)
        for w in word:
            if w in dict:
                dict[w] += 1
            else:
                dict[w] = 1
        print(dict)
        most = 0
        word1 = ""
        for key in dict:
            if  most < dict[key]:
                most = dict[key]
                word1 = key

        print(f"most frequent word is =  {word1} : {most}")
        #print(f"most frequent word is = {most}")
main()