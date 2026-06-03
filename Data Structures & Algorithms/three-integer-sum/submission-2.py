class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            
            if i > 0 and nums[i] == nums[i - 1]:
                    continue

            while l < r:
                current_sum = nums[l] + nums[r] + nums[i]

                if current_sum > 0:
                    r -= 1
                elif current_sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                        
        return res