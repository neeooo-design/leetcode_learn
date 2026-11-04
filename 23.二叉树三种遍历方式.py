# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res =[]
        def f(node:Optional[TreeNode]):
            if node==None:
                return
            res.append(node.val)
            f(node.left)
            f(node.right)
        f(root)
        return res
        