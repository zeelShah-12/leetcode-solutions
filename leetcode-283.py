class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        (i_p = insert_pos)
        """
        i_p = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i_p]=nums[i]
                i_p +=1
        for i in range(i_p,len(nums)):
            nums[i] = 0