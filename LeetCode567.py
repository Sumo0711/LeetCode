from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        s1_num = Counter(s1)
        window_num = Counter(s2[:n1])
        
        if s1_num == window_num:
            return True
   
        for i in range(n1, n2):
            new = s2[i]          
            old = s2[i - n1]    
            
            window_num[new] += 1
            window_num[old] -= 1
            
            if window_num[old] == 0:
                del window_num[old]
            
            if s1_num == window_num:
                return True
                
        return False