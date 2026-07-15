class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        col=len(matrix[0])

        left=0
        right=rows*col-1

        while left<=right:
            mid=(left+right)//2

            curelement=matrix[mid//col][mid%col]

            if curelement==target:
                return True
            elif curelement<target:
                left=mid+1
            elif curelement>target:
                right=mid-1
            
            
        else:
            return False
        
