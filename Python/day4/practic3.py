def main():
    n = get_int("Enter the size of list = ")

    list1 = []
    insert(list1,n)

    list2 = find_top_most(list1)
    print(f"top three value  = {list2}")

def get_int(prompt):
    try:
        val = int(input(prompt))
        return val
    except ValueError:
        exit("Enter valid number")

def insert(lists,n):
    
    for _ in range(n):
        lists.append(get_int("Enter number = "))

def find_top_most(lists):
    first  = 0
    second = 0
    third = 0
    for num in lists:
        if num > first:
            first = num
            second = first
            third = second
        elif num > second:
            second = num
            third = second
        elif num > third :
            third = num
    
    return [first,second,third]

main()