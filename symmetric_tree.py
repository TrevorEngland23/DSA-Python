# Given a binary tree "root", check if it is symmetric around its center (a mirror of itself)

# So, imagine a piece of paper folded down the middle. There's a crease down the center of the paper. If you can fold that paper in half, and the left side of the paper lines up with the right side of the paper, you have a symmetric tree. However, if the nodes do not line up, the tree is not symmetric. 

# given two trees, the root must have the same value on both trees. if they are, use recursion to check the rest of the subtrees

# function logic to check for symmetric trees
def are_symmetric(root1, root2):
    # check to see is the trees exist
    if root1 is None and root2 is None:
        return True
    # if one exists but the other doesn't or if they have different root value.. return false
    elif ((root1 is None) != (root2 is None)) or root1.val != root2.val:
        return False
    else:
        # both trees do exist, and have the same root values... check their subtrees
        return are_symmetric(root1.left, root2.right) and are_symmetric(root1.right, root2.left)
    
    # depth first search 
def is_symmetric(root): # main root
    if root is None: 
        return True
    return are_symmetric(root.left, root.right) # recursion to check for symmetric trees

# time complexity is O(n), n being the number of nodes, space complexity is O(nlogn)