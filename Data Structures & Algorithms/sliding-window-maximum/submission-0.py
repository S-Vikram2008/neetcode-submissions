class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxima=[]
        max_element=float('-inf')
        
        left=0
        right=k

        while right<=len(nums):
            maxima.append(max(nums[left:right]))
            left+=1
            right+=1
        
        return maxima


