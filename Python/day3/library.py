#learn about libraries
import random
import statistics

def main():
    #uses random libraries method
    coin = toss()
    print(coin,"wins")
    print()
    x = get_num("Enter smallest integer = ")
    y = get_num("Enter y (y greater then x) = ")
    guess = guess_num_int(x,y)
    print(f"random number between {x} and {y} = {guess}")

    #uses statistics library
    print("mean of list value = ",statistics.mean([80,36,58,83,78]))
    print("mode of list = ",statistics.mode(["red","blue","red","red","pink","black","grean"]))


def  get_num(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            pass

def toss():
    return random.choice(["Head","Tail"])

def guess_num_int(a,b):
    return random.randint(a,b)



main();