# https://www.codewars.com/kata/52fba2a9adcd10b34300094c/train/python

def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]



if __name__ == "__main__":
    print(transpose([[1]]), [[1]])
    print(transpose([[1, 2, 3]]), [[1], [2], [3]])
    print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                    [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
    print(transpose([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]]),
                    *[[1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0]])


"""
def transpose(matrix):
    return list(map(list, zip(*matrix)))
"""

"""
def transpose(matrix):
    return [list(x) for x in zip(*matrix)]
"""

"""
import numpy as np
def transpose(matrix):
    return np.transpose(np.matrix(matrix)).tolist()
"""

"""
transpose = lambda m: [list(c) for c in zip(*m)]
"""