class Solution:
    def isHappy(self, n: int) -> bool:
        
        sum = 0
        visit = set()

        while n != 1 and n not in visit:
            visit.add(n)
            sum = 0
            for i in str(n):
                i = int(i)
                sum += i * i

            n = sum
            
        
        return n == 1