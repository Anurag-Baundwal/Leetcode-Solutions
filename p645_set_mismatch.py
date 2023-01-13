class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [sum(nums)-sum(set(nums)), list(set([x for x in range(1, len(nums)+1)])-set(nums))[0]]