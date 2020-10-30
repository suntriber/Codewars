"""
Consider the following array:

[1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789, 12345678910, 1234567891011...]
If we join these blocks of numbers, we come up with an infinite sequence which starts with 112123123412345123456.... The list is infinite.

You will be given an number (n) and your task will be to return the element at that index in the sequence, where 1 ≤ n ≤ 10^18. Assume the indexes start with 1, not 0. For example:

solve(1) = 1, because the first character in the sequence is 1. There is no index 0. 
solve(2) = 1, because the second character is also 1.
solve(3) = 2, because the third character is 2.
More examples in the test cases. Good luck!
"""

def main():
    
    #print(solve(1), 1)
    #print(solve(2), 1)
    #print(solve(3), 2)
    #print(solve(100), 1)
    #print(solve(2100), 2)
    #print(solve(31000), 2)
    #print(solve(99999999))
    print(solve(999999999999999999), 4) 
    #print(solve(1000000000000000000), 1)
    #print(solve(999999999999999993), 7)
    
  
    
    
# INCOMPLETE #

"""
There are 9 numbers with 1 digit:
first: 1 (sequence length: 1 * 1)  
last: 9 (sequence length: 9 * 1)  
average sequence length: (1 + 9) / 2 = 5  
1-digit block length: 9 * 5 = 45  

There are 90 numbers with 2 digits:
first: 10 (sequence length: 9 * 1 + 1 * 2)  
last: 99 (sequence length: 9 * 1 + 90 * 2)  
average sequence length: 9 + (2 + 180) / 2 = 100  
2-digit block length: 90 * 100 = 9000  

There are 900 numbers with 3 digits:
first: 100 (sequence length: 9 * 1 + 90 * 2 + 1 * 3)  
last: 999 (sequence length: 9 * 1 + 90 * 2 + 900 * 3)  
average sequence length: 9 + 180 + (3 + 2,700) / 2 = 1,540.5  
3-digit block length: 900 * 1,540.5 = 1,386,450  

There are 9,000 numbers with 4 digits:
first: 1,000 (sequence length: (9 * 1) + (90 * 2) + (900 * 3) + (1 * 4))
last: 9,999 (sequence length: (9 * 1) + (90 * 2) + (900 * 3) + (9,000 * 4))
average sequence length: 9 + 180 + 2,700 + (3 + 36000) / 2 = 18,001.5
4-digit block length: 9,000 * 18,001.5 = 162,013,500

There are 90000 numbers with 5 digits:
first: 10,000 (sequence length: (9 * 1) + (90 * 2) + (900 * 3) + (9,000 * 4) + (1 * 5))
last: 99,999 (sequence length: (9 * 1) + (90 * 2) + (900 * 3) + (9,000 * 4) + (90,000 * 5))
average sequence length: 9 + 180 + 2,700 + 36,000 + (5 + 450,000) / 2 = 263,891.5 
5-digit block length: 90,000 * 263,891.5 = 2.3750235E10   (23,750,235,000)

There are 900,000 numbers with 6 digits:
first: 100,000 (sequence length: (9 * 1) + (90 * 2) + (900 * 3) + (9,000 * 4) + (90,000 * 5) + (1 * 6))
last: 999,999 (sequence length: (9 * 1) + (90 * 2) + (900 * 3) + (9,000 * 4) + (90,000 * 5) + (900,000 * 6))
average sequence length: 9 + 180 + 2,700 + 36,000 + 450,000 + (6 + 5,400,000) / 2 = 3,188,892
6-digit block length: 900,000 * 3,188,892 = 2.8700028E12   (2,870,002,800,000)

There are 9,000,000 numbers with 7 digits:
first: 1,000,000 (sequence length: (9 * 1) + (90 * 2) + (900 * 3) + (9,000 * 4) + (90,000 * 5) + (900,000 * 6) + (1 * 7))
last: 9,999,999 (sequence length: (9 * 1) + (90 * 2) + (900 * 3) + (9,000 * 4) + (90,000 * 5) + (900,000 * 6) + (9,000,000 * 7))
average sequence length: 9 + 180 + 2,700 + 36,000 + 450,000 + 5,400,000 + (7 + 63,000,000) / 2 = 37,388,892.5
7-digit block length: 9,000,000 * 37,388,892.5 = 3.365000325E14   (336,500,032,500,000)

There are 90,000,000 numbers with 8 digits:
first: 10,000,000 (sequence length: (9 * 1) + (90 * 2) + (900 * 3) + (9,000 * 4) + (90,000 * 5) + (900,000 * 6) + (9,000,000 * 7) + (1 * 8))
last: 99,999,999 (sequence length: (9 * 1) + (90 * 2) + (900 * 3) + (9,000 * 4) + (90,000 * 5) + (900,000 * 6) + (9,000,000 * 7) + (90,000,000 * 8))
average sequence length: 9 + 180 + 2,700 + 36,000 + 450,000 + 5,400,000 + 63,000,000 + (8 + 720,000,000) / 2 = 428,888,893
8-digit block length: 90,000,000 * 428,888,893 = 3.860000037E16   (38,600,000,370,000,000)

There are 900,000,000 numbers with 9 digits:
first: 100,000,000 (sequence length: (9 * 1) + (90 * 2) + (900 * 3) + (9,000 * 4) + (90,000 * 5) + (900,000 * 6) + (9,000,000 * 7) + (90,000,000 * 8) + (1 * 9))
last: 999,999,999 (sequence length: (9 * 1) + (90 * 2) + (900 * 3) + (9,000 * 4) + (90,000 * 5) + (900,000 * 6) + (9,000,000 * 7) + (90,000,000 * 8) + (900,000,000 * 9))
average sequence length: 9 + 180 + 2,700 + 36,000 + 450,000 + 5,400,000 + 63,000,000 + 720,000,000 + (9 + 8,100,000,000) / 2 = 4,838,888,894
9-digit block length: 900,000,000 * 4,838,888,894 = 4.355000004E18   (4,355,000,004,000,000,000)
"""



def solve(n):
    sumz = 0
    block = 1

    while n >= sumz:
        sumz += block
        block += 1
    print(f'The number {n} is in block {block} with a sum of {sumz}')

"""
def solve(n):
    index_we_want = n
    index_we_are_at = 0
    number_we_are_up_to = 1

    while index_we_are_at < index_we_want:
        str_to_check = get_string(number_we_are_up_to)
        number_we_are_up_to += 1

        if index_we_are_at + len(str_to_check) >= index_we_want:
            get_index = index_we_want - index_we_are_at
            ret_num = str_to_check[get_index-1]
            return ret_num

        index_we_are_at += len(str_to_check)


def get_string(number):
    str_to_check = ''
    for i in range(1, number+1):
        str_to_check += str(i)
    return str_to_check
"""


"""
def solve(n):
    i, total, tmp = 1,'1','1'
    while len(total) <= n:
        i += 1
        tmp += str(i)
        total += str(tmp)
        print(total)
        
    return int(total[n-1])
"""



if __name__ == "__main__":
    main()