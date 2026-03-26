# Definition for a binary tree node.
from typing import Optional
from collections import deque
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        ans = 0
        
        while queue:
            sum = 0
            # 當前層的節點數量
            size = len(queue)
            
            for _ in range(size):
                node = queue.popleft()
                sum += node.val
                # 將下一層的節點加入
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans = sum
            
        return ans