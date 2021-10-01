"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
"""


def square_digits(num):
    return int(''.join([str(int(n)**2) for n in str(num)]))


if __name__ == "__main__":
    print(square_digits(9119), 811181)
    print(square_digits(0), 0)


"""
def square_digits(num):
    # s converts num to a str so we can index through it
    # when then loop through the len of the str 
    # while we're looping the string we convert it back to a int and square it
    # after we add it to a str to keep it from adding and then convert it to a int
    s = str(num)
    t = len(s)
    y=0
    g= 0
    b=""
    while y < t:
        g = int(s[y])**2 
        b= b+ str(g) 
        final = int(b)
        y=y+1
    return(final)   
    pass
"""

"""
def square_digits(n):
  return int("".join(str(pow(int(i), 2)) for i in str(n)))
"""

