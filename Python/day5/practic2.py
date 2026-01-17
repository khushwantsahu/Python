
def main():
    student_dict = {}

    user_choice(student_dict)
    


def user_choice(s_dict):
    while True:
        print("1. Add Student \n2. update student \n3. delete student \n4. show all students database \n5. exit")
        ans = s_input("select number : ")
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
                print()
            case "5":
                exit()
                print()
            case _:
                exit("incalid input")
                print()
        print("\n")

def s_input(prompt):
    return str(input(prompt))

#add student function
def add_student(s_dict):
    if s_dict =={}:
        roll_num = 101
    else:
        roll_num = max(s_dict.keys(), default=0) + 1
    
    if roll_num in s_dict:
        exit("roll number exist ")
    else :
        name = s_input("Enter name - ")
        s_class = s_input("Enter class - ")
        age = input("Enter age - ")
        s_dict[roll_num] = {"name":name,"class":s_class,"age":age}
        print(f"{roll_num} {s_dict[roll_num]} is added ")

#bug in update function
def update_student(s_dict):
    roll_unum = s_input("Enter roll number to update - ")
    print(s_dict)
    if roll_unum not in s_dict:
        return print("roll number not found ")
    
    name = input("Enter name - ")
    s_class = input("Enter class - ")
    age = input("Enter age - ")
    s_dict[roll_unum] = {"name":name,"class":s_class,"age":age}
    print(s_dict[roll_unum]," updated ")
    
#delete function
def delete_student(s_dict):
    roll_dnum = s_input("Enter roll number to delete - ")
    if roll_dnum in s_dict:
        s_dict.pop(roll_dnum,None)
        print(roll_dnum,"student detail is deleted ")
    else:
        print("roll number not found ")

#show all students
def show_students(s_dict):
    if s_dict == {}:
        return print("no data found")
    
    for key,value in s_dict.items():
        print(f"roll number : {key} \n name : {value["name"]} , class : {value["class"]} age {value["age"]} \n")
main()