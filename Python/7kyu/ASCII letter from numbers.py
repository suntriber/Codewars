# https://www.codewars.com/kata/589ebcb9926baae92e000001/train/python

def convert(n):
    return ''.join([chr(int(n[i]+n[i+1])) for i in range(0, len(n), 2)])


if __name__ == "__main__":
    print(convert("65"),"A")
    print(convert("656667"),"ABC")
    print(convert("676584"),"CAT")
    print(convert("73327673756932858080698267658369"),"I LIKE UPPERCASE")