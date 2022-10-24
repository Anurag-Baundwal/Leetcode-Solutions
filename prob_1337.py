class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        tmp = []
        for i, row in enumerate(mat):
            cand = (sum(row),i)             # sums firstbecause we will have to sort tmp
            tmp.append(cand)

        tmp.sort
        return [i[1] for i in tmp[:k]]      # i[1] means 2nd element ie row numbers
                                            # [:k] selects the first k elements ie the first k rows 

