class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ref = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 
            5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']}
        
        
        sub = []
        res = []
        def dfs(i):
            if i == len(digits):
                res.append(''.join(sub))
                return
            
            curDig = int(digits[i])
            for ch in ref[curDig]:
                sub.append(ch)
                dfs(i + 1)
                sub.pop()
            
            return
        
        if not digits:
            return res
        dfs(0)
        return res
