"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
"""

def main():
    print(accum("ZpglnRxqenU"), "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")
    print(accum("NyffsGeyylB"), "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")
    print(accum("MjtkuBovqrU"), "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu")
    print(accum("EvidjUnokmM"), "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm")
    print(accum("HbideVbxncC"), "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc")


def accum(s):
    b = ''
    for i in range(len(s)):
        b += s[i].upper() + s[i].lower()*i + '-'
    return b[:len(b)-1]




if __name__ == "__main__":
    main()




"""

return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

return '-'.join((a * i).title() for i, a in enumerate(s, 1))


output = ""
for i in range(len(s)):
    output+=(s[i]*(i+1))+"-"
return output.title()[:-1]

return '-'.join([c.upper() + c.lower() * i for i, c in enumerate(s)])


return "-".join([((j*(i+1)).capitalize()) for i,j in enumerate(s)])


return "-".join(list(x.upper() + x.lower() * count for count, x in enumerate(s)))

"""
