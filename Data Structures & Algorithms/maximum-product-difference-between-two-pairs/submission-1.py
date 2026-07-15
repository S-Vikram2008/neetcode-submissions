class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:

        # Main math logic :
        '''
        If a pair is (w,x)-(y*z)
        Inorder to maximise a product difference ,the first pair (w,x) should be greater than second pair (y,z) 
        So the first two values (w,x) should be the maximum two values from list and
        second two values (y,z) should be minimum two values from list 
        '''

        # We first sort the list two numbers 
        nums.sort()

        # Finally returning the answer
        return (nums[-1]*nums[-2])-(nums[0]*nums[1])