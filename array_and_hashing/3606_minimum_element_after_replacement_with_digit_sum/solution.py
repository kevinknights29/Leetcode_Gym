class Solution:
    def minElement(self, nums: list[int]) -> int:
        # We need to traverse the entire list, meaning exhaustive search. O(n) time complexity.
        # We need to calculate the digits of the current number with an arithmetic operation. O(n * m)
        ans = []
        for num in nums:
            value = 0
            while num > 0:
                value += num % 10
                num = num // 10
            ans.append(value)
        return min(ans)


if __name__ == "__main__":
    s = Solution()

    assert s.minElement([10, 12, 13, 14]) == 1
    assert s.minElement([1, 2, 3, 4]) == 1
    assert s.minElement([999, 19, 199]) == 10

    print("All passed!")
