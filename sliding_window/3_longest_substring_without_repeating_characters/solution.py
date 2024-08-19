class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # best case
        if len(s) <= 1:
            return len(s)

        # iterave over the string
        L = 0
        hashset = set()
        max_length = 0
        for R in range(len(s)):
            # check if character exist in hashset
            while s[R] in hashset:
                hashset.remove(s[L])
                L += 1
            # add character to hashset
            hashset.add(s[R])
            # update max lenght
            max_length = max(max_length, len(hashset))
        return max_length


if __name__ == "__main__":
    # Test Cases
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3

    print("All passed!")
