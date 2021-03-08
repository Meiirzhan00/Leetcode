class Solution:
    def reverse(self, x: int) -> int:
        
        result = 0
        abs_x = abs(x)
        while abs_x != 0 :
            remainder = abs_x % 10 
            abs_x = abs_x //10
            
            temp = result * 10 + remainder
            result = temp
        
        if x < 0 :
            result = -1 * result
            
        if result < - 2**31 or result > 2**31 -1:
            result = 0
        
        return result

p=Solution()
print(p.reverse(1245125))
