import heapq


class Solution:
    def minimumSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        # Initialize the heap with (cost, number_used, worker_time) for each worker
        heap = [(worker_time, 1, worker_time) for worker_time in workerTimes]
        heapq.heapify(heap)

        max_time = 0
        for _ in range(mountainHeight):
            cost, number_used, worker_time = heapq.heappop(heap)
            max_time = max(max_time, cost)

            # Calculate the new cost and number_used for this worker
            new_cost = cost + (number_used + 1) * worker_time
            new_number_used = number_used + 1

            # Push the updated tuple back to the heap
            heapq.heappush(heap, (new_cost, new_number_used, worker_time))

        return max_time


if __name__ == "__main__":
    s = Solution()

    assert s.minimumSeconds(4, [2, 1, 1]) == 3
    assert s.minimumSeconds(10, [3, 2, 2, 4]) == 12
    assert s.minimumSeconds(5, [1]) == 15

    print("All Passed!")
