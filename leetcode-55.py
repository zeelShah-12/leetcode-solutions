from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        for i in range(len(nums)):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + nums[i])
            if max_reachable >= len(nums) - 1:
                return True
        return False
solution = Solution()
nums = [2, 3, 1, 1, 4]
print(solution.canJump(nums))  
nums = [3, 2, 1, 0, 4]
print(solution.canJump(nums))  