class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        # we are using binary search
        right = n-1
        left = 0
        while(left<=right):
            mid = left + (right-left)//2
            if isBadVersion(mid)==False:
                left = mid+1
            else:
                right = mid-1
        return left