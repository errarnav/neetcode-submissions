class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # first we will find the deflection point - the index of smallest element
        while l < r:
            m = l + (r - l)//2
            if nums[r] > nums[m]:
                r = m
            else:
                l = m + 1
        
        inflection = l
        r = inflection - 1
        l = 0
        print(l, r)
        while l <= r:
            m = l + (r - l)//2
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return m

        l = inflection
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l)//2
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return m
        
        return -1
