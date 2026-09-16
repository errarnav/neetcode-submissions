class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen, res = 1, s[0]
        for i in range(len(s)):
            # odd length palindromes, treat current character as middle
            curLen = 1
            l, r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curLen += 2

                if curLen > resLen:
                    res = s[l : r + 1]
                    resLen = curLen

                l -= 1
                r += 1

            
            # even length palindromes, treat i and i + 1 as starting pointers
            l, r = i, i + 1
            curLen = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curLen += 2

                if curLen > resLen:
                    res = s[l : r + 1]
                    resLen = curLen

                l -= 1
                r += 1

        return res

        


    
