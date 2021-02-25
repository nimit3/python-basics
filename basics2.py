import sys
import cubeModule
# how to improt only some specific module
from cubeModule import square
import random

# importing path
from pathlib import Path

import keyword
import termcolor

print(termcolor.colored('Hello Nimit!', "yellow"))
# print(help(termcolor))

print(keyword.iskeyword('def'))
print(keyword.iskeyword('falseee'))

# # ---------------------------------EXCEPTIONS-----------------------------------------------


def testErr(age):
    try:
        # age = int(input("enter the age"))
        # print(f'you are {age} year old!')
        print(23/int(age))
    except ValueError:
        print("please don't add string!")
    # except ZeroDivisionError:
        # print("age can't be zero")
    # #--------------combining upper 2 execption at a same time
    # except (ZeroDivisionError, ValueError) as err:
    #     print('something went wrong!')
    #     print(err)
    # this below will be used for unknown error. like a default for all error. try commenting zerodiv exception and tthen divide by zero. will print err message too
    except:
        print(f'unknown err {sys.exc_info()[1]}')
    # else will run only when any exception blocks are not run
    else:
        print("all good!")
    finally:
        print('I will run all the time!')


testErr('fff')
# #----------------------------CUSTOM ERRORS--------------------------
# def colorize(text,color):
#     colorList = ['red','green','purple']
#     if color not in colorList:
#         raise ValueError('color is not in the list!')
#     if type(text) is not str:
#         raise TypeError('type has to be string!')
#     else:
#         print(f'color changed in {color}')

# colorize('hola Nimit','red')
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
# path = Path("xx")
# print(path.mkdir())  # will create xx dir if not exist
# print(path.rmdir())  # will delete the dir
# # path.rename("xxx")

print('------------------------------------------')
name = {
    "namee": "nimit",
    "age": 26
}

name2 = {
    "ismarried": False,
    "hasjob": True
}

news = {** name, ** name2}

print(news)
