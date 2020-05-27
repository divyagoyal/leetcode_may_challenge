class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dict_map={}
        max_len,count=0,0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                count+=-1
            if count ==0:
                max_len=i+1
            if count in dict_map:
                max_len = max(max_len, i-dict_map[count])
            else:
                dict_map[count]=i
        return max_len
                    
                
                
            
        
        
        
