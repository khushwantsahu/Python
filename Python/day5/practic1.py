#Word frequency counter
'''
para = "I like pizza and I like burgers and I like pasta."
word = para.split() #split the paragraph return list of words

word_dict = {}

for w in word:
    if w in word_dict:
       
        word_dict[w] += 1
    else:
        word_dict[w] = 1
print(word_dict)
'''
def main():
    para = get_text("Enter sentance with repeated words := ")
    word = para.split() #split the paragraph return list of words

    word_dict = {}

    word_counter(word,word_dict)

    print(word_dict)

def get_text(prompt):
   return str(input(prompt))

def word_counter(word,dict):
    for w in word:
        if w in dict:
            dict[w] += 1
        else:
            dict[w] = 1  

main()  