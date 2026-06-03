class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        
        while l < r:

            m = l + ((r - l) // 2)

            if target < nums[m]:
                r = m
            elif target > nums[m]:
                l = m + 1
            else:
                return m
        if l == r and nums[r] == target:
            return r
        return -1