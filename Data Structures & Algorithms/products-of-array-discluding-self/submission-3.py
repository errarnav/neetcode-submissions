class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix_multiples = []
        suffix_multiples = [1]*(len(nums))

        for i in range(len(nums)):
            if len(prefix_multiples) == 0:
                prefix_multiples.append(1)
            else:
                prefix_multiples.append(prefix_multiples[i - 1] * nums[i - 1])

        for i in range(len(nums) -1, -1 , - 1):
            if i == len(nums) - 1:
                suffix_multiples[i] == 1
            else:
                suffix_multiples[i] = suffix_multiples[i + 1] * nums[i + 1]

        final_list = []

        for i in range(len(nums)):
            final_list.append(prefix_multiples[i] * suffix_multiples[i])

        return final_list
            