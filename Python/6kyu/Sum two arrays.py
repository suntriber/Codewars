"""
Your task is to create a function called sum_arrays() in Python or addArrays in Javascript, 
which takes two arrays consisting of integers, and returns the sum of those two arrays.

The twist is that (for example) [3,2,9] does not equal 3 + 2 + 9, it would equal '3' + '2' + '9' 
converted to an integer for this kata, meaning it would equal 329. The output should be an array 
of the the sum in a similar fashion to the input (for example, if the sum is 341, 
you would return [3,4,1]). Examples are given below of what two arrays should return.

[3,2,9],[1,2] --> [3,4,1]
[4,7,3],[1,2,3] --> [5,9,6]
[1],[5,7,6] --> [5,7,7]
If both arrays are empty, return an empty array.

In some cases, there will be an array containing a negative number as the first index in the array. 
In this case treat the whole number as a negative number. See below:

[3,2,6,6],[-7,2,2,8] --> [-3,9,6,2] # 3266 + (-7228) = -3962
"""
def main():
    ############# TESTING ##################
    """
    print(sum_arrays([3,2,9],[1,2]),[3,4,1])
    print(sum_arrays([4,7,3],[1,2,3]),[5,9,6])
    print(sum_arrays([1],[5,7,6]),[5,7,7])
    print(sum_arrays([-3,4,2],[3,4,4]),[2])
    print(sum_arrays([],[]),[])
    print(sum_arrays([0],[]),[0])
    print(sum_arrays([],[1,2]),[1,2])
    print(sum_arrays([3,2,9],[1,2]),[3,4,1])
    print(sum_arrays([4,7,3],[1,2,3]),[5,9,6])
    print(sum_arrays([1],[5,7,6]),[5,7,7])
    print(sum_arrays([-3,4,2],[3,4,4]),[2])
    print(sum_arrays([],[]),[])
    print(sum_arrays([0],[]),[0])
    print(sum_arrays([],[1,2]),[1,2])
    """
    ########################################
    print(sum_arrays([-8,9,6,1,5,0], [6]), [-8,9,6,1,4,4])

def sum_arrays(array1,array2):
   
    arr1, arr2 = '',''
    for item in array1:
        arr1 += str(item)
    for item in array2:
        arr2 += str(item)
    try:
        comb = int(arr1)+int(arr2)
        return [int(x,10) for x in str(comb)]
    except ValueError:
        if not array1:
            return array2
        elif not array2:
            return array1
        
    
       

if __name__ == "__main__":
    main()