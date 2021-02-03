import sys
import cubeModule
# how to improt only some specific module
from cubeModule import square
import random

# importing path
from pathlib import Path
# # /////////////////////////////////////// DICTIONARY----------------- key value pair data---------------OBJECT------------------------
# student = {
#     "name": "nimit",
#     "age": 26,
#     "isLegal": True
# }
# print(student)
# # how to print some specific value
# print(student["age"])
# print(student.get("namee"))  # will print none instead of giving error
# print(student.get("isMarried", "false"))  # we can put default value too

# ----------------------------------FUNCTIONS---------------------------
# def greeting(firstName, lastName):
#     print(f'Hello {firstName} {lastName}😊')


# greeting("Nimit", "Chavda")
# # we can change the args order with defining args and passing the name
# greeting(lastName="Chavda", firstName="Nimit")


# def cube(param):
#     return param*param*param


# print(cube(5))

# # we can return mutiple elemtns from fucntion too
# def name(ff, dd):
#     return ff, dd


# # this will be tuple. below
# print(name(12, 33))

# # ---------------------------------EXCEPTIONS-----------------------------------------------
# try:
#     age = int(input("enter the age"))
#     print(f'you are {age} year old!')
#     print(23/age)
# except ValueError:
#     print("please don't add string!")
# # except ZeroDivisionError:
#     # print("age can't be zero")
# # this below will be used for unknown error. like a default for all error. try commenting zerodiv exception and tthen divide by zero. will print err message too
# except:
#     print(f'unknown err " + {sys.exc_info()[1]}')
# else:
#     print("all good!")

# # -------------------------------------------------CLASS----------------------------------------------
# class Point:
#     # how to write constructor
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     # always use self in args while decalring functions
#     def move(self):
#         print("moving!")

#     # how to pass any var into any fucntion dynamically
#     def draw(self):
#         print(f'drawing! and value of x is {self.x}')


# point1 = Point(222, 33)
# point1.move()
# print(point1.y)
# point1.y = 123456
# print(f'value of y changed to {point1.y}')
# point1.draw()

# # ############## --- INHERITANCE---------------


# class Animal:
#     def walk(self):
#         print("walking!")


# # how to extend any clss. just type class name(class_that_you_want_to_extend)
# class cat(Animal):
#     def cuddling(self):
#         print("All hail Lord Cat🐈")


# kitty = cat()
# kitty.walk()
# kitty.cuddling()

# ------------------------------------------------MODULES-----------------------------------------------
# # BREAK DOWN THE CODE INTO MUTLIPLE FILES
# print(cubeModule.cube(2))
# # below will be directly called from module like we defined code in this current file
# print(square(3))

# # ----------------------------RANDOM VALUES JUST CODE--------------------------------------------
# for i in range(3):
#     print(random.random())
#     # for int in some specific range(from,to)
#     print(random.randint(1, 6))

# members = ["nimit", "jim", "michael", "dwight"]
# leader = random.choice(members)
# print(leader)

# ----------------------------------------------DIRECTORIES--------------------------------------------
# abs path

# relative path
path = Path("xx")
print(path.mkdir())  # will create xx dir if not exist
print(path.rmdir())  # will delete the dir
# path.rename("xxx")
