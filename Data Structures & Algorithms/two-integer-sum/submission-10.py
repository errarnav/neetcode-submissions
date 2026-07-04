class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        visit = {}

        index = 0
        for num in nums:
            if target - num not in visit:
                visit[num] = index
                index += 1
            else:
                return [visit[target - num], index]