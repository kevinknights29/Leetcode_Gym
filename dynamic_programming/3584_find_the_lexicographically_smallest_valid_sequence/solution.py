class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        m, n = len(word1), len(word2)
        # Step 1: Build the DP array
        # dp[j] stores the rightmost index in word1 that matches word2[j]
        dp = [-1] * (n + 1)
        dp[n] = n + 1  # Sentinel value for easier processing

        # Iterate from right to left to fill the DP array
        i, j = m - 1, n - 1
        while j >= 0:
            # Find the rightmost matching character in word1 for word2[j]
            while i >= 0 and word1[i] != word2[j]:
                i -= 1
            if i < 0:
                break  # No more matches possible
            dp[j] = i
            i -= 1
            j -= 1

        # Step 2: Construct the result
        result = []
        i, j = 0, 0
        mismatch_used = False

        while j < n:
            if i >= m:
                return []  # Reached end of word1 before matching all of word2

            if word1[i] == word2[j]:
                # Characters match, add current index to result
                result.append(i)
                i += 1
            else:
                if not mismatch_used and dp[j + 1] >= i + 1:
                    # Use the mismatch here as there's a valid future match
                    # This ensures lexicographically smallest sequence
                    result.append(i)
                    mismatch_used = True
                    i += 1
                else:
                    # Find the next matching character in word1
                    while i < m and word1[i] != word2[j]:
                        i += 1
                    if i >= m:
                        return []  # No valid sequence possible
                    result.append(i)
                    i += 1

            j += 1

        return result


if __name__ == "__main__":
    s = Solution()

    assert s.validSequence("vbcca", "abc") == [0, 1, 2]
    assert s.validSequence("bacdc", "abc") == [1, 2, 4]
    assert s.validSequence("aaaaaa", "aaabc") == []
    assert s.validSequence("abc", "ab") == [0, 1]

    print("All passed!")
