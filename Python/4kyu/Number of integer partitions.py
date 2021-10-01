"""
An integer partition of n is a weakly decreasing list of positive integers which sum to n.

For example, there are 7 integer partitions of 5:

[5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1].

Write a function named partitions which returns the number of integer partitions of n. The function should be able to find the number of integer 
partitions of n for n as least as large as 100.
"""

def main():
    print(partitions(1) == 1)
    print(partitions(5) == 7)
    print(partitions(10) == 42)
    print(partitions(25) == 1958)



def partitions(n):
    # table[i] will be storing the number of
    # solutions for value i. We need n+1 rows
    # as the table is consturcted in bottom up
    # manner using the base case (n = 0)
    # Initialize all table values as 0
    table =[0] * (n + 1)
 
    # Base case (If given value is 0)
    # Only 1 way to get 0 (select no integer)
    table[0] = 1
 
    # Pick all integer one by one and update the
    # table[] values after the index greater
    # than or equal to n
    for i in range(1, n ):
 
        for j in range(i , n + 1):
 
            table[j] +=  table[j - i]           
 
    return table[n]+1   




if __name__ == "__main__":
    main()




"""
def partitions(n):
    c = [[1]]
    for x in range(1, n + 1):
        c.append([0])
        for m in range(1, x + 1):
            c[x].append(c[x][m - 1] + c[x - m][min(m, x - m)])
    return c[n][n]




def partitions(n, k=1, cache={}):
    if k > n: return 0
    if n == k: return 1
    if (n,k) in cache: return cache[n,k]
    return cache.setdefault((n,k), partitions(n, k+1) + partitions(n-k, k))




ls = [1,1,2,3,5,7,11,15,22,30,42,56,77,101,135,176,231,297,385,490,627,792,1002,1255,1575,1958,2436,3010,3718,4565,5604,6842,8349,10143,12310,14883,17977,21637,26015,31185,37338,44583,53174,63261,75175,89134,105558,124754,147273,173525,204226,239943,281589,329931,386155,451276,526823,614154,715220,831820,966467,1121505,1300156,1505499,1741630,2012558,2323520,2679689,3087735,3554345,4087968,4697205,5392783,6185689,7089500,8118264,9289091,10619863,12132164,13848650,15796476,18004327,20506255,23338469,26543660,30167357,34262962,38887673,44108109,49995925,56634173,64112359,72533807,82010177,92669720,104651419,118114304,133230930,150198136,169229875,190569292]
def partitions(n):   
    return ls[n]





from functools import lru_cache

@lru_cache(maxsize=None)
def partitions(n, start=1):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    return sum(partitions(n-i, i) for i in range(start, n+1))






def partitions(n):
    part = [0] * (n + 1)
    part[0] = 1
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            part[j] += part[j - i]
    return part[-1]





dic={}
def partitions(n,x=None, maxx=None):
    x,maxx = (n,n) if x==None else (x,maxx)
    return sum([dic[(x-i,i)] if (x-i,i) in dic else(0 if dic.update({(x-i,i):partitions(n,x-i,i)}) else dic[(x-i,i)])for i in range(1,min([maxx,x])+1)[::-1]]) if x else 1




from functools import lru_cache

@lru_cache(maxsize=16384)
def partition_helper(sum, largest_number):
    if largest_number == 0: return 0
    if sum == 0: return 1
    if sum < 0: return 0
    return partition_helper(sum, largest_number - 1) + partition_helper(sum - largest_number, largest_number)

partitions = lambda n: partition_helper(n, n)




def partitions(n: int) -> int:
    parts = [1] + [0] * n
    
    for i in range(1, n + 1):
        for j, k in enumerate(range(i, n + 1)):
            parts[k] += parts[j]
            
    return parts[n]





def partitions(n):
    arr_result =[0] * (n + 1) 
    arr_result[0] = 1
    for i in range(1, n): 
        for j in range(i , n + 1): 
            arr_result[j] = arr_result[j] + arr_result[j-i] 
    return arr_result[n] + 1


"""




