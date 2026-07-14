class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashmap=dict()
        nums=[] # List to store all distinct characters
        
        # Iterating through array and storing frequencies in hashmap
        for i in arr:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        
        # Iterating through hashmap to get distinct characters
        for i in hashmap:
            if hashmap[i]==1:
                nums.append(i)

        if len(nums)<k:
            return ''
        else:
            return nums[k-1]

  