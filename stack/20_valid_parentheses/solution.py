class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for c in s:
            if c in close_to_open:
                if len(stack) == 0 or stack[-1] != close_to_open[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return True if len(stack) == 0 else False


if __name__ == "__main__":
    # Test Cases
    assert Solution().isValid("()")
    assert Solution().isValid("()[]{}")
    assert not Solution().isValid("(]")
    assert Solution().isValid("{[((()))]}")

    print("All passed!")
