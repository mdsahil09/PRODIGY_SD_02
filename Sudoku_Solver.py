def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def is_valid_move(board, row, col, num):
    # Check if the number is not in the same row or column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if the number is not in the same 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None  # No empty location found

def solve_sudoku(board):
    empty_row, empty_col = find_empty_location(board)

    if empty_row is None and empty_col is None:
        # No empty location, puzzle is solved
        return True

    for num in range(1, 10):
        if is_valid_move(board, empty_row, empty_col, num):
            # Try placing the number
            board[empty_row][empty_col] = num

            # Recursively try to solve the rest of the puzzle
            if solve_sudoku(board):
                return True

            # If placing the number doesn't lead to a solution, backtrack
            board[empty_row][empty_col] = 0

    return False  # No solution found for the current configuration

def get_user_input():
    print("Enter the Sudoku puzzle row by row. Use '0' for empty cells.")
    puzzle = []
    for i in range(9):
        row = list(map(int, input(f"Enter row {i + 1} (9 numbers separated by spaces): ").split()))
        puzzle.append(row)
    return puzzle

if __name__ == "__main__":
    # Get the Sudoku puzzle from the user
    puzzle = get_user_input()

    print("\nUnsolved Sudoku Puzzle:")
    print_board(puzzle)

    # Solve the Sudoku puzzle
    if solve_sudoku(puzzle):
        print("\nSolved Sudoku Puzzle:")
        print_board(puzzle)
    else:
        print("\nNo solution exists.")
