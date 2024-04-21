import math


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operands = []
        operators = {"+", "-", "*", "/"}
        for t in tokens:
            if t in operators:
                arg_1 = operands.pop()
                arg_2 = operands.pop()
                if t == "+":
                    result = arg_2 + arg_1
                elif t == "-":
                    result = arg_2 - arg_1
                elif t == "*":
                    result = arg_2 * arg_1
                else:
                    result = arg_2 / arg_1
                    if result >= 0:
                        result = math.floor(result)
                    else:
                        result = math.ceil(result)
                operands.append(result)
            else:
                operands.append(int(t))
        return operands.pop()


if __name__ == "__main__":
    # Test Cases
    assert Solution().evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert Solution().evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert (
        Solution().evalRPN(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        )
        == 22
    )

    print("All passed")
