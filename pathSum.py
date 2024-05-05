
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum():
    if not root:
        return False
    
    
    if not root.left and not root.right:
        return targetSum == root.val


    targetSum -= root.val

    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)


