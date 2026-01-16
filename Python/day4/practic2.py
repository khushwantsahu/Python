def main():
    lists = [1,2,23,4,5,4,4,4,5,6]
    list2 = []
    print(list)
    
    for num in lists:
        if num not in list2:
            list2.append(num)

    print(list2)
main()