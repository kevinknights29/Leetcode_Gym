class Solution:
    def search(self, nums: list[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target:
                return mid

            if nums[L] <= nums[mid]:
                if (target > nums[mid]) or (target < nums[L]):
                    L = mid + 1
                else:
                    R = mid - 1
            else:
                if (target < nums[mid]) or (target > nums[R]):
                    R = mid - 1
                else:
                    L = mid + 1
        return -1


# Space: O(1)
# Time: O(log(n))

if __name__ == "__main__":
    # Test Cases
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert Solution().search([1], 0) == -1

    print("All passed!")
