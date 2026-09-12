class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        sub, res = [], []

        def dfs(starting):
            res.append(sub[:])

            
            for i in range(starting, len(nums)):
                if i > starting and nums[i] == nums[i - 1]:
                    continue

                sub.append(nums[i])
                dfs(i + 1)
                sub.pop()

        dfs(0)
        return res