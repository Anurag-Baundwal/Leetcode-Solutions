# part a: Iterative solution
# For recursive solution check p704b.py
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        lo = 0
        hi = len(arr) - 1

        while (lo <= hi):
            mid = (lo+hi)//2
            if arr[mid] == target:
                # base condition
                return mid

            if target < arr[mid] and target >= arr[lo]:
                #target lies in left half
                #adjust hi to be one less than mid
                hi = mid - 1

            elif target > arr[mid] and target <= arr[hi]:
                #target lies in right half
                # we must adjust lo to be one more than mid
                lo = mid + 1
        # we are out of the loop 
        # ie lo became more than hi 
        # then target was not found
        return -1
        # we return -1 when the target is not found