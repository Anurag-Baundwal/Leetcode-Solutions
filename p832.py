# class Solution:
#     def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
#         for i in image:
#             i.reverse()
#         for i in image:
#             for j in i:
#                 j = 0 if j == 1 else 1

#         return image

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[0 if x==1 else 1 for x in x][::-1] for x in A] 