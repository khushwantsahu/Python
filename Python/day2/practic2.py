#using function
import random
random_num = random.randint(1,100)      #global variable

def main():
    print("we are playing the number guessing game \nlet's go.........:")
    if guess_game():
        print("you win! boyaah you guess the right number.")

def guess_game():
    while True:
        guess_num = int(input("Enter any number = "))    #local variable
        if guess_num == random_num :
            return True
        elif guess_num > random_num :
            print("your number is higher then random number")
        else:
            print("your number is lower then random number")

main()