import heapq

# given an array of integers "arr" and an integer "k", find the kth largest element 

# example:
# [1, 2, 5, 7, 8, 3, 4, 6]
# k = 3
# the third largest element in arr is 6, so the function should return 6.

def kth_largest(arr, k):
    # repeaet the loop k-1 times, because at the end we want to use the max method to get the largest value that exists
    for i in range(k-1):
        arr.remove(max(arr)) # remove the larger elements
    return max(arr)

# time complexity of this is O(kn), space complexity is O(1) because we are using constant variables

# optimized solution

# sort the array

def kth_largest2(arr, k):
    # store the arr length in a variable
    n = len(arr)
    # sort the array from smallest to largest
    arr.sort()
    # if n is arr length, subtract k from n to find the kth largest element in arr
    return arr[n-k]

# time complexity is O(nlogn) (sort) and space complexity is O(1)
# way faster than the first solution, except in some cases

# optimized solution 2

# priority queues ...
# next element to be popped in the queue is not the one that first entered, but the one with highest priority
# import heapq - by defualt heapq finds the min heap, we want the max heap.. multiply values by -1 to reverse that order so we get max heap
def kth_largest3(arr, k):
    # build an arr that negates the original sign of the element. This is to transform the list into a max heap, so that the largest element is at the root, rather than the smallest element
    arr = [-element for element in arr]
    # turn the arr into a heap
    heapq.heapify(arr)
    # iterate through
    for i in range(k-1): # so.. if k is 4, you do the below operation 3 times, leaving the kth largest element in the heap
        # delete the smallest value found in the heap (in this case, the largest negative number)
        heapq.heappop(arr) 
    return -heapq.heapop(arr) # extract the value one more time, which is the kth largest element. reverse the sign back to the original sign, and return that value.

# time complexity of O(n klogn) space complexity of O(n)

