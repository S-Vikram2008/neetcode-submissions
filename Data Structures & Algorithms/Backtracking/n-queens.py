class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Path list to store all valid combinations of placing Queen
        paths=[]

        # Initialising a board full of empty spaces '.' 
        board=[['.' for x in range(n)]for i in range(n)]

        # Initialising the isValid() 
        def isValid(board,row,column):
            # Checking if there is any queen in any row of that particular column before placing the next Queen .
            for i in range(row):
                if board[i][column]=='Q':
                    return False
            
            r=row
            c=column

            # Checking if there is any queen in upper left diagonal 
            while r>=0 and c>=0:
                if board[r][c]=='Q':
                    return False
                r-=1
                c-=1
            
            r=row
            c=column

            # Checking if there is any queen in upper right diagonal 
            while r>=0 and c<n:
                if board[r][c]=='Q':
                    return False
                r-=1
                c+=1
            # If none of the above returns False it means it is safe to place a queen here. Hence we return True 
            return True

        # Backtrack function
        def backtrack(row):
            # If row becomes equal to n , it means we have reached the last row . Hence we append the possible arrangement in paths and return back to calling function 
            if row==n:
                paths.append([''.join(row) for row in board])
                return
            
            # Checking every column in a particular row (ie) we check every possible column in particular row for safer placing of queen so that no two queens attack each other either diagonally or in straight line
            for column in range(n):
                if isValid(board,row,column):
                    board[row][column]='Q'
                    backtrack(row+1)
                    board[row][column]='.'
        

        backtrack(0)
        
        # Finally returning the paths list which contains all possible arrangements.
        return paths
