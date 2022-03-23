# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

def digital_root(n):
    # Recursive solution, return sum of all digits in n if < 9 else recursive call with that sum
    return sum([int(i) for i in str(n)]) if sum([int(i) for i in str(n)])<10 else digital_root(sum([int(i) for i in str(n)]))


if __name__ == "__main__":
    print(digital_root(16), 7)
    print(digital_root(942), 6)
    print(digital_root(132189), 6)
    print(digital_root(493193), 2)


# def digital_root(n):return n if n < 10 else digital_root(sum(map(int,str(n))))
# def digital_root(n):return n%9 or n and 9 
# def digital_root(n):return 1 + ((int(n) - 1) % 9) if n>0 else 0