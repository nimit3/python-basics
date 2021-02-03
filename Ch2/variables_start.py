#
# Example file for variables
#

# Declare a variable and initialize it
# we don't need to declare type of var. simple like JS, but not even let, var etc
name = "Nimit"
print(name)

# re-declaring the variable works
name = 222
print(name)

# ERROR: variables of different types cannot be combined
# below line will not run. we can't do like this.in JS we can do.

# print("This is a string" + 123)
# in python data type must be same whhile using it together
print("This is nimit " + str(123))

# Global vs. local variables in functions


def someFunction():
    print("Inside the function")
    global name  # if you remove this global then varibale's scope will only remain inside the function
    name = "xxx"
    print(name)


someFunction()
print(name)  # op = 222

# how to delete the variable

del name
# print(name)  # error this line will give an error because name is deleted
name = "sex"
print(name)
