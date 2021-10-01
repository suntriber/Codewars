"""
We need prime numbers and we need them now!

Write a method that takes a maximum bound and returns all primes up to and including the maximum bound.

For example,

11 => [2, 3, 5, 7, 11]
"""
def main():
    print(prime(0),[])
    print(prime(1),[])
    print(prime(2),[2])
    print(prime(5),[2,3,5])
    print(prime(10),[2,3,5,7])
    print(prime(15),[2,3,5,7,11,13])
    print(prime(25),[2,3,5,7,11,13,17,19,23])
    print(prime(35),[2,3,5,7,11,13,17,19,23,29,31])
    print(prime(50),[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47])


def prime(n):
    return [x for x in range(n+1) if is_prime(x)]



def is_prime(x):
    #return n == 2 or n > 2 and n % 2 and all(n % i for i in range(3, int(n ** .5) + 1, 2))
    if x >= 2:
        for y in range(2,x//2+1):
            if not ( x % y ):
                return False
    else:
	    return False
    return True


if __name__ == "__main__":
    main()