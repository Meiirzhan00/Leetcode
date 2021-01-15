class Solution:
    def isPalindrome(self, x: int) -> bool:
        if -2**31 <= x <= 2**31 - 1:
            s=''
            for i in range(len(str(x))-1,-1,-1):
                s+=str(x)[i]
            if s==str(x):
                return True
            else:
                return False
        else:
            return 'Белгіленген шектен асып кетті'

p=Solution()
print(p.isPalindrome(121))
print(p.isPalindrome(-121))
print(p.isPalindrome(10**35))
             

----------------------------------------------------

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if -2**31 <= x <= 2**31 - 1:
            x=str(x)
            if x==x[::-1]:
                return True
            else:
                return False
        else:
            return 'Белгіленген шектен асып кетті'

p=Solution()
print(p.isPalindrome(-121))
print(p.isPalindrome(10**35))
