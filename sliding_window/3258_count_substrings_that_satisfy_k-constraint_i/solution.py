class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        count = 0
        # sliding window
        for L in range(len(s)):
            # set R to L, smallest substring is size 1 (one character)
            R = L
            # create variables track of characters within a substring
            zeros = ones = 0
            # iterate over the remaining characters from s
            while R < len(s):
                # track the current character count
                if s[R] == "0":
                    zeros += 1
                else:
                    ones += 1
                # check if the conditions holds for the current substring
                if min(zeros, ones) <= k:
                    count += 1
                    R += 1
                # if the condition is no longer valid for the current substring break the loop
                else:
                    break
        return count


if __name__ == "__main__":
    # Test Cases
    assert Solution().countKConstraintSubstrings("10101", 1) == 12
    assert Solution().countKConstraintSubstrings("1010101", 2) == 25
    assert Solution().countKConstraintSubstrings("11111", 1) == 15

    print("All passed!")
