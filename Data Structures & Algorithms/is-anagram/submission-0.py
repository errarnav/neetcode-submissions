class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        for char in s:
            if char not in dict_s.keys():
                dict_s[char] = 1
            else:
                dict_s[char] += 1
        dict_t = {}
        for char in t:
            if char not in dict_t.keys():
                dict_t[char] = 1
            else:
                dict_t[char] += 1

        return (dict_s == dict_t)