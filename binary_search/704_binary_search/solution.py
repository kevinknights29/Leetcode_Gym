class Solution:
    def search(self, nums: list[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] > target:
                R = mid - 1
            elif nums[mid] < target:
                L = mid + 1
            else:
                return mid
        return -1


if __name__ == "__main__":
    # Test Cases
    assert Solution().search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert Solution().search([-1, 0, 3, 5, 9, 12], 2) == -1

    print("All passed!")
