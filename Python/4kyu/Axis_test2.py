"""
You are given a string S consisting of letters 'a' and/or 'b'.
A block is a consecutive fragment of S composed of the same letters
and surrounded by different letters or string endings. For example, 
S = "abbabbaaa" has five blocks:
"a", "bb", "a", "bb", and "aaa".

What is the minium number of additional letters needed to obtain a 
string containing blocks of equal lengths? Letters can be added only 
at the beginning or at the end of an existing block.

Write a function:

def solution(S):

thats, given a string S of length N, return the minimum number of
additional letters to obtain a string containing blocks of equal lengths.

Examples:

1. Given S = "babaa", the function should return 3. There are four blocks,
"b", "a", "b", and "aa". One letter each should be added to the first, second,
and third blocks, therefore obtaining a string "bbaabbaa", in which every block
is of equal length.

2. Given S = "bbbab", the function should return 4. Two letters each should be 
added to the second and third blocks, therefore obtaining a string
"bbbaaabbb", in which every block is equal length.

3. Given S = "bbbaaabbb", the function should return 0. All blocks are of 
equal lengths.

Write an efficient algorithm for the following assumptions:

 - N is an integer within the range [1..40000];
 - string S consists only of the characters "a" and/or "b"
"""
from itertools import groupby

def main():
    test_one = "babaa"           # should return 3
    test_two = "bbbab"           # should return 4
    test_three = "bbbaaabbb"     # should return 0

    print(solution(test_one))
    print(solution(test_two))
    print(solution(test_three))


def solution(S):
    # blocks = [''.join(g) for _, g in groupby(S)]
    # lengths = [len(c) for c in blocks]
    # return sum([max(lengths) - x for x in lengths])
    return sum([max([len(c) for c in [''.join(g) for _, g in groupby(S)]]) -x for x in [len(c) for c in [''.join(g) for _, g in groupby(S)]]])


if __name__ == "__main__":
    main()