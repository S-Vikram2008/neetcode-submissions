class Solution:
    def isPalindrome(self, s: str) -> bool:
        sub=''
        for i in s:
            if i.isalnum():
                sub+=i.lower()
        
        left=0
        right=len(sub)-1

        while left<right:
            if sub[left]!=sub[right]:
                return False
            left+=1
            right-=1
        else:
            return True

