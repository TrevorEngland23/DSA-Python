# Given an integer array "nums", find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# What the question is asking is... starting from anywhwere in the array and going in order, what is the largest sum you can possibly come up with if you add the numbers togther.
# example [-1,2,5,0,-4,1] 
# the largest possible sum is 7, which derives from 2 + 5. so the returned answer would be [2,5]
# "Sliding Window" approach with a Time complexity of O(n) and space complexity of O(1)


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0] # initialize to the first value in the array as a default value, since you're starting with the first value anwyways
        currentSum = 0 # initialize the sum to be 0

        for number in nums: # iterate through the numbers array
            if currentSum < 0: # checks the value of currentSum. If the value is negative...
                currentSum = 0 # reset the currentSum back to 0...
            currentSum += number # and start the addition process from this point forward
            maxSub = max(maxSub, currentSum) # update the maxSubArray to the maximum of itself and what was computed. so it takes the maximum portion and maximum values.
        return maxSub

