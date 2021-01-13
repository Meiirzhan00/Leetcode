class Solution:    
    def reverse(self, x: int) -> int:
        s=''
        if x==0:
            s+='0'
            
        elif x<0 and str(x) not in '0' :
            c=str(x).count('0')
            s+='-'
            x=-x
            x//=10**c
            while x>0:
                n=x
                n%=10
                s+=str(n)
                x//=10

        elif x<0 :
            s+='-'
            x=-x
            while x>0:
                n=x
                n%=10
                s+=str(n)
                x//=10

        elif str(x) not in '0':
            c=str(x).count('0')
            x//=10**c
            while x>0:
                n=x
                n%=10
                s+=str(n)
                x//=10

        else:
             while x>0:
                n=x
                n%=10
                s+=str(n)
                x//=10

        return s

p=Solution()
print(p.reverse(x=123))
print(p.reverse(x=-123))
print(p.reverse(x=120))
print(p.reverse(x=0))
            
