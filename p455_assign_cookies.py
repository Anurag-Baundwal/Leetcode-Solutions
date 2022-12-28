# class Solution:
#     def findContentChildren(self, greed: List[int], sizes: List[int]) -> int:
#         greed.sort()
#         sizes.sort()
        
#         count = 0

#         for g in greed:
#             for s in sizes:
#                 if s >= g:
#                     count += 1
#                     sizes.remove(s)
#                     break 

#         return count

from collections import deque

class Solution:
    def findContentChildren(self, greed: List[int], sizes: List[int]) -> int:
        # Initialize two pointers to the beginning of the lists
        i = 0
        j = 0
        count = 0

        # Convert the sizes list to a deque to allow efficient element removal
        sizes = deque(sizes)

        # Keep looping until one of the pointers reaches the end of the list
        while i < len(greed) and j < len(sizes):
            # If the current size is big enough for the current greed factor,
            # increment the count and move the j pointer to the next element
            if sizes[j] >= greed[i]:
                count += 1
                j += 1
            # Otherwise, move the i pointer to the next element
            else:
                i += 1

        # Return the final count
        return count