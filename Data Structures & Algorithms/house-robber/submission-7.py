class Solution:
    def rob(self, nums: List[int]) -> int:
        two_away, one_away = 0, 0

        for money in reversed(nums):
            current = max(two_away + money, one_away)
            two_away = one_away
            one_away = current

        return current