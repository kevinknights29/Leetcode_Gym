import heapq


class Solution:
    def resultsArray(self, queries: list[list[int]], k: int) -> list[int]:
        min_heap = []  # Stores k nearest obstacles
        max_heap = []  # Stores obstacles farther than kth nearest
        results = []

        for x, y in queries:
            distance = abs(x) + abs(y)

            if len(min_heap) < k:
                heapq.heappush(min_heap, -distance)  # Use negative for max heap behavior
            elif -distance > min_heap[0]:
                # Move the furthest of k nearest to max_heap
                popped = -heapq.heapreplace(min_heap, -distance)
                heapq.heappush(max_heap, popped)
            else:
                heapq.heappush(max_heap, distance)

            if len(min_heap) == k:
                results.append(-min_heap[0])
            else:
                results.append(-1)

        return results


# Time Complexity: O(n * log(k)), where n is the number of queries
# Space Complexity: O(n), as we store all obstacles in heaps


if __name__ == "__main__":
    # Test Cases
    assert Solution().resultsArray([[1, 2], [3, 4], [2, 3], [-3, 0]], 2) == [-1, 7, 5, 3]
    assert Solution().resultsArray([[5, 5], [4, 4], [3, 3]], 1) == [10, 8, 6]

    print("All passed!")
