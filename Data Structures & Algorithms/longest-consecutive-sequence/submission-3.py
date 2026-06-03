class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        maxStreak = 0
        for element in num_set:
            if element - 1 in num_set:
                continue

            # moving forward we know that this element is a starting position for a streak
            current_streak = 1

            while element + 1 in num_set:
                element += 1
                current_streak += 1
            
            maxStreak = max(maxStreak, current_streak)

        
        return maxStreak
