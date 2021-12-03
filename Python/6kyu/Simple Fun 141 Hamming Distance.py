"""
Task
The hamming distance between a pair of numbers is the number of binary bits that differ in their binary notation.

Example
For a = 25, b= 87, the result should be 4

25: 00011001
87: 01010111
The hamming distance between these two would be 4 ( the 2nd, 5th, 6th, 7th bit ).

Input/Output
[input] integer a
First Number. 1 <= a <= 2^20

[input] integer b
Second Number. 1 <= b <= 2^20

[output] an integer
"""


def hamming_distance(a, b):
    return sum([i != j for i,j in zip(bin(a)[2:].zfill(16), bin(b)[2:].zfill(16))])



if __name__ == "__main__":
    print(hamming_distance(25,87),4)
    print(hamming_distance(256,302),4)
    print(hamming_distance(543,634),4)
    print(hamming_distance(34013,702),7)



# def hamming_distance(a, b):
#     return bin(a ^ b).count('1')



# def hamming_distance(a, b):
#     return sum(int(i) for i in bin(a^b)[2:])
    


# def hamming_distance(a, b):
#     return sum(x != y for x, y in zip(format(a, "020b"), format(b, "020b")))



# hamming_distance=lambda a,b:bin(a^b).count('1')


# def hamming_distance(a: int, b: int) -> int:
#     return f'{a ^ b:b}'.count('1')
