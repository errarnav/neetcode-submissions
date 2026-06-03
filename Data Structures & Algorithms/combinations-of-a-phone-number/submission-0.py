class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        loc = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'],
         5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 
         8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        
        res = []
        options = []
        
        if not digits:
            return []
        
        for i in digits:
            options.append(loc[int(i)])

        sub = []

        def dfs(i):
            if i == len(digits):
                string = ''.join(sub)
                res.append(string)
                return

            for k in range(len(options[i])):
                sub.append(options[i][k])
                dfs(i + 1)
                sub.pop()

        dfs(0)

        return res

            
