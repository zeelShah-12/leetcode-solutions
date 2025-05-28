class Solution:
    def reverse(self, x: int) -> int:
        int_min, int_max = -2**31, 2**31 - 1  
        res = 0  
        sign = -1 if x < 0 else 1  
        x = abs(x)  
        while x:
            digit = x % 10  
            x //= 10  
            if res > (int_max - digit) // 10:
                return 0  
            res = res * 10 + digit  

        return sign * res  