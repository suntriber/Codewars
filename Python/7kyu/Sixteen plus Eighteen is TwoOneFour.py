"""
16+18=214

  1 6
 +1 8
------
  2 14
"""


def add(n1,n2):
    return ''.join(str(int(a)+int(b)) for a,b in zip(str(n1), str(n2)))




if __name__ == "__main__":
    print(add(16,18), 214)
    print(add(26,39), 515)
    print(add(122,81), 1103)