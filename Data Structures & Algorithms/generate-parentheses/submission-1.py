class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        sub = []
        res = []

        def dfs(nOpen, nClosed):
            if len(sub) == 2 * n:
                res.append(''.join(sub))
                return

            
            if nOpen > nClosed:
                sub.append(')')
                dfs(nOpen, nClosed + 1)
                sub.pop()
            
            if nOpen < n:
                sub.append('(')
                dfs(nOpen + 1, nClosed)
                sub.pop()
                
            
            
            return

        dfs(0, 0)
        return res
                