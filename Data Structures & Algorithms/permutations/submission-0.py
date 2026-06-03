class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        perms = [[]]

        for n in nums:
            new_perms = []
            for p in perms:
                for index in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(index, n)
                
                    new_perms.append(p_copy)

            perms = new_perms

        return perms
