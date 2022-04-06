# https://www.codewars.com/kata/539ee3b6757843632d00026b/train/python

def capitals(word):
    return [i for i in range(len(word)) if word[i].isupper()]


if __name__ == "__main__":
    print(capitals('CodEWaRs'), [0,3,4,6])