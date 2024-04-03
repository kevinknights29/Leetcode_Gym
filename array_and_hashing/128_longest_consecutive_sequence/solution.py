class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hashset = set(nums)
        hashmap = {}
        longest = 0
        for n in hashset:
            lower = hashmap.get(n - 1, 0)
            upper = hashmap.get(n + 1, 0)
            val = lower + upper + 1
            hashmap[n - lower] = val
            hashmap[n + upper] = val
            longest = max(longest, val)
        return longest


if __name__ == "__main__":
    assert Solution().longestConsecutive(nums=[100, 4, 200, 1, 3, 2]) == 4
    assert Solution().longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9

    print("All passed!")
