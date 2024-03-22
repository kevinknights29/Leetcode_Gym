class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = []
        count_0 = 0
        multiplication = 1

        for num in nums:
            if num == 0:
                count_0 += 1
            else:
                multiplication *= num
            if count_0 > 1:
                return [0] * len(nums)

        for num in nums:
            if count_0 > 0:
                if num == 0:
                    output.append(multiplication)
                else:
                    output.append(0)
            else:
                output.append(multiplication // num)
        return output


# Brute Force:
# - Iterate over the array
# - Iterave over the sub array not containing current index (i+1:len(n))
# - Multiply each value with current value (starting at 1, mult *= num[j])
# - Append/insert multiplied value to the output array
# - Return output array
# T: O(n^2) | S: O(n) -> O(1) hence the output array does not count as extra space for space complexity analysis.

# Optimized solution:
# - Iterate over the array
# - Compute the multiplication of all values of the array (starting at 1, mult *= num[j])
# - If there is only one 0 present:
#   - ignore it, this will be our non-zero result.
#   - set exist_0 to True.
# - If there is more than one 0:
#   - return [0] * len(nums)
# - Iterate over the array (again - not nested)
# - If exist_0 is not True:
#   - Divide current value from the multiplied total and append/insert to output array
# - Else, return 0 for every value that is not the 0 and append the multiplied total for 0.
# T: O(n) | S: O(1)

if __name__ == "__main__":
    # Test Cases
    assert Solution().productExceptSelf(nums=[1, 2, 3, 4]) == [24, 12, 8, 6]
    assert Solution().productExceptSelf(nums=[-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert Solution().productExceptSelf(nums=[0, 0, 0]) == [0, 0, 0]
    assert Solution().productExceptSelf(nums=[-1, 1]) == [1, -1]

    print("All passed!")
