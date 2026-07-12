class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        nums.sort()

        

        for i in range(0,len(nums)):
            first=nums[i]
            left=i+1
            right=len(nums)-1
            while left<right:
                if first+nums[left]+nums[right]<0:
                    left+=1
                elif first+nums[left]+nums[right]>0:
                    right-=1
                else:
                    if [first,nums[left],nums[right]] not in answer:
                        answer.append([first,nums[left],nums[right]])
                    left+=1
                    right-=1

        return answer
