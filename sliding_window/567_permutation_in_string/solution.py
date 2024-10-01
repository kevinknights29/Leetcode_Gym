class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge Case: If s1 is larger than s2
        if len(s1) > len(s2):
            return False

        # populate counters for both s1 and s2 from a to z
        s1_counter = {chr(ord("a") + i): 0 for i in range(26)}
        s2_counter = {chr(ord("a") + i): 0 for i in range(26)}

        # add values counts for first window of size len(s1)
        for i in range(len(s1)):
            s1_counter[s1[i]] = s1_counter.get(s1[i], 0) + 1
            s2_counter[s2[i]] = s2_counter.get(s2[i], 0) + 1

        # count the number of matches between the two counters for the first window
        matches = 0
        for i in range(26):
            letter = chr(ord("a") + i)
            if s1_counter[letter] == s2_counter[letter]:
                matches += 1

        # iterate over the remaining windows
        L = 0
        for R in range(len(s1), len(s2)):
            # check exit condition
            if matches == 26:
                return True

            # updates matches based on character entering the window
            letter = s2[R]
            s2_counter[letter] += 1
            if s2_counter[letter] == s1_counter[letter]:
                matches += 1
            elif s2_counter[letter] - 1 == s1_counter[letter]:
                matches -= 1

            # updates matches based on character leaving the window
            letter = s2[L]
            s2_counter[letter] -= 1
            if s2_counter[letter] == s1_counter[letter]:
                matches += 1
            elif s2_counter[letter] + 1 == s1_counter[letter]:
                matches -= 1

            L += 1

        # Return the result of total matches after last update
        return matches == 26


if __name__ == "__main__":
    s = Solution()

    assert s.checkInclusion("ab", "eidbaooo")
    assert not s.checkInclusion("ab", "eidboaoo")

    print("All Passed!")
