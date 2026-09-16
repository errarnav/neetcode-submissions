class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        lenS = len(s)
        
        for i in range(lenS):
        
            # odd length
            l, r = i, i
            while l >= 0 and r < lenS and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            # even length
            l, r = i, i + 1
            while l >= 0 and r < lenS and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res
