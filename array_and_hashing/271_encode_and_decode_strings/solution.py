class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        enc = ""
        delimeter = "#"
        for s in strs:
            enc += f"{len(s)}{delimeter}{s}"
        return enc

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        dec = []
        delimeter = "#"
        i, j = 0, 0
        while j < len(s):
            if s[j] == delimeter:
                len_s = int(s[i:j])
                dec.append(s[j + 1 : j + len_s + 1])
                i = j + len_s + 1
                j = i
            else:
                j += 1
        return dec


if __name__ == "__main__":
    codec = Codec()
    strs = ["Hello", "World"]
    assert codec.decode(codec.encode(strs)) == strs
    print("Passed all tests!")
