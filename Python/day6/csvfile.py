#csv
import csv

data = [
    ["roll", "name", "age"],
    [1, "Alice", 20],
    [2, "Bob", 21]
]

with open("cust.csv","r")as f:
    read = csv.reader(f)
    for row in read:
        print(row)


with open("cust.csv","w",newline="")as f:
    write = csv.writer(f)
    write.writerow(data[0])

with open("cust.csv","a",newline="")as f:
    writer = csv.writer(f)
    writer.writerow([3, "Charlie", 22])