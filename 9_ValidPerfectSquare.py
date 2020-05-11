class Solution:

    def isPerfectSquare(self, num: int) -> bool:
        if num % 10 in [2, 3, 7, 8]:
            return False
        if num%10 ==0:
            a=num/10
            if a%10!=0:
                return False
        # if sumOfDigits(self,num) not in [1, 4, 7, 9]:
        #     return False
        # else:
        #     return True
        if num in [0,1]:
            return True
        x = num // 2
        seen = set([x])
        while x * x != num:
            x = (x + (num // x)) // 2
            if x in seen: 
                return False
            seen.add(x)
        return True
        
