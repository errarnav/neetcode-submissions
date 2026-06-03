class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
        
    def helper(self, numss):
        if not numss:
            return 0
        if len(numss) == 1:
            return numss[0]

        dp = [0] * len(numss)

        dp[0] = numss[0]
        dp[1] = max(numss[0], numss[1])

        for i in range(2, len(numss)):
            dp[i] = max(dp[i - 1], dp[i - 2] + numss[i])

        return dp[-1]