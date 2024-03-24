class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = set()
        size = len(board)
        dim = int(size**0.5)

        for i in range(size):
            for j in range(size):
                if board[i][j] != ".":
                    num = board[i][j]
                    # Check for duplicate in row
                    if (i, num) in seen:
                        return False
                    seen.add((i, num))
                    # Check for duplicate in column
                    if (num, j) in seen:
                        return False
                    seen.add((num, j))
                    # Check for duplicate in 3x3 sub-box
                    if (i // dim, j // dim, num) in seen:
                        return False
                    seen.add((i // dim, j // dim, num))

        return True


# Brute Force:
# - Create a hashset to store the seen values.
# - Iterate over each 3x3 matrix.
# - Iterate over each column.
# - Iterave over each row.
# - Add the value to the hashset.
# - If a num has already been seen in the row, column or 3x3 sub-box, return False.
# - After all iterations are done, return True.
# T: O(n^3) | S: O(n^2)

# Optimization:
# - Create a hashset to store the seen values.
# - Iterate over each cell.
# - If the cell is not empty.
#   - Check if the value has been seen in the row.
#   - Check if the value has been seen in the column.
#   - Check if the value has been seen in the 3x3 sub-box.
#   - If the value has been seen in any of the above, return False.
# - If all cells have been iterated over, return True.
# T: O(n^2) | S: O(n^2)

if __name__ == "__main__":
    # Test Cases
    assert Solution().isValidSudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
    assert not Solution().isValidSudoku(
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )

    print("All passed!")
