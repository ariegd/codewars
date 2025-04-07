#!/usr/bin/python3

import inspect

def foo(msg):
    print(msg)
    ###▼ YOUR INSPECTION CODE ▼###
    print("\t«{}»\tLine number in which the function is defined.".
           format(inspect.getsourcelines(foo)[1]))
    print("\t«{}»\tLine from which the function has been called.".
           format(inspect.stack()[1][2]))
    print("\t«{}»\tInvoking/calling function.".format(inspect.stack()[1][3]))
    print("\t«{}»\tModule in which it is contained.\n".format(foo.__module__))

def suma(a, b):
    foo("Call from [suma()], on the line [14]")
    return a+b

def difference(a, b):
    foo("Call from [difference()], on the line [18]")
    return a-b

def main():
    foo("Call from [main()], on the line [22]")
    suma(3,6)
    foo("Call from [main()], on the line [24]")
    difference(5,2)

if __name__ == "__main__":
    main()

