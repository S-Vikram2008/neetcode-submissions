class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap=dict()

        for i in range(len(nums)):
            if target-nums[i] not in hashmap:
                hashmap[nums[i]]=i
            else:
                if i<hashmap[target-nums[i]]:
                    return [i,hashmap[target-nums[i]]]
                else:
                    return [hashmap[target-nums[i]],i]


