from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window_s = 2 * k + 1
        res = [-1] * n 
        
        if n < window_s:
            return res
        
        Sum = sum(nums[:window_s])
        
        res[k] = Sum // window_s
        
        for i in range(k + 1, n - k):
            Sum = Sum + nums[i + k] - nums[i - k - 1]
            res[i] = Sum // window_s
            
        return res