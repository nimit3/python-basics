import math
import random

# type conversion int(), float(), str() etc
# age = int(input('ENter the age'))
# print(f'you were born in {2020 - age}')
# print(int('22') -2)
# ll=[1,2,3]
# print(str(ll))

# printing type of any var
# print(type(5555.555))

# how to print element multiple time
# print("N" * 4)

# how to print multiple lines using ''' ---------------------string------------- '''
# course = '''
# fw2f2e
# fefwq
# fewfew
# '''
# print(course)

# how to print some specific chars(from to limit chars) in string
# name = "Nimit Chavda"
# firstName = name[0:6]  # we can use that syntax for declaring vars too
# print(name[0:6] + " ------- " + firstName)  # this will only print Nimit

# # formatted strings (`` what we use in JS equivalent ${})
# # var = f'{name} {int(4+5)} {str("22222")}' or we can use f"     " toooooo(double "")
# # print(var)

# # calculating length of string
# print(len(name))

# # string.includes() equivalent
# print('Nimit' in name)

# name='nimit chavda dineshkumar'
# print(name.split(' '))

# --------------NONE-----------------
# None in python is almost equivalent to "null"
# child = None  # if you want to define something with nothing until you get some value later in your prog then "None" can be used
# print(child)
# print(type(child))  # will print NoneType

# -------------------------------------------------------------------------------------------------------------------------
# print(round(33.3333))
# max min abs etc can be used as the same way above
# print(max(22, 3333, 44444))

# logical and and or
# if((56 > 6) and (5 < 66)):
#     print("yesssssssssssss")
# # for or just use or(no ||) for not just use not
# if(not(55 < 4)):
#     print('not in the action')

# ///////////////////////////////////////////// while //////////////////////////////////////////////////////
# while loop can have its own else block in python. that else will be executed once while loop is finished. "if while loop gets break in the middle then it won't be executed"
# i = 0
# while(i < 5):
#     print(f'the value of i is {i}')
#     # if(i == 4):
#     #     break
#     i = i+1
# else:
#     print('loop finished and now else part of while loop is executed')

# /////////////////////////////////// FOR LOOPS////////////////////////
# name = "Nimit"
# arr = [1, 2, 3, 4, 5]
# for i in name:
#     print(i)
# for i in arr:
#     print(i)

# range for for loop.         from to till
# range syntax 1) range(10)======= will from 0 to 9
# syntax 2) range(1,10) ======= will go from 1 to 9
# syntax 3 range(1,10,2) ==== will increment by 2. op ======1,3,5,7,9
# printing total
# j = 0
# for i in range(1, 10, 2):
#     j = j+i
#     print(j)

# for i in range(7,0,-1): #will print from 7 to 1 while decreasing everything by 1
#     print(i)

# nested loops
# for i in range(4):
#     for j in range(3):
#         print(f'i = {i} & j = {j}')


# ---------------------------------------------------------------------TUPLES-----------------------------------------------
# #  we can't modify the tuple like array. no instert, removal can be done. we can only get information about elements
# # its just ------------------------------------IMMUTABLE------------------------------------
#  tupes can't be nested
# tup = (1, 2, 3)
# print(type(tup))
# print(tup[1])

# # unpacking tuple into variables. like destructruing in JS
# x, y, z = tup
# print(x, y, z)
# arr = [1, 2, 3]
# a, b, c = arr
# print(a, b, c)

# #  we can use tuple in dictionary as key too
# office = {
#     (222,3423.4): 'vadodara',
#     (22223,423.5): 'toronto'
# }
# print(office)

# ----------------------------------------------------------------SETS-----------------------------------
#  init of set
set1 = {1, 2, 3, 4}
# method 2
set2 = set({6.7, 8, 9})
print(f'{set1} and {set2}')
# method 3
set3 = set([1, 2, 4, 4, 1, 3])
print(set3)
# we can use "IN" function here too
print(2 in set1)
# we can iterate through sets just like normal iterating through list

#  set methods
set1.add('vv')
print(set1)
set1.remove('vv')
print(set1)
# for removing any elemtns. same like remove. but it wont throw an error in case you pass something in args that is not in the list
set1.discard(4)
print(set1)
