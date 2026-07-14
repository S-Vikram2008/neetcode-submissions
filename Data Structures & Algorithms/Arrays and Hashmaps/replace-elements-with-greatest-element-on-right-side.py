class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max=arr[-1]
        output=[-1]*len(arr)

        for i in range(len(arr)-2,-1,-1):
            if arr[i]>max:
                output[i]=max
                max=arr[i]
                
            else:
                output[i]=max
        
        return output

                
