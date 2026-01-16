list = [1,2,3,4,5,6,7,8,9]
print(list[-3])
print(list[4:])     #slice the list from index 0 to 4 and return new list
print(list[-4:])    #slice the list from index end to -4 and return new list
list += [10,11,12,13]    #add new elements to the list
print(list)

list[5] = 55    #change the value of index 5
print(list)

list[5:7]= [34,45] #change the value of index 5 and 6

print(list)

list[:] = []   #clear the list
print(list)

list = [1,2,3,4]
a  = [5,6,7,8]
b = [list+a] # concatenate two lists
print(b)
b = [list,a] # create a list of two lists
print(b)
print(len(b))  #length of the list
print(4**2)


list.reverse()  #reverse the list
print(list)

list.append(5)  #add element to the end of the list
print(list)

print(list.count(4))  #count the number of occurrences of an element in the list

list.copy()   #create a copy of the list
print(list)

print(list.index(3))  #return the index of the first occurrence of an element in the list

print(list.pop())   #remove and return the last element of the list

list.extend([6,7,8])
print(list)  #add elements of another list to the end of the list

print(list[4:])
list.sort()  #sort the list
print(list)

#print(list.search(3))  #search for an element in the list and return its index

list.insert(2,10)  #insert an element at a specific index
print(list)
'''
time complexity
Operation	                    Average Complexity	Notes
Index access (lst[i])	        O(1)	            Direct memory access
Append (append)	                O(1)                amortized	Occasional resize
Insert/remove at end (pop())	O(1)	            Last element only
Insert/remove at start/middle	O(n)	            Shift elements
Slice creation (lst[a:b])	    O(k)	            k = slice length
Search (x in lst)	            O(n)	            Linear scan
Sort (sort())	                O(n log n)          Timsort algorithm
'''