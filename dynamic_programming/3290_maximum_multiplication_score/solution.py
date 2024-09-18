class Solution:
    def maxScore(self, a: list[int], b: list[int]) -> int:
        # Initialize the four maximum scores
        M = [float("-inf")] * 4

        # Iterate through each element in b
        for x in b:
            # Update the maximum scores from right to left
            for i in range(3, 0, -1):
                M[i] = max(M[i], M[i - 1] + x * a[i])

            # Update M[0]
            M[0] = max(M[0], x * a[0])

        # The final answer is M[3]
        return M[3]


if __name__ == "__main__":
    # Test Cases
    assert Solution().maxScore([3, 2, 5, 6], [2, -6, 4, -5, -3, 2, -7]) == 26
    assert Solution().maxScore([-1, 4, 5, -2], [-5, -1, -3, -2, -4]) == -1

    print("All passed!")
