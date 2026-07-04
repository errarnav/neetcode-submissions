class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        l, r = 0, 0
        res = 0

        for r in range(len(prices)):
            if prices[r] <= prices[l]:
                l = r
            else:
                cur = prices[r] - prices[l]
                res = max(cur, res)
            
        
        return res