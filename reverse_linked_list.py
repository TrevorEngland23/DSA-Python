# Reverse a singly linked list

# Input: 1 -> 2 -> 3 -> 4 -> 5
# Output: 5 -> 4 -> 3 -> 2 -> 1

# things to note: singly linked lists cannot be bi-directional. You can only visit one node at a time, meaning you cannot iterate over a singly linked list in the same manneras lists or arrays. 

# Iterative Solution: Use two pointers
# p1 is null before head, p2 is head. rotate the pointer to point to null from head. shift p1 to head, shift p2 to next node. keep doing this. at the end, p2 points to null, p1 points to the new head, return the new head 

# Doesn't make sense to me...

def reverseList(head): # Tn  = O(n), sn = O(1)
    prev, curr =  None, head # in python use None instead of null...

    while curr: # while not null
        next = curr.next # moves over one node
        curr.next = prev # ?
        prev = curr # 
        curr = next
   
    return prev

# recursive solution tn = O(n) sn O(n)

def recursive(head):

    if not head:
        return None
    
    new_head = head
    if head.next:
        new_head = reverseList(head.next)
        head.next.next = head
    head.next = None

    return new_head


