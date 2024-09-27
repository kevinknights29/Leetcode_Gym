class Solution:
    def reportSpam(self, message: list[str], bannedWords: list[str]) -> bool:
        # exhaustive search: traverse messages list
        # and perform a membership test in banned words.
        hashset = set(bannedWords)
        return len([word for word in message if word in hashset]) >= 2


if __name__ == "__main__":
    s = Solution()

    assert s.reportSpam(["hello", "world", "leetcode"], ["world", "hello"])
    assert not s.reportSpam(["hello", "programming", "fun"], ["world", "programming", "leetcode"])

    print("All Passed!")
