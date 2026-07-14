class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        hashmap=dict()
        maxlucky=-1
        count=0

        for i in arr:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        
        for i in hashmap:
            if hashmap[i]==i:
                maxlucky=max(maxlucky,i)
        
        return maxlucky
        

        



