from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        H = []
        for num in nums:
            if len(H) < k:
                heapq.heappush(H, num)
            elif num > H[0]:
                heapq.heapreplace(H, num)
        return H[0]