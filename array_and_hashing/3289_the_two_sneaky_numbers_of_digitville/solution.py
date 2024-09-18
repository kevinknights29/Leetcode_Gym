from collections import Counter


class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        # We need to traverse the list O(n)
        # Need to store repeated numbers in an array O(2) => O(1).
        # Approaches:
        # 1. Create a hashset to store unique numbers, making space: O(n)
        # 2. Count elements with a hashmap, and retrieve all keys with values 2, making space: O(n)

        # Count the occurrences of each number
        count = Counter(nums)

        # Return the numbers that appear twice
        return [num for num, freq in count.items() if freq == 2]


if __name__ == "__main__":
    # Test Cases
    assert sorted(Solution().getSneakyNumbers([0, 1, 1, 0])) == [0, 1]
    assert sorted(Solution().getSneakyNumbers([0, 3, 2, 1, 3, 2])) == [2, 3]
    assert sorted(Solution().getSneakyNumbers([7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2])) == [4, 5]

    print("All passed!")
