import math

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums

    # 把問題切成很多個子問題
    def merge_sort(self, A, p, r): # A 原始陣列 p 起始點 r 結束點 
        if p >= r: 
            return
        
        q = (p + r) // 2 # 切一半的地方
        
        self.merge_sort(A, p, q) # 處理左半
        
        self.merge_sort(A, q + 1, r) # 處理右半
        
        self.merge(A, p, q, r) # 合併

    def merge(self, A, p, q, r):
        # Python [start:end] 是左閉右開，所以 end 要 +1
        left = A[p : q + 1]
        right = A[q + 1 : r + 1]
        
        i = j = 0    # i 看左 j 看右
        k = p        # K 新陣列要擺的位置
        
        # 開始合併
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
            
        # 處理剩餘元素
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1