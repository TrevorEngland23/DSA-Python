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

# priority queues