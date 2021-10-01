"""
We want to know the index of the vowels in a given word, for example, there are two vowels in the word super (the second and fourth letters).

So given a string "super", we should return a list of [2, 4].

Some examples:
Mmmm  => []
Super => [2,4]
Apple => [1,5]
YoMama -> [1,2,4,6]
"""
def main():
    print(vowel_indices("mmm"), [], "failed on the word 'mmm'")
    print(vowel_indices("apple"), [1,5], "failed on the word 'apple'")
    print(vowel_indices("123456"), [], "failed on the word '123456'")
    print(vowel_indices("UNDISARMED"), [1,4,6,9], "failed on the word 'UNDISARMED'. Consider case")


def vowel_indices(word):
    return [i+1 for i in range(len(word)) if word[i].lower() in 'aeiouy']


if __name__ == "__main__":
    main()