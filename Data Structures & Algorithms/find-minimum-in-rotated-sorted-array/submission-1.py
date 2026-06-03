class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1 2 3 4 5 6
        # 6 1 2 3 4 5
        # 5 6 1 2 3 4
        # 4 5 6 1 2 3
        # 3 4 5 6 1 2
        # 2 3 4 5 6 1

        # 1 2 3 4 5
        # 5 1 2 3 4 
        # 4 5 1 2 3
        # 3 4 5 1 2
        # 2 3 4 5 1


        l = 0
        r = len(nums) - 1


# 4 5 6 1 2 3


        while nums[l] > nums[r]:
            m = l + ((r - l) // 2)
            
            if nums[r] > nums[m]:
                r = m
            
            else:
                l = m + 1

        return nums[l]
            
