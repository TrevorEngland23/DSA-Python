# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems conected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers respresenting the amount of money of each house, determine the max amount of money you can rob tonight without alerting the police.

# example given: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1, where money = 1, and rob house 3 (where money = 3)

# INITIAL THOUGHTS: brute force solution is to iterate through the list twice, once by starting at index 0 and looking at every other number, the next loop starting at index 1, looking at every number. add all the numbers up on each loop, then compare the two sums. Whichever sum is higher, those are the houses you should rob. The flaw in this logic though, is what if house 1 is 50, house 2 is 10, house 3 is 0, and house 4 is 10000? In this case house 1 and house 4 are the houses we want to rob to have the most successful night, but the two options above will not get us to that solution. CON: this is a O(n^2) operation, and it would be better to get the solution down to linear time.

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
       rob_house1 = 0 # first house robbed
       rob_house2 = 0 # next house robbed

       for n in nums: # for numbers in nums
           tmp = max(n + rob_house1, rob_house2) # ...? revisit later. stuck on understanding the logic behind this.
           rob_house1 = rob_house2 # update the state. now THAT house is considered 2 houses ago
           rob_house2 = tmp # THIS house is considered the last house robbed
       return rob_house2 # at the end, the total number will be rob_house2.