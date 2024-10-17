class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        # Define n as the length of nums => n = len(nums)
        # Create an ans array of size n => ans = list[None] * n | O(n) space
        # Iterate over nums => for i, num in enumerate(nums): | O(n) time
        # - Brute force Route: O(m) where m is the max(nums) => Overall O(n*m)
        #       ans[i] = -1
        #       for value in range(0, num, 1):
        #           if value OR (value + 1) == num:
        #               ans[i] = value
        #               break

        n = len(nums)
        ans = [None] * n
        for i, num in enumerate(nums):
            ans[i] = -1
            for value in range(0, num):
                if (value | (value + 1)) == num:
                    ans[i] = value
                    break
        return ans


if __name__ == "__main__":
    s = Solution()

    assert s.minBitwiseArray([2, 3, 5, 7]) == [-1, 1, 4, 3]
    assert s.minBitwiseArray([11, 13, 31]) == [9, 12, 15]

    print("All Passed!")
