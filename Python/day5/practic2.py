
def main():
    student_dict = {}
    user_choice(student_dict)
    

def user_choice(s_dict):
    while True:
        print("\n1. Add Student \n2. update student \n3. delete student \n4. show all students database \n5. exit\n")
        ans = s_input("select number : ")
        print()
        match ans:
            case "1":
                add_student(s_dict)
                print()
            case "2":
                update_student(s_dict)
                print()
            case "3":
                delete_student(s_dict)
                print()
            case "4":
                show_students(s_dict)
            case "5":
                exit()
            case _:
                exit("--------------invalid input--------------")

def s_input(prompt):
    return str(input(prompt))

#add  student details  
def add_student(s_dict):
    if s_dict =={}:
        roll_num = 101
    else:
        roll_num = max(s_dict.keys(), default=0) + 1
    
    if roll_num in s_dict:
        exit("-------------roll number exist----------------")
    else :
        name = s_input("Student name : ")
        s_class = s_input("Student class : ")
        age = int(s_input("Student age : "))
        s_dict[roll_num] = {"name":name,"class":s_class,"age":age}
        print(f"\nroll number : {roll_num} {s_dict[roll_num] } is Added " ,end="")

#update student details  
def update_student(s_dict):
    try:
        roll_unum = int(s_input("Enter roll number to update : "))
    except ValueError:
        return print("---------invalid roll number----------- ")
    
    if roll_unum not in s_dict:
        return print("------------roll number not found----------------")
    
    name = s_input("Student name : ")
    s_class = s_input("Student class : ")
    age = int(s_input("Student age : "))
    s_dict[roll_unum] = {"name":name,"class":s_class,"age":age}
    print(f"roll number : {roll_unum} {s_dict[roll_unum] } Updated ")
    
#delete student details  
def delete_student(s_dict):
    try:
        roll_dnum = int(s_input("Enter roll number to Delete : "))
    except ValueError:
        return print("---------invalid roll number----------- ")
    
    if roll_dnum in s_dict:
        s_dict.pop(roll_dnum,None)
        print(f"roll number : {roll_dnum} student detail is Deleted ")
    else:
        print("------------roll number not found----------------")

#show all students
def show_students(s_dict):
    if s_dict == {}:
        return print("no data found")
    
    for key,value in s_dict.items():
        print(f"roll number : {key} \n name : {value["name"]} , class : {value["class"]}, age : {value["age"]}")
main()