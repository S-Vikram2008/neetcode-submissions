class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curcount=0
        maxcount=0

        for i in nums:
            if i==1:
                curcount+=1
                maxcount=max(maxcount,curcount)
            else:
                maxcount=max(maxcount,curcount)
                curcount=0
        
        return maxcount