class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        cur = 0

        for num in nums:
            cur += num
            if cur > 0 :
                res = max(cur, res)
            else:
                cur = 0

        return res