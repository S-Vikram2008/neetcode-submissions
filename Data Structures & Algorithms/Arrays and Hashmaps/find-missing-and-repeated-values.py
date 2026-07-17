class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        # Designing a dictionary to store elements and their occurence
        hashmap=dict()
        output=[]

        for i in grid:
            for j in i:
                if j not in hashmap:
                    hashmap[j]=1
                else:
                    hashmap[j]+=1

        # Checking which element in hashmap has a frequency greater than 1
        for element in hashmap:
            if hashmap[element]>1:
                output.append(element)
                break
        
        # Iterating from 1 to n*n+1 where n*n is number of elements in square matrix and finding which element is missing in the grid 
        for element in range(1,len(grid)*len(grid[0])+1):
            if element not in hashmap:
                output.append(element)
                break
        
        # Finally returning the output which contains [Repeated element,Missing value]
        return output
        
