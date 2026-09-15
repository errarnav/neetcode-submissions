class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = [0] * (len(nums) + 1)

        mem[len(nums) - 1] = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            mem[i] = max(nums[i] + mem[i + 2], mem[i + 1])
        
        return mem[0]