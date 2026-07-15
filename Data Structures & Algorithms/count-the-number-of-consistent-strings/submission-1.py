class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        count=0     # Initialising the count variable to 0

        for word in words:     # Iterating through words list
            for ch in word:    # Picking up a single element from words and iterating the characters
                if ch not in allowed:
                    break
            else:
                count+=1
        
        return count   # Finally returning the count 


            
