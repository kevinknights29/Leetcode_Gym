class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: list[int]) -> int:
        n = len(source)
        m = len(pattern)
        target_set = set(targetIndices)

        dp = [[float("inf")] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(0, m + 1):
                dp[i][j] = min(dp[i][j], dp[i - 1][j])
                if j < m and source[i - 1] == pattern[j]:
                    if i - 1 not in target_set:
                        dp[i][j + 1] = min(dp[i][j + 1], dp[i - 1][j])
                    else:
                        dp[i][j + 1] = min(dp[i][j + 1], dp[i - 1][j] + 1)

        if dp[n][m] == float("inf"):
            return 0

        return len(targetIndices) - dp[n][m]


if __name__ == "__main__":
    # Test Cases
    s = Solution()
    assert s.maxRemovals(source="abbaa", pattern="aba", targetIndices=[0, 1, 2]) == 1
    assert s.maxRemovals(source="bcda", pattern="d", targetIndices=[0, 3]) == 2
    assert s.maxRemovals(source="dda", pattern="dda", targetIndices=[0, 1, 2]) == 0
    assert s.maxRemovals(source="yeyeykyded", pattern="yeyyd", targetIndices=[0, 2, 3, 4]) == 2
    print("All passed!")
