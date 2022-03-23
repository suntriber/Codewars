# https://www.codewars.com/kata/5590961e6620c0825000008f/train/python

def swap(string_):return string_.swapcase()


if __name__ == "__main__":
    print(swap('HelloWorld'), 'hELLOwORLD')
    print(swap('CodeWars'), 'cODEwARS')


# swap = lambda s: "".join([c.lower() if c.isupper() else c.upper() for c in s])
# def swap(str):return ''.join( i.upper() if i >= 'a' else i.lower() for i in str )