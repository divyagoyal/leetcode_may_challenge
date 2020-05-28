class Solution:
    def countBits(self, num: int) -> List[int]:
        import math
        
        if num<0:
            return []

        dict_map={}
        dict_map[0]=0
        dict_map[1]=1
        dict_map[2]=1

        if num>2:
            for i in range(3,num+1):
                sum=0
                if int(math.log(i,2)) ==math.log(i,2):
                    dict_map[i]=1
                    continue
                else:
                    number = i
                    while number:
                        b = int(math.log(number, 2))
                        sum+= dict_map[2**b]
                        number = number - 2 ** b
                dict_map[i]=sum

        return list(dict_map.values())[0:num+1]
        
        
        # bits_per_index = [0] * (num + 1)

        # for i in range(num + 1):
        #     bits_per_index[i] = bits_per_index[i // 2] + (i & 1)

         # return bits_per_index
