# https://www.codewars.com/kata/55606aeebf1f0305f900006f

def to_binary(n):
    # return str(bin(n))[2:] if n < 0 else int("{0:32b}".format(n))
    return ~(bin("{0:32b}".format(n))+1)



def main():

    pass

if __name__ == "__main__":
    # print(to_binary(2),"10")
    # print(to_binary(3),"11")
    # print(to_binary(4),"100")
    # print(to_binary(-3),"11111111111111111111111111111101")
    # print(to_binary(0),"0")
    main()