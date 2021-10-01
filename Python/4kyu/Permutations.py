"""
In this kata you have to create all permutations of an input string and remove duplicates, if present. 
This means, you have to shuffle all letters from the input in all possible orders.

Examples:

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
"""
from itertools import permutations as perm

def main():
    print(sorted(permutations('a')), ['a'])
    print(sorted(permutations('ab')), ['ab', 'ba'])
    print(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])


def permutations(string):
    #combo = [''.join(p) for p in perm(string)]    # all possible combinations of string
    #return list(dict.fromkeys(combo))    # removes duplicates from list
    return list(dict.fromkeys([''.join(p) for p in perm(string)]))


if __name__ == "__main__":
    main()