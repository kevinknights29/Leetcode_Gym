from collections import deque


class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        # Define directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Use a queue for BFS
        queue = deque([(0, 0, health)])

        # Use a set to keep track of visited states
        visited = set([(0, 0, health)])

        while queue:
            i, j, current_health = queue.popleft()

            # Calculate health after entering the current cell
            current_health -= grid[i][j]

            # If health becomes 0 or negative, continue to the next iteration
            if current_health <= 0:
                continue

            # If we've reached the bottom-right corner with health > 0, return True
            if i == m - 1 and j == n - 1:
                return True

            # Explore all four directions
            for di, dj in directions:
                ni, nj = i + di, j + dj

                # Check if the new position is within the grid
                if 0 <= ni < m and 0 <= nj < n:
                    # If this state hasn't been visited
                    if (ni, nj, current_health) not in visited:
                        queue.append((ni, nj, current_health))
                        visited.add((ni, nj, current_health))

        # If we've explored all possible paths and haven't reached the end, return False
        return False


if __name__ == "__main__":
    # Test Cases
    assert Solution().findSafeWalk([[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], 1)
    assert not Solution().findSafeWalk(
        [[0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 0]], 3
    )

    print("All passed")
