class Solution:
    def jump(self, nums: List[int]) -> int:
        
        mem = {}
        INF = 10 ** 9
        n = len(nums)

        def dfs(i):
            if i >= n - 1:
                return 0

            if i in mem:
                return mem[i]
            if nums[i] == 0:
                mem[i] = INF
                return INF

            farthest = min(n - 1, i + nums[i])

            best = INF
            for j in range(i + 1, farthest + 1):
                best = min(best, 1 + dfs(j))

            mem[i] = best
            return best
        
        return dfs(0)

        
                