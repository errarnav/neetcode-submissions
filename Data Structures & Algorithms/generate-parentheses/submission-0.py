class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        string = []

        def dfs(openCount, closeCount):
            if len(string) == 2*n:
                actual_string = ''.join(string)
                res.append(actual_string)
                return


            if openCount < n:
                string.append('(')
                dfs(openCount + 1, closeCount)
                string.pop()

            if openCount > closeCount:
                string.append(')')
                dfs(openCount, closeCount + 1)
                string.pop()

        dfs(0, 0)
        return res