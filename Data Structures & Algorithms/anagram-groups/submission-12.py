class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for string in strs:
            list1 = [0] * 26
            for i in string:
                list1[ord(i) - ord('a')] += 1

            list1 = tuple(list1)
            if list1 not in res:
                res[list1] = [string]
            else:
                res[list1].append(string)

        result = []
        for key, value in res.items():
            result.append(value)

        return result