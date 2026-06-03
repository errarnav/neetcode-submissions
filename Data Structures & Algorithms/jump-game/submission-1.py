class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        mem = {}

        def dfs(i):
            
            if i >= len(nums) - 1:
                return True
            
            if nums[i] == 0:
                mem[i] = False
                return False

            if i in mem:
                return mem[i]

            farthest = nums[i] + i
            for j in range(i + 1, farthest + 1):
                if dfs(j):
                    mem[i] = True
                    return True
            
            return False
        
        return dfs(0)
