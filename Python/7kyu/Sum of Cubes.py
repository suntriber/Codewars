"""
Write a function that takes a positive integer n, sums all the cubed values from 1 to n, and returns that sum.

Assume that the input n will always be a positive integer.

Examples: (Input --> output)

2 --> 9 (sum of the cubes of 1 and 2 is 1 + 8)
3 --> 36 (sum of the cubes of 1, 2, and 3 is 1 + 8 + 27)
"""

def sum_cubes(n):
    return sum([i**3 for i in range(n+1)])


if __name__ == "__main__":
    print(sum_cubes(1), 1)
    print(sum_cubes(2), 9)
    print(sum_cubes(3), 36)
    print(sum_cubes(4), 100)
    print(sum_cubes(10), 3025)
    print(sum_cubes(123), 58155876)



"""
def sum_cubes(n):
    return (n*(n+1)/2)**2
"""

"""
def sum_cubes(n):
    return sum( i**3 for i in range(n+1) )
"""


"""
def sum_cubes(n):
    return (n*n*(n+1)*(n+1))/4
"""
