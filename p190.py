class Solution:
    def reverseBits(self, n: int) -> int:
        return int(str(n)[::-1])        # ...
        # bitwise negation ?
        # convert into a string -> reverse digits -> convert back into an integer? -> will involve typecasting
