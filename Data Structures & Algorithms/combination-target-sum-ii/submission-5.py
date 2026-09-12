class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        candidates.sort()

        def dfs(starting, runSum):
            if runSum == target:
                print(sub)
                res.append(sub[:])
                return 

            for i in range(starting, len(candidates)):
                if i > starting and candidates[i] == candidates[i - 1]:
                    continue
                
                num = candidates[i]
                
                if runSum + num > target:
                    break
                
                sub.append(num)
                dfs(i + 1, runSum + num)
                sub.pop()
        
            return 
        
        dfs(0, 0)
        return res