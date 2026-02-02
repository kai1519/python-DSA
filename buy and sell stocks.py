from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        B = prices[0]      
        profit = 0         

        for i in range(1, len(prices)):
            S = prices[i]  

            if S > B:
                profit = max(profit, S - B)
            else:
                B = S    

        return profit

        
   