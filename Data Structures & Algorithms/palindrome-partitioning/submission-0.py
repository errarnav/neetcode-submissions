class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        sub = []

        
        def isValidPalindrome(word, l, r):
            while l < r:
                if word[l] == word[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True



        def dfs(i, j):

            if j >= len(s):
                if i == j:
                    res.append(sub.copy())
                return

            if isValidPalindrome(s, i, j):
                sub.append(s[i : j + 1])
                dfs(j + 1, j + 1)
                sub.pop()
            
            j += 1
            dfs(i, j)

        dfs(0, 0)
        return res
