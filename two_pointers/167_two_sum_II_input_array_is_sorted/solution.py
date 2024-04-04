class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        L = 0
        R = len(numbers) - 1

        if len(numbers) == 2:
            return [L + 1, R + 1]

        while R > L:
            index_sum = numbers[L] + numbers[R]
            if index_sum > target:
                R -= 1
            elif index_sum < target:
                L += 1
            else:
                return [L + 1, R + 1]


if __name__ == "__main__":
    assert Solution().twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert Solution().twoSum([2, 3, 4], 6) == [1, 3]
    assert Solution().twoSum([-1, 0], -1) == [1, 2]

    print("Passed all tests!")
