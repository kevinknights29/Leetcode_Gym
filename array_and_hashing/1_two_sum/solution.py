class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            if (target - nums[i]) in hashmap:
                return [hashmap[target - nums[i]], i]
            hashmap[nums[i]] = i


# Brute Force:
# - For each value in num perform a sum with each remaining value of the array.
# - Compare if sum matches target, if it does return those indexes as a result in an array format.
# T: O(n^2) | S: O(n)

# Things to consider:.
# - There is only oen solution
# - Not use the same element twice.

# Optimization:
# Create a hashmap to store values and indexes seen.
# Iterarte over nums array.
# Check if the difference between the current num and target have been seen.
#   - If so, return [hashmap[target - nums[i]], i]
#   - Else, add num and index to hashmap.
# T: O(n) | S: O(n)

if __name__ == "__main__":
    # Test Cases
    assert Solution().twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
    assert Solution().twoSum(nums=[3, 2, 4], target=6) == [1, 2]
    assert Solution().twoSum(nums=[3, 3], target=6) == [0, 1]
    assert Solution().twoSum(nums=[3, 0, 3], target=6) == [0, 2]

    print("All passed!")
