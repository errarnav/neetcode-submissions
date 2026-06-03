class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 3 5 6 0 1 2
        # 6 0 1 2 3 5
        # 5 6 0 1 2 3

        l = 0
        r = len(nums) - 1

        while nums[l] > nums[r]:

            m = l + ((r - l ) // 2)

            if nums[l] <= nums[m]:
                l = m + 1

            else:
                r = m
            
        inflection_index = l

        # first binary search

        l1 = 0
        r1 = inflection_index - 1

        while l1 <= r1:
            
            m = l1 + ((r1 - l1) // 2)

            
            if target < nums[m]:
                r1 = m - 1
            elif target > nums[m]:
                l1 = m + 1
            else:
                return m


        # second binary search

        l2 = inflection_index
        r2 = len(nums) - 1

        while l2 <= r2:
            
            m = l2 + ((r2 - l2) // 2)

            
            if target < nums[m]:
                r2 = m - 1
            elif target > nums[m]:
                l2 = m + 1
            else:
                return m

        
        return -1






