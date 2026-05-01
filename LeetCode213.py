class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        def rob_simple(houses: list[int]) -> int:
            prev2 = 0
            prev1 = 0
            
            for money in houses:
                current = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = current
                
            return prev1

        max1 = rob_simple(nums[:-1])
        max2 = rob_simple(nums[1:])
        
        return max(max1, max2)