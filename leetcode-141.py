class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)  # Convert the wordDict to a set for O(1) lookups
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: empty string is always valid
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[len(s)]

# Example usage:
solution = Solution()

# Example 1:
s = "leetcode"
wordDict = ["leet", "code"]
print(solution.wordBreak(s, wordDict))  # Output: True

# Example 2:
s = "applepenapple"
wordDict = ["apple", "pen"]
print(solution.wordBreak(s, wordDict))  # Output: True

# Example 3:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(solution.wordBreak(s, wordDict))  # Output: False