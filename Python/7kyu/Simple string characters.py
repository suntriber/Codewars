# https://www.codewars.com/kata/5a29a0898f27f2d9c9000058/train/python


def solve(s):
    l = []
    l.append(len([n for n in s if n.isupper()]))
    l.append(len([n for n in s if n.islower()]))
    l.append(len([n for n in s if n.isdigit()]))
    l.append(len(s)-sum(l))
    return l



if __name__ == "__main__":
    print(solve("Codewars@codewars123.com"),[1,18,3,2])
    print(solve("bgA5<1d-tOwUZTS8yQ"),[7,6,3,2])
    print(solve("P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H"),[9,9,6,9])
    print(solve("RYT'>s&gO-.CM9AKeH?,5317tWGpS<*x2ukXZD"),[15,8,6,9])
    print(solve("$Cnl)Sr<7bBW-&qLHI!mY41ODe"), [10,7,3,6])
    print(solve("@mw>0=QD-iAx!rp9TaG?o&M%l$34L.nbft"), [7,13,4,10])