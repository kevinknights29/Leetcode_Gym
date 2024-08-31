class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        nums = [f"{num:04d}" for num in (num1, num2, num3)]

        result = 0
        for i in range(4):
            digit = min(nums[0][i], nums[1][i], nums[2][i])
            if result > 0 or digit != "0":
                result = result * 10 + int(digit)

        return result


if __name__ == "__main__":
    # Test Cases
    assert Solution().generateKey(1, 10, 100) == 0
    assert Solution().generateKey(987, 879, 798) == 777
    assert Solution().generateKey(1, 2, 3) == 1

    print("All passed!")
