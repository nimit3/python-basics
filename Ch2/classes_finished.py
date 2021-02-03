#
# Example file for working with classes
#


class myClass():
    def method1(self):
        print("myClass method1")

    def method2(self, someString):
        print("myClass method2: " + someString)


# extending another class
class anotherClass(myClass):
    def method2(self, sometString):
        print("anotherClass method2")

    def method1(self):
        # how tp call parent class method into child class method
        myClass.method1(self)  # will print "myClass method1"
        print("anotherClass method1")


def main():
    c = myClass()
    c.method1()
    c.method2("This is a string")
    print("-------------------------------------------------------")

    c2 = anotherClass()
    c2.method1()
    # c2.method2("xxxxxxxxxxxxxxxxxxxxx")


if __name__ == "__main__":
    main()
