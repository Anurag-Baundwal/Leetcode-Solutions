# class Solution:
#     def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
#         s1 = sum(aliceSizes)
#         s2 = sum(bobSizes)

#         # now swap 2 boxes
        
#         # brute force
#         for i in aliceSizes:
#             for j in bobSizes:
#                 if s1 +j-i == s2+i-j:
#                     return [i, j]

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_a = sum(aliceSizes)
        sum_b = sum(bobSizes)
        set_b = set(bobSizes)
        diff = (sum_a - sum_b) // 2
        for a in aliceSizes:
            b = a - diff
            if b in set_b:
                return [a, b]
