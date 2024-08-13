class Solution:
    def findMin(self, nums: list[int]) -> int:
        L = 0
        R = len(nums) - 1
        min_num = min(nums[L], nums[R])
        while L <= R:
            mid = (L + R) // 2
            min_num = min(min_num, nums[mid])
            if nums[mid] > nums[R]:
                min_num = min(min_num, nums[R])
                L = mid + 1
            else:
                min_num = min(min_num, nums[L])
                R = mid - 1
        return min_num


if __name__ == "__main__":
    # Test Cases
    assert Solution().findMin([3, 4, 5, 1, 2]) == 1
    assert Solution().findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert Solution().findMin([11, 13, 15, 17]) == 11

    print("All passed!")
