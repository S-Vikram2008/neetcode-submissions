class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words=s.split()

        if len(pattern)!=len(words):
            return False
        else:
            # Creating a hashmap to map characters with words
            hashmap=dict()

            for i in range(0,len(pattern)):
                if pattern[i] in hashmap:
                    if hashmap[pattern[i]]!=words[i]:
                        return False
                else:
                    if words[i] in hashmap.values() :
                        return False
                    else:
                        hashmap[pattern[i]]=words[i]
            
            return True