class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict1 = {}
        
        for i, n in enumerate(numbers):
            if target - n not in dict1:
                dict1[n] = i + 1
            else:
                return [dict1[target - n], i + 1]