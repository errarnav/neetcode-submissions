class Solution:
   
    # lets design the validity function

    def isValid(self, piles: List[int], h: int, rate: int) -> bool:
        total = 0
        for i in range(len(piles)):
            time = -(-piles[i] // rate)
            total += time

        if total <= h:
            return True
        else:
            return False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        # 1 2 3 4 | target time = 9 || upper bound for eating rate = biggest pile

        l = 1
        r = piles[-1]   # 1 2 3 4 5

        while l <= r:
            m = l + ((r - l)//2)

            if self.isValid(piles, h, m):
                r = m - 1
                lastValid = m
            else:
                l = m + 1

        return lastValid


