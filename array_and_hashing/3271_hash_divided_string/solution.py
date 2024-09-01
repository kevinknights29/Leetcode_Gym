class Solution:
    def stringHash(self, s: str, k: int) -> str:
        return "".join(chr((sum(ord(c) - 97 for c in s[i : i + k]) % 26) + 97) for i in range(0, len(s), k))


if __name__ == "__main__":
    # Test Cases
    assert Solution().stringHash("abcd", 2) == "bf"
    assert Solution().stringHash("mxz", 3) == "i"

    print("All passed!")
