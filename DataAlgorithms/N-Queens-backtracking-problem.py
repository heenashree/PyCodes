#https://www.youtube.com/watch?v=xFv_Hl4B83A
#https://www.geeksforgeeks.org/python-program-for-n-queen-problem-backtracking-3/


N = 4

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print (board[i][j])
        print

def isSafe(board, row, col):
    

