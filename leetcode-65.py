class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        has_num = has_dot = has_exp = False

        for i, c in enumerate(s):
            if c.isdigit():
                has_num = True  
            elif c in "+-":
                if i > 0 and s[i - 1] not in "eE":
                    return False  
            elif c == ".":
                if has_dot or has_exp:
                    return False  
                has_dot = True  
            elif c in "eE":
                if has_exp or not has_num:
                    return False  
                has_exp = True
                has_num = False  
            else:
                return False  

        return has_num  