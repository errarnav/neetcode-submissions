class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_streak = 0

        
        for num in nums:
            length = 0
            
            if num - 1 not in nums:
                length = 0
                while num + length in nums:
                    length += 1
                longest_streak = max(longest_streak, length)
            
            else:
                continue
            
        return longest_streak
            