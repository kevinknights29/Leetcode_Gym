class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False


# Notes:
# Brute Force: For each num check the rest of the arry to find twin.           T: O(n^2) | S: O(1)
# Optimization: Add a counter (hashmap) and check if num has appeared already. T: O(n)   | S: O(n)
# Optimization: Use a set (hashset) and check if num has appeared already.     T: O(n)   | S: O(n)
# Alternative: Convert list to set and check lengths.                          T: O(n)   | S: O(1)

if __name__ == "__main__":
    # Test Cases:
    assert Solution().containsDuplicate([1, 2, 3, 1])
    assert not Solution().containsDuplicate([1, 2, 3, 4])
    assert Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    assert not Solution().containsDuplicate([1])
    assert not Solution().containsDuplicate([1, -2])

    print("All passed!")
