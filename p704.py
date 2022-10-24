class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # get middle 
        # compare middle and target
        # go to either left of middle or right of middle and repeat
        
        middle = len(nums)/2
        if nums[middle] == target