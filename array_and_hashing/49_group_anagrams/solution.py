from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            anagrams[tuple(count)].append(s)
        return list(anagrams.values())


# Brute Force:
# - For each value in strs compare it to the remaining values in strs.
# - To check if values are anagram, store each character and value in a hasmap
#       then compare the counts for each char, if they match for all char is an anagram.
# - Track anagrams found in an array and later instert it to the result array (return).
# - Track anagrams found in a set, and skip those values.
# T: O(n^2 * k) | S: O(n * k)

# Optimization:
# - Create a hashmap to count the characters in each value in strs.
# - For each value in strs, create an array to store the count for each character from a-z.
# - Use the array as a key to store the values in a hashmap.
# - Return the values in the hashmap.
# T: O(n * k) | S: O(n * k)

if __name__ == "__main__":
    # Test Cases
    assert Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["eat", "tea", "ate"],
        ["tan", "nat"],
        ["bat"],
    ]
    assert Solution().groupAnagrams([""]) == [[""]]
    assert Solution().groupAnagrams(["a"]) == [["a"]]

    print("All passed!")
