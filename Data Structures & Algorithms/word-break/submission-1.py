class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # applepen
        # return dfs(4) where dfs(i) returns true if that word is in the dictionary
        
        mem = {}
        wordSet = set(wordDict)

        def dfs(i):
            if i >= len(s):
                return True

            if i in mem:
                return mem[i]

            for k in range(i + 1, len(s) + 1):
                if s[i : k] in wordSet and dfs(k): 
                        mem[i] = True
                        return True 
            
            mem[i] = False
            return False
        
        return dfs(0)