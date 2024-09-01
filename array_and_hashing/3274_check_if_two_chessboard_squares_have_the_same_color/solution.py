class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        # Logic:
        # ord("a") -> 97; ord("1") -> 49; ord("a1") = 97 + 49 = 146 % 2 == 0: black, else white

        return sum(map(ord, coordinate1)) % 2 == sum(map(ord, coordinate2)) % 2

        # Time: O(1)
        # Space: O(1)


if __name__ == "__main__":
    # Test Cases
    assert Solution().checkTwoChessboards("a1", "c3")
    assert not Solution().checkTwoChessboards("a1", "h3")

    print("All passed!")
