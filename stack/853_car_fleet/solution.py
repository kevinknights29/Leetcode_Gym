class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = []
        array = sorted(list(zip(position, speed)), reverse=True)
        for p, s in array:
            t = (target - p) / s
            if stack and stack[-1] >= t:
                continue
            else:
                stack.append(t)
        return len(stack)


if __name__ == "__main__":
    # Test Cases
    assert (
        Solution().carFleet(
            target=12,
            position=[10, 8, 0, 5, 3],
            speed=[2, 4, 1, 1, 3],
        )
        == 3
    )
    assert (
        Solution().carFleet(
            target=10,
            position=[3],
            speed=[3],
        )
        == 1
    )
    assert (
        Solution().carFleet(
            target=100,
            position=[0, 2, 4],
            speed=[4, 2, 1],
        )
        == 1
    )

    print("All passed")
