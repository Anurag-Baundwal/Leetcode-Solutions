class Solution:
    def reverse(self, x: int) -> int:
        # Initialize result
        res = 0
        
        # Check if the number is negative
        negative = False
        if x < 0:
            negative = True
            x = -x
        
        # Reverse the digits of the number
        while x > 0:
            res = res * 10 + x % 10
            x = x // 10
        
        # Check if the result is within the 32-bit signed integer range
        if res > 2**31 - 1:
            return 0
        
        # Return the result with the appropriate sign
        return -res if negative else res