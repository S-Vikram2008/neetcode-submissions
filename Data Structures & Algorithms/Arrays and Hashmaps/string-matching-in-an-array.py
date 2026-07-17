class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        output=[]
        for i in range(0,len(words)):
            for j in range(0,len(words)):
                if i!=j and words[i] in words[j]:
                    output.append(words[i])
                    break
        
        return output
                  
