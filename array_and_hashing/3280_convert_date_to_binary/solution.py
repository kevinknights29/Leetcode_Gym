class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return "-".join([bin(int(c))[2:] for c in date.split("-")])


if __name__ == "__main__":
    # Test Cases
    assert Solution().convertDateToBinary("2080-02-29") == "100000100000-10-11101"
    assert Solution().convertDateToBinary("1900-01-01") == "11101101100-1-1"

    print("All passed!")
