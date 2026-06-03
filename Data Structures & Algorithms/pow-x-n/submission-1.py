class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1


            a = helper(x, n // 2)
            if n % 2 == 0:
                return a * a
            if n % 2 == 1:
                return a * a * x

            if n == 1:
                return x

        res = helper(x, abs(n))
        
        return res if n >= 0 else 1 / res

        