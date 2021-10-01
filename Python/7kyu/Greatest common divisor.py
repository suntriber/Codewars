"""
Find the greatest common divisor of two positive integers. The integers can be large, so you need to find a clever solution.

The inputs x and y are always greater or equal to 1, so the greatest common divisor will always be an integer that is also greater or equal to 1.
"""
def main():
    print(mygcd(30,12),6)
    print(mygcd(8,9),1)
    print(mygcd(1,1),1)



def mygcd(x, y):
    import math
    return math.gcd(x,y)

    # return x if y == 0 else mygcd(y, x % y)

    # while y:
    #     x,y=y,x%y
    # return x

    # return x if not y else mygcd(y, x%y)

    # return mygcd(y, x % y) if y else x


if __name__ == "__main__":
    main()