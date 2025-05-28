class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""       
        from collections import Counter       
        target_count = Counter(t)
        window_count = {}
        left, right = 0, 0
        required = len(target_count)
        formed = 0
        min_len = float("inf")
        ans = (0, 0)       
        while right < len(s):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1            
            if char in target_count and window_count[char] == target_count[char]:
                formed += 1
            
            while left <= right and formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    ans = (left, right)
                
                window_count[s[left]] -= 1
                if s[left] in target_count and window_count[s[left]] < target_count[s[left]]:
                    formed -= 1
                left += 1
            
            right += 1
        
        return "" if min_len == float("inf") else s[ans[0]: ans[1] + 1]