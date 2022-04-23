"""
https://www.codewars.com/kata/57f4ccf0ab9a91c3d5000054/train/python
"""
def get_octal(item):
    s = 0
    if item[0] == 'r':s+=4
    if item[1] == 'w':s+=2
    if item[2] == 'x':s+=1
    return str(s)


def chmod_calculator(perm):
    s = ['0', '0', '0']
    for k,v in perm.items():
        if k == 'user':s[0] = get_octal(perm['user'])
        if k == 'group':s[1] = get_octal(perm['group'])
        if k == 'other':s[2] = get_octal(perm['other'])
    return ''.join(c for c in s)
    

if __name__ == "__main__":
    print(chmod_calculator({"user": 'rwx', "group": 'r-x', "other": 'r-x'}),"-->","755")
    print(chmod_calculator({"user": 'rwx', "group": 'r--', "other": 'r--'}),"-->","744")
    print(chmod_calculator({"user": 'r-x', "group": 'r-x', "other": '---'}),"-->","550")
    print(chmod_calculator({"group": 'rwx'}),"-->","070")
    print(chmod_calculator({}),"-->","000")


"""
def chmod_calculator(perm):
    return ''.join(str(('r' in (y := perm.get(x, '---')))*4 + ('w' in y)*2 + ('x' in y)) for x in ('user', 'group', 'other'))
"""
