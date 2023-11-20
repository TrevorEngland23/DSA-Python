from collections import Counter


# anagrams - hash table implemented from scratch.
def are_anagrams(s1, s2):
    # check to see if the strings are same length. if not, they won't have same number of characters, so they won't be anagrams regardless. 
    if len(s1) != len(s2):
        return False
    # create dictionaries to store character and count
    freq1 = {}
    freq2 = {}
    # loop through the first string
    for character in s1:
        # if there is a character found at the current index
        if character in freq1:
            # find the letter in the dictionary and increment its count by 1
            freq1[character] += 1
        else:
            # if the character was not in the freq dictionary, add it with a value of one
            freq1[character] = 1
    
    # same logic
    for character in s2:
        if character in freq2:
            freq2[character] += 1
        else:
            freq2[character] = 1

    # loop through the dictionary freq1
    for key in freq1:
        # compare each key against the freq2 keys. If the values don't match or there is a missing key in one of the dictionaries, return false, but if this loop completes, then everything matched perfectly, and the strings are indeed anagrams
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
    
    return True

# The short hand version of implementing the above code. starts with imporing Counter from collections

def are_anagrams2(s1, s2):
    if len(s1) != len(s2):
        return False
     # Counter function keeps track of how many times each character is used. If these two are equal, then True will be returned, but if not, then False will be returned. Same result.
    return Counter(s1) == Counter(s2)

# Test Test Test

t_string1 = "heart"
t_string2 = "earth"
print(are_anagrams(t_string1, t_string2))
print(are_anagrams2(t_string1, t_string2))
print()

t_string3 = "bobs"
t_string4 = "burgers"
print(are_anagrams(t_string3, t_string4))
print(are_anagrams2(t_string3, t_string4))

# worst case scenario, the time complexity is O(n), space complexity is also O(n) because each dictionary can contain up to n numbers

# another logical solution to solve the above... if anagram means that the strings have the same number of characters in a word, without being in the same order, then if we sort the srtrig alphabetically (or reverse alphabetically, we should be able to just compare the two strings at that point. if S1 deeply equals S2 at that point, then these strings are anagrams)

def are_anagrams3(s1, s2):
    # edge case
    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)

print(are_anagrams3(t_string1, t_string2))
print(are_anagrams3(t_string1, t_string4))

# the benefit of this method is that sorting in place is a O(n log n) operation, and you do that twice. So the time complexity with this method is O(n log n), and the space complexity is O(n)
