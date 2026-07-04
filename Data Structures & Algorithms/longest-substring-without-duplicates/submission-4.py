class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        exist = set()

        l, r = 0, 0

        res = 0
        for r in range(len(s)):
            while s[r] in exist:
                exist.remove(s[l])
                l += 1
            cur = r - l + 1
            res = max(res, cur)
            exist.add(s[r])

        return res

            