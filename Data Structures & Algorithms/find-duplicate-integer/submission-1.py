class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):  # 1 3 4 2 2

            index_to_mark = abs(nums[i]) - 1

            if nums[index_to_mark] < 1:
                return index_to_mark + 1
            
            nums[index_to_mark] *= -1


