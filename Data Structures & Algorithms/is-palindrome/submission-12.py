class Solution:
    def isAlphaNumeric(self, char):
        # 48 --> 39, 65 --> 90, 97 --> 122

        if ord('a') <= ord(str(char)) <= ord('z') or ord('A') <= ord(str(char)) <= ord('Z') or ord('0') <= ord(str(char)) <= ord('9'):
            return True
        else:
            return False
            
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not self.isAlphaNumeric(s[l]):
                l += 1
            while r > l and not self.isAlphaNumeric(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True



