student = {
    "rohan":"mumbai",
    "anil":"delhi",
    "raj":"delhi",
    "monti":"banglore"
}

print(student["rohan"])
print(student["anil"])
print(student["raj"])
print()
for std in  student:
    print(std,student[std],sep=" : ")

print()

student1 = [
    {"name":"rohan","class":"10th","live":"mumbai"},
    {"name":"rahul","class":"11th","live":None}
]

for std in student1:
    print(std["name"],std["class"],std["live"])