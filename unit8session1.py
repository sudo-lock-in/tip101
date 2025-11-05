class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
left = TreeNode(4)
right = TreeNode(6)
# center = TreeNode(10, left, right)
center = TreeNode(10, 4, 6)

def check_tree(root):
    if root.left + root.right == root.val:
        return True
    return False

# def check_tree(root):
#     if root.left + root.right == root.val:
#         return True
#     return False

def check_tree(root):
    if root.left == None:
        if root.right == root.val:
            return True
        else: 
            return False
    elif root.right == None:
        if root.left == root.val:
            return True
        else: 
            return False
    elif root.left + root.right == root.val:
        return True
    return False


# def left_most(root):
#     curr = root
#     while curr.left:
#         curr = curr.left
#     return curr.val



#recursive mode
def left_most(root):
    if root is None:
        return None
    if root.left == None:
        return root.val
    return left_most(root.left) 

test = TreeNode(1, None, TreeNode(2, TreeNode(3)))
test = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), 5)
print(left_most(test))
