"""
Compare two strings by comparing the sum of their values (ASCII character code).

For comparing treat all letters as UpperCase
null/NULL/Nil/None should be treated as empty strings
If the string contains other characters than letters, treat the whole string as it would be empty
Your method should return true, if the strings are equal and false if they are not equal.

Examples:
"AD", "BC"  -> equal
"AD", "DD"  -> not equal
"gf", "FG"  -> equal
"zz1", ""   -> equal (both are considered empty)
"ZzZz", "ffPFF" -> equal
"kl", "lz"  -> not equal
null, ""    -> equal
"""

def main():
    print(compare("AD", "BC"), True, "\'AD\' vs \'BC\'")
    print(compare("AD", "DD"), False, "\'AD\' vs \'DD\'")
    print(compare("gf", "FG"), True, "\'gf\' vs \'FG\'")
    print(compare("Ad", "DD"), False, "\'Ad\' vs \'DD\'")
    print(compare("zz1", ""), True, "\'zz1\' vs \'\'")
    print(compare("ZzZz", "ffPFF"), True, "\'ZzZz\' vs \'ffPFF\'")
    print(compare("kl", "lz"), False, "\'kl\' vs \'lz\'")
    print(compare(None, ""), True, "\'<null>\' vs \'\'")
    print(compare("!!", "7476"), True, "\'!!\' vs \'7476\'")
    print(compare("##", "1176"), True, "\'##\' vs \'1176\'")




def compare(s1,s2):

    if not s1 or not s1.isalpha():
        sum_1 = 0
    else:
        sum_1 = sum([ord(c) for c in s1.upper()]) if s1.isalpha() else 0
    if not s2 or not s2.isalpha():
        sum_2 = 0
    else:
        sum_2 = sum([ord(c) for c in s2.upper()]) if s2.isalpha() else 0

    return sum_1 == sum_2


if __name__ == "__main__":
    main()