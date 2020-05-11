class Solution:
    def findComplement(self, num: int) -> int:
        import math 
        number_of_bits = (int)(math.floor(math.log(num) /
                                math.log(2))) + 1; 
        return ((1 << number_of_bits) - 1) ^ num; 
