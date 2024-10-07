# Hacktoberfest Contribution :-
# N-Queens Problem Using Backtracking
def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
        if board[row][i]:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j]:
            return False
            
    return True

def solve_n_queens_util(board, col, N):
    if col >= N:
        print_solution(board)
        return True
    
    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1  # Place queen
            
            # Recur to place rest of the queens
            res = solve_n_queens_util(board, col + 1, N) or res
            
            # If placing queen in board[i][col] doesn't lead to a solution, remove queen
            board[i][col] = 0  # Backtrack
