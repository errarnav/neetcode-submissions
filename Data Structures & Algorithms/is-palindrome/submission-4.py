class Solution:
    def isAlphaNumeric(self, char):
        val = ord(char)
        return (ord('a') <= ord(char) <= ord('z') or ord('A') <= ord(char) <= ord('Z') or ord('0') <= val <= ord('9'))
            
    def isPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1

        while l<r:
            while l<r and not self.isAlphaNumeric(s[l]):
                l += 1
            while r>l and not self.isAlphaNumeric(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True