class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        costs.sort(key=lambda x: x[1] - x[0])
        
        cost = 0
        n = len(costs) // 2
        
        # 前 n 個人去 B 市，後 n 個人去 A 市
        for i in range(n):
            cost += costs[i][1]      
            cost += costs[i + n][0]  
            
        return cost