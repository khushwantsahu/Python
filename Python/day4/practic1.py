#Student marks processing
import sys
def main():
    marks = []
    n = get_int("Enter number of subjects : ")

    total_mark = n*100
    total_obt_mark = Enter_val(marks,n)

    percentage = (total_obt_mark/(n*100))*100

    print(f"marks = {marks}")

    if ispass(marks) :
        print(f"you are pass {percentage} %")
    else:
        print(f"fail {percentage}")
   
def get_int(prompt):
    try :
        val = int(input(prompt))
        return val
    except ValueError:
        sys.exit("Enter valid input")

def Enter_val(list_mark,n):
    total_obt_marks = 0
    for i in range(n):
        temp = get_int(f"Enter {i+1} subject number = ")
        list_mark.insert(i,temp)
        total_obt_marks += temp
    return total_obt_marks

def ispass(marks):
    count = 0
    for mark in marks:
        if mark >= 33:
            count += 1
    return count > 2



main()