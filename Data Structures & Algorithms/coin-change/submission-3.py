class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {0 : 0}

        for i in range(1, amount + 1):
            mem[i] = float('inf')
            for coin in coins:
                if i - coin in mem:
                    mem[i] = min(mem[i], mem[i - coin] + 1)
            
        return mem[amount] if mem[amount] != float('inf') else -1
                    

