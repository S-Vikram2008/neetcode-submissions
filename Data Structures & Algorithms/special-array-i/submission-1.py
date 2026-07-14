class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)<=1:
            return True
        else:
            left=0
            right=1
            flag=False

            while right<len(nums):
                if (nums[left]%2==0 and nums[right]%2!=0) or (nums[left]%2!=0 and nums[right]%2==0):
                    flag=True
                else:
                    return False
                
                left+=1
                right+=1
            
            return flag