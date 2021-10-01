"""
Complete the function that takes a list of numbers (nums), as the only argument to the function. 
Take each number in the list and square it if it is even, or square root the number if it is odd. 
Take this new list and return the sum of it, rounded to two decimal places.

The list will never be empty and will only contain values that are greater than or equal to zero.
"""

def main():
    print(sum_square_even_root_odd([4,5,7,8,1,2,3,0]), 91.61)
    print(sum_square_even_root_odd([1,14,9,8,17,21]), 272.71)


def sum_square_even_root_odd(nums):
    return float(f'{sum([x**2 if x%2==0 else x**0.5 for x in nums]):.2f}')


if __name__ == "__main__":
    main()
