class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        results = []

        def backtracking(open_parantheses, closed_parenthesis):
            if open_parantheses == closed_parenthesis == n:
                results.append("".join(stack))
                return

            if open_parantheses < n:
                stack.append("(")
                backtracking(open_parantheses + 1, closed_parenthesis)
                stack.pop()

            if closed_parenthesis < open_parantheses:
                stack.append(")")
                backtracking(open_parantheses, closed_parenthesis + 1)
                stack.pop()

        backtracking(0, 0)
        return results


if __name__ == "__main__":
    # Test Cases
    assert Solution().generateParenthesis(3) == [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()",
    ]
    assert Solution().generateParenthesis(2) == ["(())", "()()"]
    assert Solution().generateParenthesis(1) == ["()"]

    print("All passed")
