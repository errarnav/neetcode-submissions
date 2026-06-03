class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        for element in nums:
            if not res:
                res.append([])
                res.append([element])

            else:
                lenRes = len(res)
                for i in range(lenRes):
                    new_list = res[i][:]
                    new_list.append(element)

                    res.append(new_list)

        return res

