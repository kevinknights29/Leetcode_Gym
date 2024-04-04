class Solution:
    def trap(self, height: list[int]) -> int:
        units = 0
        L = 0
        R = len(height) - 1
        max_HL = height[L]
        max_HR = height[R]

        while R > L:
            if max_HR > max_HL:
                L += 1
                max_HL = max(max_HL, height[L])
                units += max_HL - height[L]
            else:
                R -= 1
                max_HR = max(max_HR, height[R])
                units += max_HR - height[R]

        return units


if __name__ == "__main__":
    assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert Solution().trap([4, 2, 0, 3, 2, 5]) == 9
    assert Solution().trap([1, 2, 3, 4, 5]) == 0
    assert Solution().trap([5, 4, 3, 2, 1]) == 0
    assert Solution().trap([5, 2, 1, 2, 1, 5]) == 14
    assert Solution().trap([5, 2, 1, 2, 1, 5, 2, 1, 2, 1, 5]) == 28

    print("Passed all tests!")
