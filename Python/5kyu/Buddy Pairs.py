"""
Buddy pairs
You know what divisors of a number are. The divisors of a positive integer n are said to be proper when you consider only the divisors other than n itself. 
In the following description, divisors will mean proper divisors. For example for 100 they are 1, 2, 4, 5, 10, 20, 25, and 50.

Let s(n) be the sum of these proper divisors of n. Call buddy two positive integers such that the sum of the proper divisors of each number is one more than the other number:

(n, m) are a pair of buddy if s(m) = n + 1 and s(n) = m + 1

For example 48 & 75 is such a pair:

Divisors of 48 are: 1, 2, 3, 4, 6, 8, 12, 16, 24 --> sum: 76 = 75 + 1
Divisors of 75 are: 1, 3, 5, 15, 25 --> sum: 49 = 48 + 1
Task
Given two positive integers start and limit, the function buddy(start, limit) should return the first pair (n m) of buddy pairs such that n (positive integer) 
is between start (inclusive) and limit (inclusive); m can be greater than limit and has to be greater than n

If there is no buddy pair satisfying the conditions, then return "Nothing" or (for Go lang) nil

Examples
(depending on the languages)

buddy(10, 50) returns [48, 75] 
buddy(48, 50) returns [48, 75]
or
buddy(10, 50) returns "(48 75)"
buddy(48, 50) returns "(48 75)"
"""

def main():
    
    # print(buddy(10, 50), [48, 75])
    # print(buddy(48,50), [48, 75])
    # print(buddy(2177, 4357), "Nothing")
    # print(buddy(57345, 90061), [62744, 75495])
    # print(buddy(1071625, 1103735), [1081184, 1331967])
    
    #print(buddy(10, 50), [48, 75])
    for i in range(1071625, 1103735):
        print(get_divisors(i))

def buddy(start, limit):
    keep = True
    while keep:
        for i in range(start, limit):
            n = sum(get_divisors(i))
            for j in range(i+1, i+limit):
                m = sum(get_divisors(j))
                if (m == i+1) and (n == j+1):
                    n1 = i
                    m2 = j
                    keep = False
    return [n1,m2]


def get_divisors(n):
    return [x for x in range(1,n) if n%x==0]

if __name__ == "__main__":
    main()