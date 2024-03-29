"""
In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. 
Your task will be to return the sum of the numbers that occur only once.

For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15. 
Every other number occurs twice.

More examples in the test cases.

Good luck!
"""

def main():
    print(repeats([4,5,7,5,4,8]),15)
    print(repeats([9, 10, 19, 13, 19, 13]),19)
    print(repeats([16, 0, 11, 4, 8, 16, 0, 11]),12)
    print(repeats([5, 17, 18, 11, 13, 18, 11, 13]),22)
    print(repeats([5, 10, 19, 13, 10, 13]),24)


def repeats(arr):
    t = 0
    for n in arr:
        if arr.count(n) == 1:
            t += n
    #return t
    return sum([x for x in arr if arr.count(x) == 1])

if __name__ == "__main__":
    main()