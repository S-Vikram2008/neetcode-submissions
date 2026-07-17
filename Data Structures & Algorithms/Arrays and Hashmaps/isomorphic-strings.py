class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # if length of both strings are not equal they can't be Isomorphic to each other
        if len(s)!=len(t):
            return False
        else:
            # Creating a hashmap to store mapped characters
            hashmap=dict()
            
            # Iterating through string 's' and checking whether it is mapped correctly .
            for i in range(0,len(s)):
                if s[i] in hashmap: 
                    if hashmap[s[i]]!=t[i]:
                        return False
                else:
                    if t[i] not in hashmap.values(): # Checking whether an element is already linked to another element 
                        hashmap[s[i]]=t[i]
                    else:
                        return False
            
            return True

        

