import heapq


class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        # Create a min-heap with (value, index) pairs
        heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)  # O(n)

        for _ in range(k):
            # Get the minimum element
            min_val, min_idx = heapq.heappop(heap)  # O(log n)

            # Update the value
            new_val = min_val * multiplier
            nums[min_idx] = new_val

            # Push the updated value back to the heap
            heapq.heappush(heap, (new_val, min_idx))  # O(log n)

        return nums


if __name__ == "__main__":
    # Test Cases
    assert Solution().getFinalState([2, 1, 3, 5, 6], 5, 2) == [8, 4, 6, 5, 6]
    assert Solution().getFinalState([1, 2], 3, 4) == [16, 8]

    print("All passed!")
