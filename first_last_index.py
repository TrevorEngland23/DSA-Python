# Given a sorted array of integers "arr" and an integer "target", find the index of the first and last positions of target in arr. If target can't be found in arr, return [-1, -1]

def first_last_index(arr, target):
    # traverse the array
    for i in range(len(arr)):
        # if the value of the index is the same as the specified target
        if arr[i] == target:
            # the index is put into the variable "start" 
            start = i
            # basically, this is keeps going through the end of the array and whatever i is at the end is the last occurence.. array is sorted so they will appear consecutively
            while i+1 < len(arr) and arr[i+1] == target:
                i += 1
                return [start, i] # i now represents the lat occurence of the condition specified (last index where target was found)
    return [-1, -1] # if the for loop ends without returning the result, then target was never in the arr of integers

# time complexity O(n), space complexity o(1). Solution uses linear search
# since the array is sorted, we could use binary search... 

def find_start(arr, target):
    if arr[0] == target:
        return 0
     # create left and right boundaries.. start and end 
    start = 0
    end = len(arr) - 1  
    
    # while there is at least one element in the array
    while start <= end: 
        mid = (start+end)//2 #integer division, rounds down to previous integer

        # if the value of mid is the target and the value of mid - 1 is less than the target, then that is the first occurence of the target so function is complete, return mid
        if arr[mid] == target and arr[mid-1] < target:
            return mid
        # otherwise if value is less than target, we can exclude everything that came before that value since the integers sorted, so mid+1 is the new starting point
        elif arr[mid] < target:
            start = mid+1
        else:
            # if the value was greater than the target, we can exclude anything past that point, and make mid-1 the new end boundary for searching
            end = mid-1
    # if the while loop doesn't return anything, target was never found in arr, so return -1
    return -1

def first_and_last(arr, target): # one way, not the best way. i think this is T(n) = O(n) at worst
    # if arr is empty, then return -1 for first and last occurence
    if len(arr) == 0:
        return [-1, -1]
    # if there was no starting point, there won't be an ending point, so return -1 for both
    start = find_start(arr, target)
    if start == -1:
        return [-1, -1]
    # whatever value was returned from find_start is the start point, also assign it to the end point for now
    end = start
    # as long as we are looking at a value in the array AND that value matches the target
    while end+1 < len(arr) and arr[end+1] == target:
        # keep traversing and add one to the index number of end
        end +=1 
        # return the start and end index
    return [start, end]

def find_end(arr, target):
    if arr[-1] == target:
        return len(arr)-1
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target and arr[mid+1] > target:
            return mid
        elif arr[mid] > target:
            right = mid+1
        else:
            left = mid-1
    return -1

def first_and_last2(arr, target): # time complexity here is O(n log n), space complexity O(1), since we are only using int variables
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1, -1]
    start = find_start(arr, target)
    end = find_end(arr, target)
    return [start, end]