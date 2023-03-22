class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = n & 1 # least signifcant bit (because 1 is 0b00000...0001)
        n >>= 1
        while n:
            curr = n & 1
            if prev == curr:
                return False
            prev = curr
            n >>= 1
        return True

        #faster than converting the number to binary using bin