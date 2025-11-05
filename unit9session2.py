from collections import deque
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def level_order(root):
    explored = []
    if not root:
        return []
    queue = deque([root])
    while queue:
        current = queue.popleft()
        explored.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return explored

test = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
#test = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), 5)
print(level_order(test)) #conclusion: i must work on my inputting of treenodes
