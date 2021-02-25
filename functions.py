# ----------------------------------FUNCTIONS---------------------------
def greeting(firstName, lastName):
    print(f'Hello {firstName} {lastName}😊')


greeting("Nimit", "Chavda")
# we can change the args order with defining args and passing the name
greeting(lastName="Chavda", firstName="Nimit")


def cube(param):
    return param*param*param


print(cube(5))

# we can return mutiple elemtns from fucntion too


def name(ff, dd):
    return ff, dd


# this will be tuple. below
print(name(12, 33))


def xxx(listt):
    if(listt):
        ll = len(listt)
        return listt[ll-1]
    return None


print(xxx([]))
