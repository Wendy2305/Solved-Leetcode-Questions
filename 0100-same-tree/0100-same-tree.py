# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None: 
              return True 
            
        if (p is None and q is not None) or (p is not None and q is None): 
              return False
    
        if (p.left and not q.left) or (not p.left and q.left):
            return False
        if (p.right and not q.right) or (not p.right and q.right):
            return False
        
        if (p.val != q.val):
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)