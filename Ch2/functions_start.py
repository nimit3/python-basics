#
# Example file for working with functions
#

# define a basic function
def function1():
    print("I am a function")

# function that takes arguments


def func2(arg1, arg2):
    print(arg1, "", arg2)

# function that returns a value


def cube(arg1):
    return arg1*arg1*arg1

# function with default value for an argument


def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# function with variable number of arguments


def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result


function1()  # op = I am a function
print(function1())  # I am a function
print(function1)  # op = None because it's not returning any value
func2("name", "bc")
print(cube(2))

print("------------------------------------------------")

print(power(3, 3))

print(multi_add(1, 2, 3, 4, 5))
