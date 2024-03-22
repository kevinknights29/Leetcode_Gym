class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = [1] * len(nums)

        # prefix calculation
        for i in range(1, len(nums)):
            output[i] = nums[i - 1] * output[i - 1]

        # postfix calculation
        postfix = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output


# Brute Force:
# - Iterate over the array
# - Iterave over the sub array not containing current index (i+1:len(n))
# - Multiply each value with current value (starting at 1, mult *= num[j])
# - Append/insert multiplied value to the output array
# - Return output array
# T: O(n^2) | S: O(n) -> O(1) hence the output array does not count as extra space for space complexity analysis.

# Optimized solution:
# - Initialize the output array with 1s ensuring it has same size as nums.
# - Iterate over the nums array skipping the first element.
# - Compute the multiplication of the prefix for the current value and store it in output.
# - Initialize a variable postfix and set it to the last element of nums
# - Iterate over the nums array in reverse order skipping the first element (i=len(n)-1).
# - Compute the multiplication of the postfix and prefix for the current value and store it in output.
# - Increase postfix by multipliying it with the current value (element i)
# T: O(n) | S: O(1)

if __name__ == "__main__":
    # Test Cases
    assert Solution().productExceptSelf(nums=[1, 2, 3, 4]) == [24, 12, 8, 6]
    assert Solution().productExceptSelf(nums=[-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert Solution().productExceptSelf(nums=[0, 0, 0]) == [0, 0, 0]
    assert Solution().productExceptSelf(nums=[-1, 1]) == [1, -1]

    print("All passed!")
