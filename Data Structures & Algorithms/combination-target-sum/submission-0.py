class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        curr = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if i >= len(nums) or total > target:
                return

            new = curr.copy()
            new.append(nums[i])
            dfs(i, new, total + nums[i])

            new.pop()
            dfs(i + 1, new, total)

        dfs(0, curr, 0)
        return res