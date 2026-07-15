class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        # Creating a hashmap to store frequency counts
        hashmap=dict()

        # Iterating through the array to store {number:frequency}
        for i in nums:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        
        # Finding whether the frequencies are even as to divide numbers into pairs they must occur a even number of times in the hashmap
        for j in hashmap:
            if hashmap[j]%2!=0:
                return False
        
        return True