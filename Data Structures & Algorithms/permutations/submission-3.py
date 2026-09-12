class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        used, res, sub = set(), [], []

        def dfs():

            if len(sub) == len(nums):
                res.append(sub[:])

            for num in nums:
                if num in used:
                    continue

                sub.append(num)
                used.add(num)

                dfs()

                sub.pop()
                used.remove(num)

        dfs()
        return res