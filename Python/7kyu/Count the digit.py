# https://www.codewars.com/kata/566fc12495810954b1000030/train/python

def nb_dig(n, d):

    tmp = ''

    for i in range(n+1):
        tmp += str(i**2)

    return tmp.count(str(d))


if __name__ == "__main__":
    print(nb_dig(5750, 0), 4700)
    print(nb_dig(11011, 2), 9481)
    print(nb_dig(12224, 8), 7733)
    print(nb_dig(11549, 1), 11905)



"""
def nb_dig(n, d):
    return ''.join(str(a ** 2) for a in xrange(n + 1)).count(str(d))
"""


"""
def nb_dig(n, d):
    return sum(str(i*i).count(str(d)) for i in range(n+1))
"""


"""
nb_dig = lambda n,d: sum(str(k**2).count(str(d)) for k in range(n+1))
"""