"""
Given a number, return a string with dash'-'marks before and after each odd integer, but do not begin or end the string with a dash mark.

Ex:

dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'
"""

def main():
    
    print(dashatize(274),"2-7-4", "Should return 2-7-4")
    print(dashatize(5311),"5-3-1-1", "Should return 5-3-1-1")
    print(dashatize(86320),"86-3-20", "Should return 86-3-20")
    print(dashatize(None),"None", "Should return None")
    print(dashatize(0),"0", "Should return 0")
    print(dashatize(-1),"1", "Should return 1")
    print(dashatize(-28369),"28-3-6-9", "Should return 28-3-6-9")
    
    
def dashatize(num):
    if num == 0:
        return '0'
    elif not num:
        return 'None'
    elif abs(num) == 1:
        return '1'
    
    num = abs(num)
    dash = []
    num = list(str(num))
    if int(num[0]) %2 != 0:
        dash.append(num[0]+'-')
    else:
        dash.append(num[0])
    for i in range(1, len(num)-1):
        if int(num[i]) %2 != 0 and int(num[i-1]) %2 == 0:
            dash.append('-'+num[i]+'-')
        elif int(num[i]) %2 != 0 and int(num[i-1]) %2 != 0:
            dash.append(num[i]+'-')
        else:
            dash.append(num[i])
    if int(num[len(num)-1]) %2 != 0 and int(num[len(num)-2]) %2 == 0:
        dash.append('-'+num[len(num)-1])
    else:
        dash.append(num[len(num)-1])
    
    return ''.join([x for x in dash])
    

if __name__ == "__main__":
    main()
