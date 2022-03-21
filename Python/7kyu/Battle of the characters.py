# https://www.codewars.com/kata/595519279be6c575b5000016/train/python

def battle(x, y):return x if sum([ord(c)-64 for c in x])>sum([ord(c)-64 for c in y]) else y if sum([ord(c)-64 for c in y])>sum([ord(c)-64 for c in x]) else 'Tie!'


if __name__ == "__main__":
        print(battle("AAA", "Z"), "Z", "Unfair fight!")
        print(battle("ONE", "TWO"), "TWO", "Unfair fight!")
        print(battle("ONE", "NEO"), "Tie!", "Unfair fight!")
        print(battle("FOUR", "FIVE"), "FOUR", "Unfair fight!")


"""
battle = lambda x,y,fn = lambda z: sum(ord(c) - 64 for c in z):\
["Tie!",x,y][(fn(x) > fn(y)) - (fn(x) < fn(y))]
"""

"""
def battle(x, y):
    X, Y = sum(ord(i)-64 for i in x), sum(ord(i)-64 for i in y)
    return X > Y and x or X < Y and y or 'Tie!'
"""

"""
battle=lambda x,y,f=lambda s:sum(ord(c)-64for c in s):["Tie!",x,y][(f(x)>f(y))-(f(x)<f(y))]
"""