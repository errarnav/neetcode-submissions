class Solution:
    def canJump(self, nums: List[int]) -> bool:
        bad = set()
        def dfs(i):
            if i == len(nums) - 1:
                return True

            if i in bad:
                return False
            
            for _ in range(i + 1, i + nums[i] + 1):
                if dfs(_):
                    return True
            
            bad.add(i)
            return False
        
        return dfs(0)