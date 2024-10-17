class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        # Define n as the length of nums => n = len(nums)
        # Create an ans array of size n => ans = list[None] * n | O(n) space
        # Iterate over nums => for i, num in enumerate(nums): | O(n) time
        # - Brute force Route: O(m) where m is the max(nums) => Overall O(n * m)
        #       ans[i] = -1
        #       for value in range(0, num, 1):
        #           if value OR (value + 1) == num:
        #               ans[i] = value
        #               break
        # NOTE: Brute force no longer valid
        # - The second iteration represents a search, thus it can be enhanced with binary search.
        #   Given that the search is ordered (0 to num), binary search is a viable option.
        #   Thus reducing the time complexity from O(n * m) to O (n * log(m))

        n = len(nums)
        ans = [None] * n
        for i, num in enumerate(nums):
            ans[i] = -1
            # binary search
            L = 0
            R = num
            while L < R:
                mid = L + ((R - L) // 2)
                result = mid | (mid + 1)
                if result == num:
                    ans[i] = mid
                    break
                elif result < num:
                    L = result
                else:
                    L = mid + 1
        return ans


if __name__ == "__main__":
    s = Solution()

    assert s.minBitwiseArray([2, 3, 5, 7]) == [-1, 1, 4, 3]
    assert s.minBitwiseArray([11, 13, 31]) == [9, 12, 15]

    print("All Passed!")
