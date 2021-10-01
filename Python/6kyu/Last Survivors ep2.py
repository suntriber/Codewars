"""
Substitute two equal letters by the next letter of the alphabet (two letters convert to one):

"aa" => "b", "bb" => "c", .. "zz" => "a".
The equal letters do not have to be adjacent.
Repeat this operation until there are no possible substitutions left.
Return a string.

Example:

let str = "zzzab"
    str = "azab"
    str = "bzb"
    str = "cz"
return "cz"
Notes
The order of letters in the result is not important.
The letters "zz" transform into "a".
There will only be lowercase letters.
"""

def main():
    # print(last_survivors('zzzab'), 'cz')

    a = 'a'
    z = 'z'
    print(ord(a))
    print(ord(z))
    print(122-97)

    import numpy as np

    a = np.zeros((12, 12))
    a[8, 3] = 8

    a[(2, 3, 4, 5, 6, 7, 8, 9, 10), 1] = 1

    a[(2, 10), 2] = 1

    a[(2, 3, 4, 5, 6, 7, 10), 3] = 1

    a[(4, 8), 4] = 1

    a[10, 4] = 6

    a[2, 5] = 3

    a[(4, 6, 7, 8), 5] = 1

    a[(2, 3, 4), 6] = 1

    a[(4, 5, 6, 7, 8, 9), 7] = 1

    a[2, 7] = 6

    a[9, 8] = 1

    a[2, 9] = 7

    a[(3, 4, 5, 9), 9] = 1

    a[7, 9] = 3

    a[(5, 6, 7, 8, 9), 10] = 1

    a[3, 10] = 6
    print(a)

    #print(last_survivors('zzzab'))


def last_survivors(s):
    from collections import Counter
    d = Counter(s)
    multiple, single = '', ''




if __name__ == "__main__":
    main()