#
# Example file for working with loops
#

def main():
    # x = 0

    # # define a while loop
    # while(x < 5):
    #     print(x)
    #     x = x+1
    # print("----------------------------")
    # # define a for loop
    # for x in range(5, 10):  # will print 5 to 9. its like range. not tradtional loop. if for x in range(7) op= 1-6 no printed
    #     print(x)

    # use a for loop over a collection
    days = ["mon", "tues", "wed", "thurs", "fri", "sat", "sun"]
    # equvicalent to arr.length. will itreate till array's length and print each element one by one
    for day in days:
        print(day)
    # with enurmate we can print the index value too. like normal function in JS
    for i, day in enumerate(days):
        print(f'index no is {i} and day is {day}')

    # use the break and continue statements
    for i in range(5, 10):
        if(i == 7):
            # continue is same like legacy. will skip the step(based oon your condition)
            break
        print(i)
    # using the enumerate() function to get index


if __name__ == "__main__":
    main()
