class Solution:
    def rob(self, nums: List[int]) -> int:

        cache = {}
        n = len(nums)

        def dfs(k):
            if k >= n:
                return 0

            if k in cache:
                return cache[k]
            
            cache[k] = nums[k] + max(dfs(k + 2), dfs(k + 3))
            return cache[k]

        return max(dfs(0), dfs(1))
        