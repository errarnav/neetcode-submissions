class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = [0]*26

        for element in s:
            index = ord(element.lower()) - 97
            list_s[index] += 1
        
        list_t = [0]*26

        for element in t:
            index = ord(element.lower()) - 97
            list_t[index] += 1

        if list_t == list_s:
            return True
        else:
            return False