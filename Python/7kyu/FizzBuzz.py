"""
Return an array containing the numbers from 1 to N, where N is the parametered value.

Replace certain values however if any of the following conditions are met:

If the value is a multiple of 3: use the value "Fizz" instead
If the value is a multiple of 5: use the value "Buzz" instead
If the value is a multiple of 3 & 5: use the value "FizzBuzz" instead
N will never be less than 1.

Method calling example:

fizzbuzz(3) -->  [1, 2, "Fizz"]
"""

def main():
    print(fizzbuzz(10))


def fizzbuzz(n):
    return ['FizzBuzz' if i%3==0 and i%5==0 else 'Fizz' if i%3==0 else 'Buzz' if i%5==0 else i for i in range(1,n+1)]

    # return ['Fizz'*(not i%3) + 'Buzz'*(not i%5) or i for i in range(1, n+1)]
    # return ['FizzBuzz' if i%15 == 0 else 'Fizz' if i%3 == 0 else 'Buzz' if i%5 == 0 else i for i in range(1,n+1)]
    # return ['Fizz' * (not i%3) + 'Buzz' * ( not i%5) if not i%3 or not i%5 else i for i in range(1, n + 1)]



if __name__ == "__main__":
    main()