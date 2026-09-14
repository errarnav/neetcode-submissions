class Solution:
    def trap(self, height: List[int]) -> int:
        
        lMax, rMax = [0] * len(height), [0] * len(height)
        l, r = 0, 0
        
        for i in range(1, len(height)):
            l = max(l, height[i - 1])
            lMax[i] = l

        for i in range(len(height) - 2, -1, -1):
            r = max(r, height[i + 1])
            rMax[i] = r

        res = 0
        cur = 0

        for i in range(len(height)):
            cur = min(lMax[i], rMax[i]) - height[i]
            if cur >= 0:
                res += cur
        
        return res


        