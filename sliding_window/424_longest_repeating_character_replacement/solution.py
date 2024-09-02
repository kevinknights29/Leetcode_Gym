class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        max_freq = 0
        max_length = 0
        hashmap = {}

        # iterate over characters in s
        for R in range(len(s)):
            # store current character in hashmap to track its count
            hashmap[s[R]] = hashmap.get(s[R], 0) + 1

            # update the highest count seen
            max_freq = max(max_freq, hashmap[s[R]])

            # check if swaps have been exceeded in the current substring
            while (R - L + 1) - max_freq > k:
                # remove starting character from hashmap
                hashmap[s[L]] -= 1
                # shift to next character
                L += 1

            # calculate the length of the subtring, and see if it's the longest
            max_length = max(max_length, R - L + 1)

        return max_length


if __name__ == "__main__":
    # Test Cases
    assert Solution().characterReplacement("ABAB", 2) == 4
    assert Solution().characterReplacement("AABABBA", 1) == 4

    print("All passed!")
