"""
Description:
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.
Example:
sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
"""

def main():
    sort_array([1,9,3,7,5,6,2,8,0])


def sort_array(source_array):
    temp_odd = sorted([x for x in source_array if x%2 != 0])
    for i, n in enumerate(source_array):
        if n%2 !=0:
            source_array[i] = temp_odd[0]
            temp_odd.remove(temp_odd[0])
    return(source_array)


if __name__ == "__main__":
    main()