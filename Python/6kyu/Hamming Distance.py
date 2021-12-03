"""
The Hamming Distance is a measure of similarity between two strings of equal length. Complete the function so that it returns the number of positions where the input strings do not match.

Examples (in JavaScript):

hamming("I like turtles","I like turkeys")  //returns 3
hamming("Hello World","Hello World")  //returns 0
You can assume that the two input strings are of equal length.
"""

def hamming(a, b):
    return len([i for i in zip(a, b) if i[0] != i[1]])



if __name__ == "__main__":
    print(hamming("hello world","hello tokyo"),4)
    print(hamming("a man a plan a canal","a man a plan sobanal"),3)
    print(hamming("hamming and cheese","Hamming and Cheese"),2)
    print(hamming("espresso","Expresso"),2)
    print(hamming("old father, old artificer","of my soul the uncreated "),24)



# def hamming(a,b):
#   return sum(ch1 != ch2 for ch1, ch2 in zip(a, b))


# def hamming(a,b):
#   return sum(x != y for x, y in zip(a,b))


# def hamming(a,b):
#   return [ca == cb for ca, cb in zip(a, b)].count(False)


# from operator import ne

# def hamming(a: str, b: str) -> int:
#     return sum(map(ne, a, b))


# def hamming(str1,str2):
#     return sum(a != b for a,b in zip(str1,str2))


