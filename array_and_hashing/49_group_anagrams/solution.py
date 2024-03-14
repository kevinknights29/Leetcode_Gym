class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        results = []
        anagrams = set()
        for i in range(len(strs)):
            if strs[i] in anagrams:
                continue
            run = [strs[i]]
            for j in range(i + 1, len(strs)):
                if len(strs[i]) != len(strs[j]):
                    continue
                hashmap_i = {}
                hashmap_j = {}
                for k in range(len(strs[i])):
                    hashmap_i[strs[i][k]] = hashmap_i.get(strs[i][k], 0) + 1
                    hashmap_j[strs[j][k]] = hashmap_j.get(strs[j][k], 0) + 1
                match = True
                for char in hashmap_i:
                    if hashmap_i[char] != hashmap_j.get(char, 0):
                        match = False
                        break
                if match:
                    run.append(strs[j])
                    anagrams.add(strs[i])
                    anagrams.add(strs[j])
            results.append(run)
        return results


# Brute Force:
# - For each value in strs compare it to the remaining values in strs.
# - To check if values are anagram, store each character and value in a hasmap
#       then compare the counts for each char, if they match for all char is an anagram.
# - Track anagrams found in an array and later instert it to the result array (return).
# - Track anagrams found in a set, and skip those values.
# T: O(n^3) | S: O(n^2)

# Optimization:

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
