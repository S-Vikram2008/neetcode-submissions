class Solution:
    def maxDifference(self, s: str) -> int:
        
        # Creating a hashmap to store characters and frequencies
        hashmap=dict()

        # Adding characters and frequencies into hashmap
        for i in s:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        
        # Math logic to solve :
        # To maximise difference we need to take maximum odd no and minimised even number 
        # which would make the difference greater. So we keep track of maximum odd and minimum even number 

        maxodd=0
        mineven=float('inf')

        for freq in hashmap.values():
            if freq%2==0:
                mineven=min(mineven,freq)
            elif freq%2!=0:
                maxodd=max(maxodd,freq)
        
        return maxodd-mineven
        
        


        
