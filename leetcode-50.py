class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x, n = 1 / x, -n      
        res = 1
        while n:
            if n % 2:
                res *= x
            x *= x
            n //= 2
        return res





