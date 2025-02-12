from functools import lru_cache
#A naive recursive implementation of 0-1 Knapsack Problem
 
# Returns the maximum value that can be put in a knapsack of
# capacity W
# called = 0
@lru_cache(maxsize=128)
def knapSack(W , wt , val , n):
    # called += 1
    # print(f'Called : {called}')
    # Base Case
    if n == 0 or W == 0 :
        return 0
 
    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W , wt , val , n-1)
 
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1),
                   knapSack(W , wt , val , n-1))
 
# end of function knapSack
 
# To test above function
val = (60, 100, 120, 20, 160, 110, 85)
wt = (10, 20, 30, 2, 40, 25, 15)
W = 50
n = len(val)
from time import time
start = time()
for i in range(10000):
    knapSack(W , wt , val , n)
    # knapSack.cache_clear()
duration = time() - start
print(f'duration : {duration}')
 
# This code is contributed by Nikhil Kumar Singh
