class Solution:
    def findMaximumScore(self, nums: list[int]) -> int:
        n = len(nums)
        stack = []
        dp = [0] * n  # dp[i] stores the max score that can be obtained starting from index i

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack:
                j = stack[-1]
                dp[i] = max(dp[i], (j - i) * nums[i] + dp[j])

            dp[i] = max(dp[i], (n - 1 - i) * nums[i])  # Consider jumping directly to the end
            stack.append(i)

        return dp[0]


if __name__ == "__main__":
    # Test Cases
    assert Solution().findMaximumScore([1, 3, 1, 5]) == 7
    assert Solution().findMaximumScore([4, 3, 1, 3, 2]) == 16

    print("All passed")
