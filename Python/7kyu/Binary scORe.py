# https://www.codewars.com/kata/56cafdabc8cfcc3ad4000a2b/train/python


def score(n):
    if n < 2:
        return n
    i = 0
    while n!=0:
        n>>=1
        i+=1
    return (1<<i)-1


if __name__ == "__main__":
    print(score(0), 0)
    print(score(1), 1)
    print(score(49), 63)
    print(score(1000000), 1048575)