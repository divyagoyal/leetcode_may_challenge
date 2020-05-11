class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_i = 0
        count=1
        for i in range(len(nums)):
            if nums[maj_i]==nums[i]:
                count+=1
            else:
                count-=1
            if count==0:
                maj_i=i
                count=1
        return nums[maj_i]
        
        
       
