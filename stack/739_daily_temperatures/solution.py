class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stack_i, _ = stack.pop()
                answer[stack_i] = i - stack_i
            stack.append([i, t])

        return answer


if __name__ == "__main__":
    # Test Cases
    assert Solution().dailyTemperatures(
        [
            73,
            74,
            75,
            71,
            69,
            72,
            76,
            73,
        ],
    ) == [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0,
    ]

    assert Solution().dailyTemperatures(
        [
            30,
            40,
            50,
            60,
        ],
    ) == [
        1,
        1,
        1,
        0,
    ]
    assert Solution().dailyTemperatures(
        [
            30,
            60,
            90,
        ],
    ) == [
        1,
        1,
        0,
    ]

    print("All passed")
