class Solution:
    def remove_num(self,l,k):
        i = 0
        len_list = len(l)
  
        if k == 0:
            return l
        max_num = -10000
        max_index = 0

        while i < len_list:
            if l[i] >= max_num:
                max_num = l[i]
                max_index = i
                i += 1
            else:
                break
        del l[max_index]
        self.remove_num(l, k - 1)
        
    def removeKdigits(self, num: str, k: int) -> str:
        l = list()
        for i in num:
            l.append(int(i))
        if len(l)==k:
            return "0"
        else:
            a= self.remove_num(l,k)
            s = [str(i) for i in l]
            return str(int("".join(s)))



        
