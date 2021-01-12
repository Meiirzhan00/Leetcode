class Solution:
    def reverse(self, x: int) -> int:
        s=''
        while x>0:
            n=x
            if n<0:
                s+='-'
            n%=10
            s+=str(n)
            x//=10
        return s
    
p=Solution()
print(p.reverse(x=-123))

        
