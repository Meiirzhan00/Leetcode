from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if 2<=len(nums)<=10**3 and -10**9<=nums[i]<=10**9 and -10**9<=target<=10**9 :
                for j in range(i+1,len(nums)):
                    if nums[i]+nums[j]==target:
                        return [i,j]
            else:
                return "Белгіленген шектен асып кетті."

s=Solution()
print(s.twoSum(nums = [2,7,11,15], target = 9))
