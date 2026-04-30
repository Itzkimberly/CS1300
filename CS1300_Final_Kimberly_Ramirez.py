# CS1300_Final_Kimberly_Ramirez.py
# Mock Final Exam Solutions

# ============================================================
# PROBLEM 2 — Caesar Cipher Encoder
# ============================================================
def caesar_encode(text, shift):
    """Returns a Caesar cipher encoded string preserving case."""
    result = ""
    for ch in text:
        if ch.isalpha():
            if ch.islower():
                # Shift within lowercase 'a'-'z'
                new_char = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            else:
                # Shift within uppercase 'A'-'Z'
                new_char = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            result += new_char
        else:
            # Non-letters remain unchanged
            result += ch
    return result


# ============================================================
# PROBLEM 3 — Matrix Transpose
# ============================================================
def transpose(matrix):
    """Returns the transpose of a rectangular 2D list."""
    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    # Outer loop runs over columns of original (becomes rows of result)
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        result.append(new_row)

    return result


# ============================================================
# PROBLEM 4 — Tic-Tac-Toe Winner Checker
# ============================================================
def check_winner(board):
    """Checks a 3x3 board and returns 'X', 'O', 'Draw', or 'Ongoing'."""
    # Check horizontal rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Check vertical columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonal (top-left to bottom-right)
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    # Check diagonal (top-right to bottom-left)
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    # Check if board is full (Draw) or still has empty spaces (Ongoing)
    for row in board:
        if " " in row:
            return "Ongoing"

    return "Draw"


# ============================================================
# TEST CASES & MAIN EXECUTION
# ============================================================
if __name__ == "__main__":
    # --- Problem 2 Tests ---
    print("=== Problem 2 Tests ===")
    print(caesar_encode("Hello, World!", 3))   # Khoor, Zruog!
    print(caesar_encode("abc xyz", 2))         # cde zab
    print(caesar_encode("Python 3", 5))        # Udymts 3

    # --- Problem 3 Tests ---
    print("\n=== Problem 3 Tests ===")
    m1 = [[1, 2, 3], [4, 5, 6]]
    print(transpose(m1))  # [[1, 4], [2, 5], [3, 6]]

    m2 = [[1, 2], [3, 4], [5, 6]]
    print(transpose(m2))  # [[1, 3, 5], [2, 4, 6]]

    # --- Problem 4 Tests ---
    print("\n=== Problem 4 Tests ===")
    board1 = [["X", "X", "X"], ["O", "O", " "], [" ", " ", " "]]
    print(check_winner(board1))  # X

    board2 = [["X", "O", "X"], ["X", "O", " "], [" ", "O", "X"]]
    print(check_winner(board2))  # O

    board3 = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]
    print(check_winner(board3))  # Draw

    board4 = [["X", "O", " "], [" ", "X", " "], [" ", " ", " "]]
    print(check_winner(board4))  # Ongoing