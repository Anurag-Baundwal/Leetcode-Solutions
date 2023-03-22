class Solution:
    def constructRectangle(self, n: int) -> List[int]:
        facs = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                facs.append(i)
        #print(facs)
        min = n
        ans = []
        for i in facs:
            diff = abs(i - n/i)
            if diff <= min:
                min = diff
                ans = [i, n//i] if i >= n//i else [n//i, i]
        return ans