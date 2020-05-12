class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)%2==0:
            return -1
        i=0
        j=len(nums)-1
        while i<=j:
            mid = i + (j - i) // 2
            if i==j:
                break
            if mid%2==0:
                if nums[mid]==nums[mid+1]:
                    i=mid+2
                else:
                    j=mid
            elif mid%2==1:
                if nums[mid]==nums[mid-1]:
                    i=mid+1
                else:
                    j=mid-1
        return nums[mid]





        
