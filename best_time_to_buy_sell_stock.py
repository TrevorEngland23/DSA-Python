# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# thoughts: generally when dealing with stock, the overall goal is to buy low and sell high. So this sounds like we will be dealing with a min/max situation to some degree.

# so an example... [9, 5, 1, 2, 1, 5, 8, 5] --> each item in the array here represents a price based on the day. so, day one is 900, day two is 500, day 3 is 100, etc. In this case, the it doesn't make sense to buy when the price is 900 dollars on day 1. If we wait until day 3, the price drops to 100, which seems like the best time to buy. Then, we ideally want to sell when the price is at 800, which would give us a 700 dollar profit. Things to consider... if you take the min and max of the array and subtract, you would actually get 9-1=8. but we cannot go back in time to sell this stock, time only moves in one direction. 

# We can use the two pointers solution to account for time and solve this problem, T(n) = O(n), S(n): O(1)

def max_profit(prices):
    l,r = 0, 1 # create two pointers (left = buy and right = sell) and initialize the left to 0 and right to 1

    max_profit = 0 # originally, the profit is 0 because no transaction has been made
    while r < len(prices): # while the the pointer has not passed the last value in list 
        if prices[l] < prices[r]: # if the transaction would be profitable... if the buying price is less than the selling price
            profit = prices[r] - prices[l] # math to find the calculated profit
            max_profit = max(max_profit, profit) # compares the maxProfit value and the profit from the current potential transacation. If the profit is greater than the current max profit, then the max profit is now equal to the profit.
        else:
            l = r # if we found a value that is less than the current left pointer, move the left pointer to where the right pointer is
        r += 1 # regardless of what happens, the right pointer continues to increment by one to traverse the list, making this operation an O(n) operation.

    return max_profit # return the maxProfit found


# TEST 

print(max_profit([9,5,1,2,1,5,8,5])) # 7
print(max_profit([10000000000, 1, 0, 1, 0, 99])) # 99