class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        lookup={"]":"[","}":"{",")":"("}
        
        if 1<=len(s)<=10**4:
            for p in s:
                if p in lookup.values():
                    stack.append(p)
                elif stack and lookup[p] == stack[-1]:
                    stack.pop()
                else:
                    return False
        else:
            return False

        return stack == []

p=Solution()
print(p.isValid("[[({})]]"))
