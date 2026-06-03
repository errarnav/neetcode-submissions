class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []

        for i in range(len(nums)):
            target = nums[i] * -1

            for k in range(i + 1, len(nums) - 1, 1):
                if target - nums[k] in nums[k + 1 :]:
                    new_list = sorted([nums[i], nums[k], target - nums[k]])
                    if new_list in final:
                        continue
                    else:
                        final.append(new_list)

        return final