class Solution:
    def isPalindrome(self, s: str) -> bool:
        sub=''
        for i in s:
            if i.isalnum():
                sub+=i.lower()
        
        if sub==sub[::-1]:
            return True
        else:
            return False

