"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""

def main():
    s1 = "apples, pears # and bananas\ngrapes\nbananas !apples"
    print(f'{solution(s1, ["#", "!"])}apples, pears\ngrapes\nbananas')
    print(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")


def solution(string, markers):
    s = ''
    i = 0
    for _ in range(len(string)):
        try:
            if string[i] not in markers:
                s += string[i]
            else:
                while string[i] != '\n':
                    i += 1
                s = s[:len(s)-1] + string[i]
            i += 1
        except IndexError:
            return s[:len(s)-1]+'\n'


if __name__ == "__main__":
    main()