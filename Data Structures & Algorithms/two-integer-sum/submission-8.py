class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        index = 0
        for element in nums:
            if (target - element) in dict1.keys():
                return [dict1[target - element], index]
            else:
                dict1[element] = index
            index += 1
        