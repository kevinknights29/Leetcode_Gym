class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                i_stack, h_stack = stack.pop()
                max_area = max((i - i_stack) * h_stack, max_area)
                start = i_stack
            stack.append([start, h])
        while stack:
            i, h = stack.pop()
            max_area = max((len(heights) - i) * h, max_area)
        return max_area


if __name__ == "__main__":
    # Test Cases
    assert Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert Solution().largestRectangleArea([2, 4]) == 4

    print("All passed")
