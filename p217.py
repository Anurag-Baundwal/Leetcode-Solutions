# METHOD 1: By sorting the array
# O(nlogn) time complexity
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

# METHOD 2: Using dictionary / hash map
# O(n) time complexity (but more memory is used)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        
        # loop through array 
        # if item is in hash map/ dict - duplicate found - return True
        # else add item to hashmap and keep looking till end of array is reached

        for x in nums:
            if x in d: return True
            else: d[x] = x