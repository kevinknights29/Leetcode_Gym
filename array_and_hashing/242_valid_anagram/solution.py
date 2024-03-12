class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashmap = {}
        t_hashmap = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            s_hashmap[s[i]] = s_hashmap.get(s[i], 0) + 1
            t_hashmap[t[i]] = t_hashmap.get(t[i], 0) + 1

            # NOTE: adaptation for unicode characters
            # s_hashmap[ord(s[i])] = s_hashmap.get(ord(s[i]), 0) + 1
            # t_hashmap[ord(t[i])] = t_hashmap.get(ord(t[i]), 0) + 1

        for key in s_hashmap:
            if s_hashmap[key] != t_hashmap.get(key, 0):
                return False
        return True


# Brute Force:
# - For each letter in s, I search for an equivalent in t (full scan).
# - Remove the matching letter from t.
# T: O(n^2) | S: O(1)

# Optimization #1:
# - Sort each array (s, t).
# - For each letter in s in index i match with letter on index i in t
# T: O(nlog(n)) | S: O(1)

# Optimization #2:
# - Create a hashmap to count each ocurrance of a letter in s and t.
# - For each letter in s increase 1 the value of the hashmap.
# - For each letter in t increase 1 the value of the hashmap.
# - Compare each value in the hashmap.
# T: O(n) | S: O(n)

if __name__ == "__main__":
    # Test Cases
    assert Solution().isAnagram(s="anagram", t="nagaram")
    assert not Solution().isAnagram(s="rat", t="car")
    assert Solution().isAnagram(s="a", t="a")
    assert not Solution().isAnagram(s="anagram", t="na")
    assert not Solution().isAnagram(s="an", t="nagaram")

    print("All passed!")
