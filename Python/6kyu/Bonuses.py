"""
John wants to give a total bonus of $851 to his three employees taking fairly into account their 
number of days of absence during last year. Employee A was absent 18 days, B 15 days, and C 12 days.

The more absences, the lower the bonus ...

How much should each employee receive? John thinks A receives $230, B $276, C $345.

Task:
Given an array arr (numbers of days of absence for each employee) and a number s (total bonus) 
the function bonus(arr, s) returns an array of the fair bonuses of all employees in the same order 
as their numbers of days of absences.

s and all elements of arrays are positive integers.

Examples:
bonus([18, 15, 12], 851) -> [230, 276, 345]

bonus([30, 27, 8, 14, 7], 34067) -> [2772, 3080, 10395, 5940, 11880]
"""

def main():
    """
    print(bonus([22, 3, 15], 18228), [1860, 13640, 2728])
    print(bonus([8, 14, 11], 23541), [10241, 5852, 7448])
    print(bonus([8, 20, 17], 25281), [13515, 5406, 6360])
    print(bonus([25, 22, 15, 22, 22], 5213), [858, 975, 1430, 975, 975])
    print(bonus([10, 11, 30, 12, 17, 23, 30, 11, 17, 10], 1788210), [258060, 234600, 86020, 215050, 151800, 112200, 86020, 234600, 151800, 258060])
    print(bonus([22, 3, 15], 18228), [1860, 13640, 2728])
    """
    bonus([22, 3, 15], 18228)
    # 18228 / 3 = 6076
    # RATIO == 1.363636364, 10, 2
    # find ratio by dividing the lowest element with all others.
    # lowest element has ratio of 1
    # calculate each part with formula:
    # p = total_sum,    a, b, c ... n = ratios
    # 
    # a * p / (a + b + c)  = sum for a
    

def bonus(arr, s):
    """
    ratios = [min(arr)/x for x in arr]
    return [int(x/sum(ratios)*s) for x in ratios]
    """
   
    year = [365-x for x in arr]
    rat = [max(year)/x for x in year]
    print(year)
    print(rat)
    print([min(arr)/x for x in arr])

    
    


if __name__ == "__main__":
    main()