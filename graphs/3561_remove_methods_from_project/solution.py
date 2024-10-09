from collections import defaultdict


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        # Create a graph representation of method invocations
        graph = defaultdict(list)
        for caller, called in invocations:
            graph[caller].append(called)

        # Identify suspicious methods using DFS
        suspicious = set()

        def dfs(method):
            if method in suspicious:
                return
            suspicious.add(method)
            for called in graph[method]:
                dfs(called)

        dfs(k)

        # Check if any non-suspicious method invokes a suspicious method
        for method in range(n):
            if method not in suspicious:
                for called in graph[method]:
                    if called in suspicious:
                        return list(range(n))  # Can't remove suspicious methods

        # Remove suspicious methods
        return [method for method in range(n) if method not in suspicious]


if __name__ == "__main__":
    s = Solution()

    assert s.remainingMethods(4, 1, [[1, 2], [0, 1], [3, 2]]) == [0, 1, 2, 3]
    assert s.remainingMethods(5, 0, [[1, 2], [0, 2], [0, 1], [3, 4]]) == [3, 4]
    assert s.remainingMethods(3, 2, [[1, 2], [0, 1], [2, 0]]) == []

    print("All passed!")
