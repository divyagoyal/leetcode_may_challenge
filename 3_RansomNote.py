class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d= dict()
        flag=True

        for i in magazine:
            if d.get(i) is None:
                d[i]=1
            else:
                d[i]+=1

        for c in ransomNote:
            if d.get(c) is None or d.get(c)==0:
                return False
            else:
                d[c]-=1
        return True

        
