class Solution:
    def readBinaryWatch(self, n: int) -> List[str]:
        times = []
        for h in range(12):
            for m in range(60):
                if ((bin(h) + bin(m)).count('1') == n):
                    time = "{:d}:{:02d}".format(h,m)
                    times.append(time)
        return times