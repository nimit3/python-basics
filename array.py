no = [1, 2, 3, 4, 5]
# # [from:to] this sytanx will work here tooo
# print(no[0:3])
# print(no[2:])  # this will print everyting from 2nd index

# 2d arrays  matrix
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# # we can store mutliple types of elements in list. same like JS
# arr=['fwqfq',12,122,1331,'fwqfwqf', False]
# for i in arr:
#     print(type(i))

# # how to give some range of numbers to list directly
# nos = list(range(1,9))
# print(nos)


# # prinintg 2d array
# for row in matrix:
#     for item in row:
#         print(item)

# # we can use in operator in array too
# print(4 in no)  # will return true
# no2 = no
# no.insert(2, 22)
# print(no2)

# # how to remove duplicate items from arr
# org = [1, 22, 22, 33, 444, 444, 33, 6, 8, 9]
# dup = []
# for i in org:
#     if(i not in dup):
#         dup.append(i)
# print(dup)

# list methods:
# 1) insert at last - append
# arr = [1,2,3]
# arr.append(4) #it only takes 1 argument. can't pass mutliple args
# print(arr)

# # 2) extend - adding multiple eleemnts at the end
# arr.extend([55,66, 444])
# print(arr)

# # 3) insert - adding element at specific location
# arr.insert(1,11)
# print(arr)
# # ----------------------removing elements from list common methods
# # # 1) clear - removed everything from list
# # print(arr.clear()) #will print None

# # removing last element only - pop
# arr.pop()
# print(arr)
# # however we can even use pop(index_no_element) that we want to remove. NOT available in JS
# arr.pop(0) #will remove 0th index element
# print(arr)

# # remove - will remove some specific element that you will pass in args.
# arr2=list(range(11,19))
# arr2.remove(11)
# print(arr2)

# -----------------------------------some more advanced methods
# 1) index - will find element's index in the lsit
# arr = [1,2,2,3,1,5,3,1,6,5,2]
# print(arr.index(5,6,10)) #syntax index(ele's index that you want, from to look, till look(will count this ele too))

# # 2) count - will count that how many times element is in the list
# print(arr.count(2))

# # 3) reverse the list
# arr.reverse()
# print(arr) # will mutate the orignal list too

# #  4) sort - will mututate the orignal list too
# arr.sort()
# print(arr)

#  5) join - will convert list into the string
# # ---------------------------------------IMPORTANT
# #  join doesn't work like it owrks in JS. it's weired here
# # here join usually joins some string into the array
# coding = ['coding', 'is', 'fun']
# print(' '.join(coding)) #JS version - coding conding.join('')=no space, coding.join(' ')=joined with space, coding.join('---')=joined with ---
# print('-----'.join(coding))

# 6) slice --- syntax list_name[from_index: to_index(dosnt include this one. like rangefn): step] - won't mutuate the orignal list
color = ['red', 'yellow', 'orange', 'silver', 'purple', 'green']
print(color[0:4])
print(color[-5:])  # will print till yellow(from reverse direction).

# to
print(color[:3])  # will print first 3 index ele(0-2)
print(color[1:-3])  # will print yello and orange

# step - almost like increment by +2, +3 etc. like range(0,10,2)
print(color[::2])  # will print even index color from 0
# left out negative step thing. lil bit coplex

# updating any list with slice
nos = [1, 2, 3, 4, 5]
nos[1:3] = ['a', 'b', 'c']
print(nos)
