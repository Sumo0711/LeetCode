from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1
        
        while L < R:
            sum = numbers[L] + numbers[R]
            
            if sum == target:
                return [L + 1, R + 1]
            
            if sum < target:
                L += 1
            else:
                R -= 1
                
        return []