class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def houseRob(l1):
            cur, one_away, two_away = 0, 0, 0
            for money in reversed(l1):
                cur = max(money + two_away, one_away)
                two_away = one_away
                one_away = cur
            
            return cur

        if len(nums) == 1:
            return nums[0]
        return max(houseRob(nums[1:]), houseRob(nums[:len(nums) - 1]))

        