class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = -1
        j = 0
        i = len(height) - 1
        while i != j:
            max_area = max(max_area, min(height[i], height[j]) * (i - j))
            if height[i] > height[j]:
                j += 1
            else:
                i -= 1
        return max_area


# Brute force: Calculate area without slant for each pair in the array. Keep highest | T: O(n^2) S: O(1)
# Optimization:
# - Set two pointers one at position 0 (lag) and other at position n-1 (lead).
# - Calculate the area created between the indexes: min(h[lead], h[lag]) * (lead - lag).
# - Compare the calculate area against max area, assign to max area if calculate area is bigger.
# - Shift the pointer with the smallest height (bottleneck):
#       - If lead is smaller, update lead to lead - 1.
#       - Else, update lag to lag + 1.
# - Repeat until lead == lag.
# T: O(n) | S: O(1)

if __name__ == "__main__":
    # Test Cases
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert Solution().maxArea([1, 1]) == 1
    assert Solution().maxArea([0, 0]) == 0
    assert Solution().maxArea([1, 1, 9]) == 2
    assert Solution().maxArea([1, 9, 1]) == 2

    print("All passed!")
