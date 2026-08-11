class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def canEat(rate, piles, hoursGiven):
            hoursUsed = 0
            for pile in piles:
                hoursUsed += -(-pile//rate)
                if hoursUsed > hoursGiven:
                    return False
            
            return True
        
        while l < r:
            m = l + (r - l)//2
            if canEat(m, piles, h):
                r = m
            else:
                l = m + 1
        
        return l
                
