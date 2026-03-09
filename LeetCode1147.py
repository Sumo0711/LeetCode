class Solution:
    def longestDecomposition(self, text: str) -> int:
        res = 0
        Lstr, Rstr = "", ""
        Lidx, Ridx = 0, len(text) - 1
        
        while Lidx < Ridx:
            Lstr += text[Lidx]
            Rstr = text[Ridx] + Rstr
            
            # 貪婪法：一旦發現左右對稱，立即切割
            if Lstr == Rstr:
                res += 2
                Lstr, Rstr = "", ""
            
            Lidx += 1
            Ridx -= 1
            
        if len(text) % 2 == 1 or Lstr != "":
            res += 1
            
        return res