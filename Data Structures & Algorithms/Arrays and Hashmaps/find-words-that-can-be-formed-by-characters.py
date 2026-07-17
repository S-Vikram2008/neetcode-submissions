class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        sum=0

        # Creating a character hashset (chars)
        hashmap=dict()
        for i in chars:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        
        # Iterating through each word in 'words' list

        for word in words:
            if len(word)<=len(chars):
                wordmap=dict()
                for j in word:
                    if j not in wordmap:
                        wordmap[j]=1
                    else:
                        wordmap[j]+=1
                
                # Checking whether character counts in wordmap are less than or equal to character counts in hashmap

                for i in wordmap:
                    if i in hashmap: # Checking if word exists in hashmap - Primary condiiton
                        if wordmap[i]>hashmap[i]: # Checking if frequencies of word in wordmap is greater than hashmap , if true when break the loop - Secondary condition
                            break
                    else:
                        break
                else:
                    sum+=len(word)

        return sum
                
        
