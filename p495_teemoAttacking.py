#First Try
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

#Cleaner code:
class Solution:
    def findPoisonedDuration(self, times: List[int], d: int) -> int:
        ans = 0
        for i in range(len(times)):
            if i == len(times) - 1:
                ans += d
            else:
                diff = times[i+1] - times[i]
                ans += d if (diff >= d) else diff 
        return ans