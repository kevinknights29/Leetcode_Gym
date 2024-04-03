class Solution:
    def isPalindrome(self, s: str) -> bool:
        # edge case
        if len(s) < 2:
            return True

        # clean s
        s_clean = ""
        for l in s:
            if l.isalnum():
                s_clean += l.lower()

        # check palindrome with two pointers
        l = 0
        r = len(s_clean) - 1
        while r > l:
            if s_clean[l] != s_clean[r]:
                return False
            l += 1
            r -= 1
        return True


if __name__ == "__main__":
    assert Solution().isPalindrome("A man, a plan, a canal: Panama")
    assert not Solution().isPalindrome("race a car")
    assert Solution().isPalindrome(" ")

    print("Passed all tests!")
