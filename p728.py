class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            digits = list(str(i))
            if "0" in digits: 
                continue
            flag = 1
            for j in digits:
                if i % int(j) != 0:
                    flag = 0
            if flag == 1:
                ans.append(i)
        return ans