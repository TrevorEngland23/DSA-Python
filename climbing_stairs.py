# You are climbing a staircase. It takes "n" steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# example: n = 2 -> output = 2
# explanation: there are two ways to climb to the top. 1.) 1 step + 1 step. 2.) 2 steps


# There are multiple ways to think of this problem. But as n is larger, to logic to this question gets hard to keep up with. You COULD think of this as a tree. Where the root is 0. you are given two options.. go up the stairs by 1 stair, or go up by 2 stairs. so the left side of every node represents 1 stair. the right side of the nodes represents two stairs. At th end, your leaf nodes that equal the target value each have a direct path relating back to the root node, which is 0 in this case. So each time your target value is found, add them up and that is the total number of possbilities... The problem with this? Very slow operation. o(2^n), n representing the height of the tree. 

# The optimal solution here is to rather think of this as an array. each step has it's own slice in this array. Start at the target step, so if your target number is 7, start at 7, which is the last element in this array. that element will have a default value of 1. Now look at 6, the next value. Give that number a 1 as well, because to get to step 7 from step 6, You can only do that by taking 1 step. now look at 3 in the array. to get from step 3 to step 5, you can do 2 steps, or 1+1 step. There are 2 total ways to get form 3 to 5. coincidentally, if you add the value of 4 (1) and 5 (1), you get 2. how many steps to get from 2 to 5? you can skip 2 then go up 1. you can go up all 3 individually. or you can go up one then skip two. there are 3 total ways from step 2. coincidentally, if you add the value of 3 (2) and the value of 4 (1), you get 3. 

# This algorithm holds true for any number of steps. So really, you can create two pointers. one starting at the end of the array, one starting at end - 1. each time you look at a new step, decrement the pointers respectively, and add the value of pointer 1 plus pointer 2 back to pointer 1. When you reach the end, pointer 1 value is the total number of possible solutions. This requires creating space though, which isn't the total optimal solution. Instead of creating an array to hold your values, You can just use a loop that executes target - 1 times (to account for starting at stair 0), and then using the algorithm. This requires no additonal space, and your runtime remains the same because regardless of which option you choose to use, you're having to loop through the array of stairs regardless, making both O(n) operations.






# COMPLETE OPTIMIZED SOLUTION... t(n): O(n) linear time, s(n): O(1)
def total_ways_to_climb(target):
    one,two = 1,1
    for i in range(target-1):
        tmp = one
        one += two
        two = tmp
    return one


print(total_ways_to_climb(3))