class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        a1=int(a,2)
        b1=int(b,2)
        sum1=a1+b1
        return bin(sum1)[2:]