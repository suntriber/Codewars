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




"""
def snail(array):
    results = []
    while len(array) > 0:
        # go right
        results += array[0]
        del array[0]

        if len(array) > 0:
            # go down
            for i in array:
                results += [i[-1]]
                del i[-1]

            # go left
            if array[-1]:
                results += array[-1][::-1]
                del array[-1]

            # go top
            for i in reversed(array):
                results += [i[0]]
                del i[0]

    return results


data = [[1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]]

data2 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
expected2 = [1, 2, 3, 6, 9, 8, 7, 4, 5]

print(snail(data2))
print(snail(data))
"""



"""
def snail(array):
    ret = []
    if array and array[0]:
        size = len(array)
        for n in xrange((size + 1) // 2):
            for x in xrange(n, size - n):
                ret.append(array[n][x])
            for y in xrange(1 + n, size - n):
                ret.append(array[y][-1 - n])
            for x in xrange(2 + n, size - n + 1):
                ret.append(array[-1 - n][-x])
            for y in xrange(2 + n, size - n):
                ret.append(array[-y][n])
    return ret
"""


"""
import numpy as np

def snail(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m
"""

"""
# my implementation/explanation of the solution by foxxyz
def snail(array):
  if array:
    # force to list because zip returns a list of tuples
    top_row = list(array[0])
    # rotate the array by switching remaining rows & columns with zip
    # the * expands the remaining rows so they can be matched by column
    rotated_array = zip(*array[1:])
    # then reverse rows to make the formerly last column the next top row
    rotated_array = rotated_array[::-1]
    return top_row + snail(rotated_array)
  else:
    return []
"""


"""
def snail(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1] # Rotate
    return out
"""


"""
def snail(array):
    next_dir = {"right": "down", "down":"left", "left":"up", "up":"right"}
    dir = "right"
    snail = []
    while array:
        if dir == "right":
            snail.extend(array.pop(0))
        elif dir == "down":
            snail.extend([x.pop(-1) for x in array])
        elif dir == "left":
            snail.extend(list(reversed(array.pop(-1))))
        elif dir == "up":
            snail.extend([x.pop(0) for x in reversed(array)])    
        dir = next_dir[dir]
    return snail  
"""


"""
import numpy as np

def snail(array):
    arr = np.array(array)
    
    if len(arr) < 2:
        return arr.flatten().tolist()
    
    tp = arr[0, :].tolist()
    rt = arr[1:, -1].tolist()
    bm = arr[-1:, :-1].flatten()[::-1].tolist()
    lt = arr[1:-1, 0] [::-1].tolist()    
    
    return tp + rt + bm + lt + snail(arr[1:-1, 1:-1])
"""



"""
def snail(array):
    res = []
    while len(array) > 1:
        res = res + array.pop(0)
        res = res + [row.pop(-1) for row in array]
        res = res + list(reversed(array.pop(-1)))
        res = res + [row.pop(0) for row in array[::-1]]
    return res if not array else res + array[0]
"""


"""
def trans(array):
    #Do an inverse transpose (i.e. rotate left by 90 degrees
    return [[row[-i-1] for row in array] for i in range(len(array[0]))] if len(array)>0 else array

def snail(array):
    output=[]
    
    while len(array)>0:

        #Add the 1st row of the array
        output+=array[0]
        #Chop off the 1st row and transpose
        array=trans(array[1:])
        
    return output
"""


"""
def _snail(array):
    n = len(array)
    for a in range(0, (n + 1) // 2):
        b = n - 1 - a
        for j in range(a, b + 1):
            yield array[a][j]
        for i in range(a + 1, b + 1):
            yield array[i][b]
        for j in range(b - 1, a - 1, -1):
            yield array[b][j]
        for i in range(b - 1, a, -1):
            yield array[i][a]

def snail(array):
    return list(_snail(array)) if array and array[0] else []
"""


# snail = lambda a: list(a[0]) + snail(zip(*a[1:])[::-1]) if a else []
# def snail(array): return array[0] + snail(list(map(list, [*zip(*array[1::])][::-1]))) if array else []


"""
import itertools

def snake(x):
    while x:
        yield x[0]
        x = list(reversed(zip(*x[1:])))

def snail(array):
    return list(itertools.chain(*snake(array)))¨
"""



"""
import numpy as np

def _rotation(arr):   
    # Visually, executes a counterclockwise rotation of inputed array:
    #                 ---->      [[6,9],  
    #     [[4,5,6],  becomes      [5,8],
    #      [7,8,9]]   ---->       [4,7]]  
    return arr[0::,-1::-1].transpose()


def snail(arr):
    arr = np.array(arr) # input not passed in as an array.
    a = arr[0,::] # first row. 
    while arr.shape[0] > 1:
        arr = _rotation(arr[1::]) # rotate everything but the first row. 
        a = np.append(a, arr[0,::]) # append first row of the rotated array. 
    return list(a)   
"""  



"""
def snail(array):
    a = []
    while array:
        a.extend(list(array.pop(0)))
        array = zip(*array)
        array = list(array)
        array.reverse()
    return a
"""



"""
def snail(snail_map):
    if snail_map:
        top_row = list(snail_map.pop(0))
        rotated_map = list(zip(*[row[::-1] for row in snail_map]))
        return top_row + snail(rotated_map)
    else:
        return []
"""



"""
def snail(snail_map):
    arr = []
    while snail_map:
        arr += snail_map.pop(0)
        snail_map = list(zip(*snail_map))
        snail_map.reverse()
    return arr
"""



"""
def snail(a):
    m = []
    while a:
        m = m + list(a[0])
        a = list(zip(*(i[::-1] for i in a[1:])))
    return m
"""



"""
def snail(arr):
    return arr[0] if len(arr) == 1 else [*arr.pop(0), *[el.pop() for el in arr], *arr.pop()[::-1], *[el.pop(0) for el in arr[::-1]]] + snail(arr) if len(arr) else []
"""


# def snail(snail_map):
#     return snail_map and [*snail_map.pop(0)] + snail([*zip(*snail_map)][::-1])
#     pass