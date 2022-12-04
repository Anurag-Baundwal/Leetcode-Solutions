class Solution:
    """
    Input: 1 string[int]. nums (string[int])
    Output: Nan
    Constrains:
        - nums well formated
        - in-place without making a copy of the array.
    Edge Cases:
        - len(nums) == 0

    Time complexity: O(N)
    Space complexity: O(1)
    """

    def moveZeroes(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        # keep track of last non-zero element's index (last_nz)
        # keep track of current index as well

        last_nz = 0
        
        for i, v in enumerate(nums):
            if v != 0:
                nums[last_nz] = v
                last_nz += 1

        for i in range(last_nz, len(nums)):
            nums[i] = 0