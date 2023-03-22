class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        cur_sum = 0 #current_sum
        right_sum = 0
        for i, num in enumerate(nums):
            cur_sum += num
            right_sum = total - cur_sum
            if cur_sum - num == right_sum: # left_sum == right_sum ?
                return i
        return -1