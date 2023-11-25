# if the list is sorted, you can use two pointers. T(n) = O(n) at worst, S(n) = O(1), which improves from the hashmap method of O(n). Note that the list has to be sorted in order to use this approach

from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        p1 = 0 # create the first (left) pointer
        p2 = len(nums)-1 # create the second (right) pointer

        while p1 < p2: # basically while there are still numbers to check. If they are ever at the same value / cross each other, then there is no valid answer in the array
            # if the two values add up to target, then return the two indicies.
            current_sum = nums[p1] + nums[p2]

            if current_sum > target: # if the sum was greater than our target...
                p2 -= 1 # move the right pointer to the left
            elif current_sum < target: # if the sum was less than the target...
                p1 += 1 # move the left pointer to the right
            else: # if the two values exactly equal the target number...
                return [p1, p2] # return the indicies for the two values in a pair
