"""
Consider the following array:

[1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789, 12345678910, 1234567891011...]
If we join these blocks of numbers, we come up with an infinite sequence which starts with 112123123412345123456.... The list is infinite.

You will be given an number (n) and your task will be to return the element at that index in the sequence, where 1 ≤ n ≤ 10^18. Assume the indexes start with 1, not 0. For example:

solve(1) = 1, because the first character in the sequence is 1. There is no index 0. 
solve(2) = 1, because the second character is also 1.
solve(3) = 2, because the third character is 2.
More examples in the test cases. Good luck!
"""

def main():
    
    print(solve(1), 1)
    print(solve(2), 1)
    print(solve(3), 2)
    print(solve(100), 1)
    print(solve(2100), 2)
    print(solve(31000), 2) 
    #print(solve(999999999999999999), 4) 
    #print(solve(1000000000000000000), 1)
    #print(solve(999999999999999993), 7)
    
    
    
# INCOMPLETE #

def solve(n):
    i, total, tmp = 1,'1','1'
    while len(total) <= n:
        i += 1
        tmp += str(i)
        total += str(tmp)
    return int(total[n-1])




if __name__ == "__main__":
    main()