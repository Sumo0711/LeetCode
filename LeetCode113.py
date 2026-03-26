# Definition for a binary tree node.
from typing import Optional
from typing import List
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(node, Sum, path):
            if not node:
                return
            path.append(node.val)

             # 判斷是否為葉子節點
            if not node.left and not node.right and node.val == Sum:
                res.append(list(path))
            
            # 往左、右子樹遞迴
            dfs(node.left, Sum - node.val, path)
            dfs(node.right, Sum - node.val, path)
            
            # 回溯 
            path.pop()
        
        dfs(root, targetSum, [])
        return res