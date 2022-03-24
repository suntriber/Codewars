# https://www.codewars.com/kata/56786a687e9a88d1cf00005d/train/python

def validate_word(word):
    # return True if not sum([word.upper().count(n) for n in word.upper()]) %len(word) else False
    l = []
    for c in word.upper():
        if c not in l:
            l.append(word.upper().count(c))
    print(l)
    print(sum(l)%len(l))
    return True if len(set(l)) == 1 else False


if __name__ == "__main__":
    print(validate_word("abcabc"),True)
    print(validate_word("Abcabc"),True)
    print(validate_word("AbcabcC"),False)
    print(validate_word("AbcCBa"),True)
    print(validate_word("pippi"),False)
    print(validate_word("abcabcd"),False)
    print(validate_word('a?b?xpxBabbbaPb?Xp'), False)


"""
from collections import Counter

def validate_word(word):
    return len(set(Counter(word.lower()).values())) == 1
"""

"""
def validate_word(word):
    word = word.lower()
    return len(set(word.count(c) for c in word)) == 1
"""


"""
def validate_word(word):
    word = word.lower()
    return all(word.count(i) == word.count(word[0]) for i in word)
"""