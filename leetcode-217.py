class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniques = {}
        for num in nums:
            if uniques.get(num):
                return True
            else:
                uniques[num] = True
        return False