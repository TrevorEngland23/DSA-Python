# Given a string "s" consisting of words and spaces, return the length of the last word in the string.

# Example: input -> s = "Hello World" , output -> 5

# Code Explanation: We are only concerned with spaces and letters, so we can split the string into a list, which by default splits the list by spaces. At this point, directly access the last element in the list, and find its length. Time = O(n), Space = O(1). per documentation, split has a time complexity of O(n), and since we are accessing the last element directly, we are using constant time for that operation. So worst case, O(n). For space, you may think that we are creating a list when we split the words, and that is true... but behind the scenes it is really returning a reference to the existing string using a generator to yield the words one by one (hence why split is O(n)), so this doesn't actually require any additional space for this list to exist. This is why we can use .split() directly on a string and print the result, rather than needing to create a new variable to hold the result for the changes to reflect.

def length_of_last_word(s):
    return len(s.split()[-1])


# test case: 

print(length_of_last_word("Hello World")) # output -> 5
print(length_of_last_word("Who's line is it anyway")) # output -> 6