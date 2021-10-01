"""
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
"""

def main():
   
    array1 = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    expected1 = [1,2,3,6,9,8,7,4,5]
    print(snail(array1), expected1)


    array2 = [[1,2,3],
            [8,9,4],
            [7,6,5]]
    expected2 = [1,2,3,4,5,6,7,8,9]
    print(snail(array2), expected2)
    

def snail(snail_map):
    arr = [snail_map[0]]
    snail_map.remove(snail_map[0])
    for i in snail_map:
        arr.append(i[-1])
        snail_map.remove(i[-1])
    for j in snail_map[-1]:
        for n in j[::-1]:
            arr.append(n)
    snail_map.remove(snail_map[-1])
    if snail_map:
        snail(snail_map)
    else: 
        return arr


if __name__ == "__main__":
    main()