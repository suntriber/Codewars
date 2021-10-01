"""
Find the sum of the digits of all the numbers from 1 to N (both ends included).

Examples
# N = 4
1 + 2 + 3 + 4 = 10

# N = 10
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) = 46

# N = 12
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) + (1 + 1) + (1 + 2) = 51
"""
def main():
    print(compute_sum(1), 1)
    print(compute_sum(2), 3)
    print(compute_sum(3), 6)
    print(compute_sum(4), 10)
    print(compute_sum(10), 46)
    print(compute_sum(12), 51)


def compute_sum(n):

    return sum([int(m) for x in range(n+1) for m in str(x)])

    #return sum(int(c) for i in range(1, n+1) for c in str(i))
    #return sum(map(int,''.join(str(n) for n in range(n+1))))
    #return sum([i if type(i)!=str else sum([int(s) for s in i]) for i in [i if i<10 else str(i) for i in [i for i in range(1,n+1)]]])
    #return sum(sum(int(c) for c in str(x)) for x in range(n+1))

if __name__ == "__main__":
    main()