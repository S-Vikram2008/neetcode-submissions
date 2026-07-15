class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # Creating a hashmap to store character and the index where they are found
        hashmap=dict()

        # Iterating through nums
        
        for i in range(0,len(nums)):
            if nums[i] in hashmap:
                if abs(i-hashmap[nums[i]])<=k:
                    return True
                else:
                    hashmap[nums[i]]=i   # If above if statement does not satisfy then we change new index value instead of old index value 
            else:
                hashmap[nums[i]]=i
        
        return False