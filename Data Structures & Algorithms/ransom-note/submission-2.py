class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(magazine)<len(ransomNote):
            return False
        else:
            # Creating new hashmaps to store character frequencies of ransomNote and amagazine
            ransommap=dict()
            magazinemap=dict()

            # Counting the frequencies of characters and updating in hashmaps
            for i in ransomNote:
                if i not in ransommap:
                    ransommap[i]=1
                else:
                    ransommap[i]+=1

            for i in magazine:
                if i not in magazinemap:
                    magazinemap[i]=1
                else:
                    magazinemap[i]+=1

            for i in ransommap:
                if i not in magazinemap:
                    return False
                else:
                    if magazinemap[i]<ransommap[i]:
                        return False
            
            return True