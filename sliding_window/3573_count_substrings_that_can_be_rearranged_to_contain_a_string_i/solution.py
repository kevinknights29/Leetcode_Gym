from collections import Counter


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        n = len(word1)

        # Calculate frequency of characters in word2
        target_freq = Counter(word2)
        required_chars = len(target_freq)

        # Initialize sliding window variables
        window = Counter()
        matched_chars = 0
        left = 0
        count = 0

        for right in range(n):
            # Expand window
            if word1[right] in target_freq:
                window[word1[right]] += 1
                if window[word1[right]] == target_freq[word1[right]]:
                    matched_chars += 1

            # Check if window is valid and count substrings
            while matched_chars == required_chars:
                count += n - right

                # Contract window
                if word1[left] in target_freq:
                    if window[word1[left]] == target_freq[word1[left]]:
                        matched_chars -= 1
                    window[word1[left]] -= 1
                left += 1

        return count


if __name__ == "__main__":
    s = Solution()

    assert s.validSubstringCount("bcca", "abc") == 1
    assert s.validSubstringCount("abcabc", "abc") == 10
    assert s.validSubstringCount("abcabc", "aaabc") == 0

    print("All Passed!")
