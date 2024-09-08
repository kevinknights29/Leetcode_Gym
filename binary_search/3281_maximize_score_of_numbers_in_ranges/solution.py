class Solution:
    def maxPossibleScore(self, start: list[int], d: int) -> int:
        n = len(start)
        start.sort()

        def isValid(gap):
            last = start[0]
            for i in range(1, n):
                curr = max(start[i], last + gap)
                if curr > start[i] + d:
                    return False
                last = curr
            return True

        left, right = 0, start[-1] + d - start[0]
        while left < right:
            mid = left + (right - left + 1) // 2
            if isValid(mid):
                left = mid
            else:
                right = mid - 1

        return left


if __name__ == "__main__":
    # Test Cases
    assert Solution().maxPossibleScore([6, 0, 3], 2) == 4
    assert Solution().maxPossibleScore([2, 6, 13, 13], 5) == 5

    print("All passed!")
