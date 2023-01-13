class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse() # works
        # s[:] = s[::-1] # works
        # s[:] = s[::-1] # does not work