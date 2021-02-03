#
# Example file for working with conditional statements
#


def main():
    x, y = 100000, 100000

    # conditional flow uses if, elif, else
    if(x < y):
        st = "x is less than y"
    elif(x == y):
        st = "x is equal to y"
    else:
        st = "x is greater than y"
    print(st)

    # conditional statements let you use "a if C else b"
    # above code in 1 line
    st = "x is less than y" if(x < y) else "x is greter or equal to y"
    print(st)


if __name__ == "__main__":
    main()
