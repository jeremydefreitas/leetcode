# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        
        def dfs(node, curSum):
            if not node:
                return 0
            
            curSum = curSum * 10 + node.val

            if not node.left and not node.right:
                return curSum

            return dfs(node.left, curSum) + dfs(node.right, curSum)

        
        return dfs(root, 0)
            
            
            


            

            
        