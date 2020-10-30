"""
Consider the numbers 6969 and 9116. When you rotate them 180 degrees (upside down), these numbers remain the same. 
To clarify, if we write them down on a paper and turn the paper upside down, the numbers will be the same. 
Try it and see! Some numbers such as 2 or 5 don't yield numbers when rotated.

Given a range, return the count of upside down numbers within that range. For example, solve(0,10) = 3, 
because there are only 3 upside down numbers >= 0 and < 10. They are 0, 1, 8.

More examples in the test cases.

Good luck!
"""

def main():
    """
    print(solve(0,10),3)
    print(solve(10,100),4)
    print(solve(100,1000),12)
    print(solve(1000,10000),20)
    print(solve(10000,15000),6)
    print(solve(15000,20000),9)
    print(solve(60000,70000),15)
    print(solve(60000,130000),55)
    """
    solve(0,100)


def solve(a, b):
    upside_down = {0: 0, 1: 1, 2: False, 3: False, 4: False, 5: False, 6: 9, 7: False, 8: 8, 9: 6}
    limits = list(range(a, b))
    nums = []
    for n in limits:
        if len(str(n)) > 1:
            

        if n == upside_down.get(n):
            nums.append(n)
            
    print(nums)
                
        



if __name__ == "__main__":
    main()