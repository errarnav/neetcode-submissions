class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        set1 = set(nums)
        
        res = 0
        for num in nums:
            if num - 1 in set1:
                continue
            cur = 1
            while (num + 1) in set1:
                cur += 1
                num += 1
            res = max(res, cur)

        return res