"""
Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks 
whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, 
that the elements in b are the elements in a squared, regardless of the order.

Examples
Valid arrays
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 
20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets 
obvious if we write b's elements in terms of squares:

a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
"""

import math

def main():
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    print(comp(a1, a2), True)

    print(func2(10, 20, 30, 40))


def comp(array1, array2):
    for i in array2:
        if math.sqrt(i) not in array1:
            return False 
    return True


def func1(x,y,z):
    return x*2, y*3, z*4

def func2(*args):
    return ' '.join([str(x) for x in args])

if __name__ == "__main__":
    main()