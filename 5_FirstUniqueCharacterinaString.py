class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_s = dict()
        for char in s:
            if char in dict_s:
                dict_s[char]+=1
            else:
                dict_s[char]=1
        for i,char in enumerate(s):
            if dict_s[char]==1:
                return i
        return -1
        
