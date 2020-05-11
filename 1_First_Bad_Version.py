class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        i=1
        j=n
        count=0
        while i<j:
            mid = int(i + (j - i) / 2)
            if isBadVersion(mid):
                j=mid
            else:
                i = mid+1
        return i
            
