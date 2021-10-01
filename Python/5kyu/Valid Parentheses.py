"""
Write a function called that takes a string of parentheses, 
and determines if the order of the parentheses is valid. 
The function should return true if the string is valid, 
and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
"""

def main():
    
    print(valid_parentheses("  ("),False)
    print(valid_parentheses(")test"),False)
    print(valid_parentheses(""),True)
    print(valid_parentheses("hi())("),False)
    print(valid_parentheses("hi(hi)()"),True)
    print(valid_parentheses('(())((()())())'), True)
    

def valid_parentheses(string):
    length = (string.count('(') + string.count(')')) // 2
    for i in range(length):
        string = "".join([s for s in string if s =='(' or s == ')']).replace('()','')
    if not string:
        return True
    else:
        return False
    


    
    
   
    



    
    
   






    """
    l, r = 0, 0
    if string.count('(') == string.count(')'):
        for i, c in enumerate(string):
            if c == '(':
                l += i
            elif c == ')':
                r += i
        if r > l:
            return True
        else:
            return False
    else:
        return False
    """

if __name__ == "__main__":
    main()


