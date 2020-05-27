class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dict_s = {}
        dict_p={}

        len_s = len(s)
        window_len =len(p)
        if len_s<window_len:
            return
        found_list = []

        for char in p:
            if dict_p.get(char):
                dict_p[char]+=1
            else:
                dict_p[char]=1

        i=0
        end= window_len-1
        if end<len_s:
            while i <= end:
                char = s[i]
                if dict_s.get(char):
                    dict_s[char] += 1
                else:
                    dict_s[char] = 1
                i += 1
        if dict_s==dict_p:
            found_list.append(0)
        dict_s[s[0]]-=1
        if dict_s.get(s[0])==0:
            del dict_s[s[0]]

        for i,ch in enumerate(s):
            if i!=0:
                end=i+window_len-1
                ind=i
                if end < len_s:
                    char=s[end]
                    if dict_s.get(char):
                        dict_s[char] += 1
                    else:
                        dict_s[char] = 1

                if dict_s==dict_p:
                    found_list.append(i)
                dict_s[ch]-=1
                if dict_s.get(ch) == 0:
                    del dict_s[ch]

        return found_list

        
