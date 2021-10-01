"""
Create a simple calculator that given a string of operators (), +, -, *, / 
and numbers separated by spaces returns the value of that expression

Example:

Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7
Remember about the order of operations! Multiplications and divisions have a 
higher priority and should be performed left-to-right. Additions and subtractions 
have a lower priority and should also be performed left-to-right.
"""

def main():
    print(Calculator().evaluate("2 / 2 + 3 * 4 - 6"), 7)
    print(Calculator().evaluate("3 * 4 + 3 * 7 - 6"), 27)
    print(Calculator().evaluate('1 + 1'), 2)
    print(Calculator().evaluate("( ( ( ( 1 ) * 2 ) ) )"), 2)
    print(Calculator().evaluate("( ( ( ( ( ( ( 5 ) ) ) ) ) ) )"), 5)
    print(Calculator().evaluate("2 * ( 2 * ( 2 * ( 2 * 1 ) ) )"), 16)
    print(Calculator().evaluate("3 * ( 4 + 7 ) - 6"), 27)


class Calculator(object):
    def evaluate(self, string):
        return 0



if __name__ == "__main__":
    main()