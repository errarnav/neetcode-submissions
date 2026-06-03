class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        post_fix_array = [1] * len(nums)
        pre_fix_array = [1] * len(nums)

        results_list = [1] * len(nums)

        multiplier = 1
        for i in range(len(nums)):
            if i == 0:
                pre_fix_array[i] = 1
            else:
                multiplier = multiplier * nums[i - 1]
                pre_fix_array[i] = multiplier
        
        multiplier = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                post_fix_array[i] = 1
            else:
                multiplier = nums[i + 1] * multiplier
                post_fix_array[i] = multiplier
        
        for i in range(len(nums)):
            results_list[i] = post_fix_array[i] * pre_fix_array[i]

        return results_list
                