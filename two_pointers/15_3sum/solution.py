class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        output = []
        nums = sorted(nums)

        for i in range(len(nums)):
            if i > 0:
                if nums[i] == nums[i - 1]:
                    continue

            L = i + 1
            R = len(nums) - 1
            target = -1 * nums[i]
            while R > L:
                two_sum = nums[L] + nums[R]
                if two_sum > target:
                    R -= 1
                elif two_sum < target:
                    L += 1
                else:
                    output.append([nums[i], nums[L], nums[R]])

                    L += 1
                    while (nums[L] == nums[L - 1]) and (R > L):
                        L += 1

        return output


if __name__ == "__main__":
    assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert Solution().threeSum([0, 1, 1]) == []
    assert Solution().threeSum([0, 0, 0]) == [[0, 0, 0]]

    print("Passed all tests!")
