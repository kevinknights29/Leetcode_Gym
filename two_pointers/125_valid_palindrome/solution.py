class Solution:
    def isPalindrome(self, s: str) -> bool:
        # edge case
        if len(s) < 2:
            return True

        # clean s
        s_clean = ""
        for letter in s:
            if letter.isalnum():
                s_clean += letter.lower()

        # check palindrome with two pointers
        L = 0
        R = len(s_clean) - 1
        while R > L:
            if s_clean[L] != s_clean[R]:
                return False
            L += 1
            R -= 1
        return True


if __name__ == "__main__":
    assert Solution().isPalindrome("A man, a plan, a canal: Panama")
    assert not Solution().isPalindrome("race a car")
    assert Solution().isPalindrome(" ")

    print("Passed all tests!")
