"""
Count the number of divisors of a positive integer n.

Random tests go up to n = 500000.

Examples
divisors(4)  == 3  # 1, 2, 4
divisors(5)  == 2  # 1, 5
divisors(12) == 6  # 1, 2, 3, 4, 6, 12
divisors(30) == 8  # 1, 2, 3, 5, 6, 10, 15, 30
"""

def main():
    print(divisors(1), 1) 
    print(divisors(4), 3)
    print(divisors(5), 2)
    print(divisors(12), 6)
    print(divisors(30), 8)
    print(divisors(4096), 13)


def divisors(n):
    return len([x for x in range(1, n+1) if not n%x])

    # return sum(1 for i in xrange(1, n + 1) if n % i == 0)
    # return  len([l_div for l_div in range(1, n + 1) if n % l_div == 0])
    # return sum([True if n % x == 0 else False for x in range(1, n + 1)])
    # return sum([n % x == 0 for x in range(1, n + 1)])

    
# divisors = lambda n: sum([n % x == 0 for x in range(1, n + 1)])

if __name__ == "__main__":
    main()