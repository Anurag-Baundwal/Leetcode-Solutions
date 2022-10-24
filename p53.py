class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #BRUTE FORCE
        #Try all arrays
        #Start at index 0 and consider all arrays starting there
        #Then go to index 1 and consider all arrays starting there
        
        
        max = min(nums)
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                arr = nums[i:j+1]   # say len of nums is 5 - then j would reach 4 - for slicing last index needs to be 4+1 
                #print(arr)
                total = sum(arr)
                #print(total)
                if total > max:
                    max = total
            
        return max

# METHOD 2:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int: