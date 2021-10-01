"""
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. 
Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

Examples:

findNextSquare(121) --> returns 144
findNextSquare(625) --> returns 676
findNextSquare(114) --> returns -1 since 114 is not a perfect square
"""
def main():
    print(find_next_square(121), 144, "Wrong output for 121")
    print(find_next_square(625), 676, "Wrong output for 625")
    print(find_next_square(319225), 320356, "Wrong output for 319225")
    print(find_next_square(15241383936), 15241630849, "Wrong output for 15241383936")
    print(find_next_square(0), 1)


def find_next_square(sq):
    import math
    if math.sqrt(sq).is_integer():
        for i in range(sq+1, (sq+1)*2):
            if math.sqrt(i).is_integer():
                return int(i)
    else:
        return -1
    
    # return (math.sqrt(sq) + 1) ** 2 if (math.sqrt(sq)).is_integer() else -1
    # return (sqrt(sq)+1)**2 if sqrt(sq)%1 == 0 else -1
    
    # x = sq**0.5    
    # return -1 if x % 1 else (x+1)**2

    # return (sq**0.5+1)**2 if int(sq**0.5)**2 == sq else -1

if __name__ == "__main__":
    main()