class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        AllNeg = True
        for num in nums:
            if num > 0:
                AllNeg = False
                break

        curSum = 0
        r = 0
        res = 0

        for r in range(len(nums)):
            if nums[r] + curSum > 0:
                curSum += nums[r]
                res = max(res, curSum)
            else:
                curSum = 0
        
        return res if not AllNeg else max(nums)