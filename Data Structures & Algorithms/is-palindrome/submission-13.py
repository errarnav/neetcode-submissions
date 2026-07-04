class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNumeric(a):
            return (ord('a') <= ord(a) <= ord('z')) or (ord('A') <= ord(a) <= ord('Z')) or (ord('0') <= ord(a) <= ord('9'))

        l, r = 0, len(s) - 1
       
        while l <= r:
            while l < r and not isAlphaNumeric(s[l]):
                l += 1
            while r > l and not isAlphaNumeric(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True
        