class Solution:
    def frequencySort(self, s: str) -> str:
        dict_full = dict()
        for i,ch in enumerate(s):
            if dict_full.get(ch):
                dict_full.get(ch)['count']+=1
            else:
                dict_full[ch]={}
                dict_full[ch]['count']=1
                dict_full[ch]['index']=i

        reversed_dict = list(reversed(sorted(dict_full.items(),key = lambda kv: (kv[1]['count'],kv[0]))))
        s=""
        for item in reversed_dict:
            while item[1]['count']>0:
                s+=item[0]
                item[1]['count']-=1
        return s
