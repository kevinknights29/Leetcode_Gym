class Solution:
    def maximumTotalSum(self, maximumHeight: list[int]) -> int:
        # Sort the heights in descending order
        maximumHeight.sort(reverse=True)

        total_sum = 0
        prev_height = float("inf")  # Initialize with infinity to allow the first height to be maximum

        for max_height in maximumHeight:
            # Choose the smaller of max_height and (prev_height - 1)
            current_height = min(max_height, prev_height - 1)

            # If we can't assign a positive height, it's impossible
            if current_height <= 0:
                return -1

            total_sum += current_height
            prev_height = current_height

        return total_sum


if __name__ == "__main__":
    s = Solution()

    assert s.maximumTotalSum([2, 3, 4, 3]) == 10
    assert s.maximumTotalSum([15, 10]) == 25
    assert s.maximumTotalSum([2, 2, 1]) == -1

    print("All passed!")
