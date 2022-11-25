class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        res.append([1]) # first row in pascal's triangle
        for i in range(1, numRows):
            row = []
            row.append(1) # 1 at the start of the row
            for j in range(i-1): 
                # i is the length of the previous row
                # this look will then run i-1 times
                # this is because we need to calculate i-1 terms using addition
                # the remaining two terms are just 1's - present at the start and end of the row
                
                #middle values - calculated using addition (total i-1 values)
                row.append(res[i-1][j] + res[i-1][j+1])
                    # previous row[0] + previous row[1]
                    # res[i-1] access the previous row
            
            row.append(1) # 1 at the end of the row
            res.append(row)
        return res