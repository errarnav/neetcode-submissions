class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}

        def dfs(k):
            if k >= len(nums):
                return 0

            if k in mem:
                return mem[k]
            
            mem[k] = max(dfs(k + 1), nums[k] + dfs(k + 2))

            return mem[k]

        return dfs(0)