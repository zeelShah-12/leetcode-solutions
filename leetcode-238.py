class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        dp = [1]*len(nums)
        for index in range(1,len(nums)):
                dp[index]=dp[index-1]*nums[index-1]
        print (dp)
        right = 1
        for index in range(len(nums)-1,-1,-1):
                dp[index] *= right
                right *=nums[index]
        return dp 