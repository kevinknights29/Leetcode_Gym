class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        T = 0
        B = len(matrix) - 1
        while T <= B:
            mid_v = (T + B) // 2
            if target > matrix[mid_v][-1]:
                T = mid_v + 1
            elif target < matrix[mid_v][0]:
                B = mid_v - 1
            else:
                break
        if not (T <= B):
            return False

        L = 0
        R = len(matrix[mid_v]) - 1
        while L <= R:
            mid_h = (L + R) // 2
            if target > matrix[mid_v][mid_h]:
                L = mid_h + 1
            elif target < matrix[mid_v][mid_h]:
                R = mid_h - 1
            else:
                return True
        return False


if __name__ == "__main__":
    # Test Cases
    assert Solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
    assert not Solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)

    print("All passed!")
