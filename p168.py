class Solution(object):
    def convertToTitle(self, n):
        # Trying to make it faster, but seems all solution have some little variation and fall approx on the same coordinates 
        lookup = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        title = []
        while n:
            n, rem = divmod(n - 1, 26)
            title.append(lookup[rem])
            
        return "".join(title[::-1])