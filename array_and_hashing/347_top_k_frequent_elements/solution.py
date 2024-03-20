class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}
        array = [[] for _ in range(len(nums) + 1)]
        result = []
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        for num, count in hashmap.items():
            array[count].append(num)
        for i in range(len(nums), 0, -1):
            if array[i]:
                for value in array[i]:
                    result.append(value)
            if len(result) == k:
                return result


# Brute Force:
# - Create a hashmap to count the ocurrence of each number.
# - Iterate over the array.
# - Count the ocurrence of each number.
# - Sort the values (ocurrances) of the hashmap.
# - Return the k first elements.
# T: O(n ^ 2 log (n)) | S: O(n)

# Optimization - Remove the sort
# - Create a hashmap to count the ocurrence of each number.
# - Iterate over the array.
# - Count the ocurrence of each number.
# - Insert number to the position matching the count.
# - Iterate over the array in reverse order (bigger first).
# - Check if array at that possition is not empty.
# - Iterate over each value at that position array.
# - Add to result
# If Results' length is equal to k, return result
# Return the result array.
# T: O(n) | S: O(n)

if __name__ == "__main__":
    # Test Cases:
    assert Solution().topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2) == [1, 2]
    assert Solution().topKFrequent(nums=[1, 1, 3], k=1) == [1]
    assert Solution().topKFrequent(nums=[1], k=1) == [1]
    assert Solution().topKFrequent(nums=[1, 2, 3], k=3) == [1, 2, 3]
    assert Solution().topKFrequent(nums=[3, 0, 1, 0], k=1) == [0]
    assert Solution().topKFrequent(nums=[4, 1, -1, 2, -1, 2, 3], k=2) == [-1, 2]

    print("All passed!")
