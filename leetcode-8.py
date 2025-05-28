class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  
        if not s:
            return 0
        sign = 1
        index = 0
        if s[0] in ['-', '+']:  
            sign = -1 if s[0] == '-' else 1
            index += 1
        result = 0
        while index < len(s) and s[index].isdigit():  
            result = result * 10 + int(s[index])
            index += 1
            if sign * result < -2**31:
                return -2**31
            if sign * result > 2**31 - 1:
                return 2**31 - 1
        return sign * result