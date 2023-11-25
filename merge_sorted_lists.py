# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

# example given: input: 1 -> 2 -> 4   1 -> 3 -> 4
# output: 1 -> 1 -> 2 -> 3 -> 4 -> 4




class Solution:
    def merge(self, list1, list2):
        made_up_node = ListNode() # create a node to reference
        tail = made_up_node # set the tail to be this made up node

        while len(list1) and len(list2) > 0: # if there are still values in both lists
            if list1.val < list2.val: # if the value of list1 is less than the value of list2
                tail.next = list1 # put that value behind the current tail
                list1 = list1.next # look at the next value in list1
            else:
                tail.next = list2 # otherwise, the value from list2 is appended
                list2 = list2.next # look at the next value in list2
            tail = tail.next # new tail is the value that was just appended

        if len(list1) > 0: # if there are still values in list1 at this point
            tail.next = list1 # copy the values down
        elif len(list2) > 0: # if there are still values in list2 at this point
            tail.next = list2 # copy the values down 
        

        return made_up_node.next # returns the head of the merged list.
        
