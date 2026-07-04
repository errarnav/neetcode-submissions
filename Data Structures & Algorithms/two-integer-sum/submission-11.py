class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        index = 0
        for num in nums:
            if target - num not in seen:
                seen[num] = index
                index += 1
            else:
                return [seen[target - num], index]