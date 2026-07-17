class Solution:
    def totalNQueens(self, n: int) -> int:
        
        # Time Complexity: O(N!)
        # Space Complexity: O(N^2) for the board and O(N) recursion stack.


        # Board with full of zeros at first indicating that no queen is present 
        board=[[0 for x in range(n)] for i in range(n)]
        # Count to track number of possible arrangements
        count=0

        def isValid(board,row,column):
            # Checking whether any queen is present in every column
            for i in range(row):
                if board[i][column]==1:
                    return False

            # Temporary variables r and c are used instead of row and column as if upper left diagonal returns True then we go to check upper right diagonal at that time the variabkes row and column if used will have negative values due to the iteration from before loop so we create a temporary variables for iteration without changing the values of orginal row and column  
            r = row
            c = column

            # Upper left diagonal checking
            while r>=0 and c>=0:
                if board[r][c]==1:
                    return False
                r-=1
                c-=1

            r=row
            c=column

            # Upper right diagonal checking
            while r>=0 and c<len(board):
                if board[r][c]==1:
                    return False
                r-=1
                c+=1

            # If none of the above conditions are True then it means it is safe to keep the queen at that place.Hence we return True
            return True
        
        # Function to perform backtracking 
        def backtrack(row):
            # Access the count variable from the enclosing function so we can modify it.
            nonlocal count
            
            # If row becomes equal to the length of board that is if we are at end point it means our arrangement is correct and we increment count value by 1
            if row==len(board):
                count+=1
                return
            # For every column from 0 to len(board) we iterate it and check whether isValid function return True if it return True we keep a queen at that point and then backtrack it for next row (row+1) if the next arrangement fails we backtrack the previous arrangement and change the queen position to 0
            for column in range(len(board)):
                if isValid(board,row,column):
                    board[row][column]=1
                    backtrack(row+1)
                    board[row][column]=0
        
        # Finally initializing row value as 0 and then performing the first backtrack (row=0)
        row=0

        # The first backtrack row=0 give rise to second backtrack row=1 until row becomes equal to len(board)
        backtrack(row)
        return count
       
            
