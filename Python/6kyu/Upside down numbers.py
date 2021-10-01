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
    print()
    print()
    print()
    #solve(0,100)

    string = 'pynative'

    #print(''.join([string[i] for i in range(len(string)) if not i%2]))
    #print(*[string[i]+'\n' for i in range(len('pynative')) if not i%2])
    print(*[string[i] for i in range(0,len('pynative'),2)])

    print()
    print()
    print()
    print('pynative'[4::])


    valid = 'tive'
    string = 'pynative'

    for c in string:
        if c in valid:
            print(c)
    
    print(func([1,2,3,1,6]))

    

    string = 'Emma is a good developer. Emma is a writer.'

    print(f'Emma appeared {string.count("Emma")} times')


    for i in range(1,6):
        print(f'{i}'*i)


    print(func2(1212))

    print(func3([10,20,23,11,17],[13,43,24,36,12]))


def func3(ls1, ls2):
    return [x for x in ls1 if x%2] + [y for y in ls2 if not y%2]

def func2(nr):
    return str(nr)[::] == str(nr)[::-1]

def func(myL):
    return myL[0] == myL[-1]


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