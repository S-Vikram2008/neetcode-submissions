class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        # Creating a hashmap to store frequencies
        hashmap=dict.fromkeys(['b','a','l','o','n'],0)

        # Adding characters and frequencies into hashmap
        for i in text:
            if i in hashmap:
                hashmap[i]+=1

        hashmap['l']//=2
        hashmap['o']//=2
        return min(hashmap.values())
            