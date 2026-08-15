class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []
        n = len(temperatures)

        for i in range(n - 1, -1, -1):
            if not stack:
                stack.append(i)
                continue
            
            
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            
            if stack:
                res[i] = stack[-1] - i
            
            stack.append(i)
        
        return res