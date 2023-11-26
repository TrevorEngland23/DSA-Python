# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# The number of elements initialized in nums1 and nums2 are m and n respectively
# You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2

# Initial thoughts: Given that nums1 has enough space to hold every single element, I want to try to avoid creating a new array to work with as that takes up space. It should be fully possible to work with the two given arrays and return the answer as nums1, which would give us a constant space complexity.

# we know that the emtpy alotted space in the array nums1 is at the END of the array. Let's not shift things around more than we need to. What we can do, is create 3 pointers to look at the last index of nums1, the last value of nums1, and the last value of nums2. Compare the values of nums1 and nums2. whichever is greatest moves to the end of nums1. move the nums1 end pointer to the left one, and whichever pointer the value came from, move that pointer to the left as well. rinse and repeat.

def merge(nums1, m, nums2, n): # nums1 and nums2 are the arrays. m and n is how we determine the last value in nums1/num2 respectively
    # get pointers
    last = m + n - 1 # last allocated index of nums1 
    # remember, m and n are the pointers for the last known values 

    while m>0 and n>0: # while there are elements in both arrays
        if nums1[m-1] > nums2[n-1]: # find the larger value between the two
            nums1[last] = nums1[m-1] # move that value to the last position in nums1
            m -= 1 # move pointer to left one
        else: # otherwise, if they are equal to each other, or if nums2 had the greater value
            nums1[last] = nums2[n-1] # move that value to the end of nums1
            n -= 1
        last -= 1 # regardless of which value is greater, this pointer gets decremented every single iteration

    # if we get here, that means that nums1 had larger values but there are still values in nums2 array to be copied over
    while n > 0:
        nums1[last] = nums2[n-1] # since these arrays are sorted, we know that this singular array is sorted, so we can copy over the left over array in reverse order.
        n -= 1 # decrement the pointer 
        last -= 1 # decrement last pointer
    
    return nums1


print(merge([1,3,5,0,0,0], 3, [2,4,6], 3)) # [1,2,3,4,5,6]