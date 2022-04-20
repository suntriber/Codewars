# https://www.codewars.com/kata/58039f8efca342e4f0000023/train/python

def changer(s):
    r = list(s)
    
    for i,c in enumerate(r):
        if c.isalpha():
            if c == 'z' or c == 'Z':
                r[i]='A'
            else:
                r[i] = chr(ord(r[i])+1)
    
    for i,c in enumerate(r):
        if c in 'aeiou':
            r[i] = r[i].upper()
        elif c in 'bcdfghjklmnpqrstvxyz'.upper():
            r[i] = r[i].lower()
    
    return ''.join([n for n in r])
            



if __name__ == "__main__":
    print(changer('Cat30'), 'dbU30')
    print(changer('Alice'), 'bmjdf')
    print(changer('sponge1'), 'tqpOhf1')
    print(changer('Hello World'), 'Ifmmp xpsmE')
    print(changer('dogs'), 'Epht')
    print(changer('z'), 'A')
    print(changer('aLWN7tCV'), 'bmxO7UdW')
    print(changer('lt8lUHo1V0kQp3F'), 'mU8mvIp1w0lrq3g')