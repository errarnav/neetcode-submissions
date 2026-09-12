class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        sub = []

        def dfs(runningSum, start):
            if runningSum == target:
                res.append(sub[:])
                return

            for i in range(start, len(nums)):
                num = nums[i]
                if runningSum + num <= target:
                    sub.append(num)
                    dfs(runningSum + num, i)
                    sub.pop()
            
            return

        dfs(0, 0)
        return res
