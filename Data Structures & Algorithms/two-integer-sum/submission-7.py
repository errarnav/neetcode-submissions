class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, n in enumerate(nums):
            if target - n not in hashMap:
                hashMap[n] = i
            else:
                return [hashMap[target - n], i]