class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [0] * n
        mem[n - 1] = 1
        if n > 1:
            mem[n - 2] = 2

        for i in range(n - 3, -1, -1):
            mem[i] = mem[i + 1] + mem[i + 2]
        
        return mem[0]
