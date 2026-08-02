class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        if target == nums[l]:
            return l
        if target == nums[r]:
            return r

        while l < r:
            m = l + (r - l) // 2

            if target < nums[m]:
                r = m
            elif target > nums[m]:
                l = m + 1
            else:
                return m
        
        
        
        return -1