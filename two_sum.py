# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?



from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {} # mapping value to the index of that value

        for index, value in enumerate(nums): # iterate through the list of numbers finding the index and value 
            diff = target - value # difference of the target number minus the current value. ex. target = 5, value = 1... 5-1 = 4. 4 is assigned to diff
            if diff in prev_map: # if diff is found in the hashmap (which is currently empty)
                return [prev_map[diff], index] # return the pair of indicies that add up to target
            prev_map[value] = index # if solution is not found, update the hashmap by storing the value and it's index in the hashmap
        return 
    
    # visual example 
    # TARGET = 7 ... Original List [2,4,6,3]
    # create empty hashmap... so what we are looking for is the value of 7 - the first value in list. so 7-2 = 5. we look at the hashmap for the value of 5, but it's not there because our hashmap is empty... So we now add the element to the hashmap. so 2 is added to the hashmap, at index 0.
    # now we move to the next number in the list. so now.. 5-4 is 1. we look in the hashmap for the value of 1, but we don't find it because currently the only thing that exists is 5. again, we add the value 4 to index 1, and move to the next number in the list. So far our hashmap looking like {2:0, 4:1,}.
    # we now look at 6. 7-6 = 1. is the value of 1 in our hashmap? No. so we add 6 at index 2, {2:0, 4:1, 6:2} and move on
    # 7-3 = 4. is the value of 4 in our hashmap? it is... find the index the value 4 is attached to, and return the pair of indicies that has values that add up to target.
    # in this case, the answer is [1, 3], 1 was found in the hashmap, and 3 is the current index of the value within the loop. 

    # time complexity is O(n), Space complexity O(n)
    # lets test

sol = Solution()

print(sol.two_sum([2,4,6,3], 7)) # answer is [1,3] as expected