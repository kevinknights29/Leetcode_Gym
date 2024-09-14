# 3286. Find a Safe Walk Through a Grid

## Description

You are given an `m x n` binary matrix `grid` and an integer `health`.

You start on the upper-left corner `(0, 0)` and would like to get to the lower-right corner `(m - 1, n - 1)`.

You can move up, down, left, or right from one cell to another adjacent cell as long as your health remains positive.

`Cells (i, j)` with `grid[i][j] = 1` are considered unsafe and reduce your health by 1.

Return `true` if you can reach the final cell with a health value of 1 or more, and `false` otherwise.

## Examples

Example 1:

```bash
Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1

Output: true

Explanation:

The final cell can be reached safely by walking along the gray cells below.
```

![image](https://assets.leetcode.com/uploads/2024/08/04/3868_examples_1drawio.png)

Example 2:

```bash
Input: grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3

Output: false

Explanation:

A minimum of 4 health points is needed to reach the final cell safely.
```

![image](https://assets.leetcode.com/uploads/2024/08/04/3868_examples_2drawio.png)

Example 3:

```bash
Input: grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5

Output: true

Explanation:

The final cell can be reached safely by walking along the gray cells below.
```

![image](https://assets.leetcode.com/uploads/2024/08/04/3868_examples_3drawio.png)

```bash
Any path that does not go through the cell (1, 1) is unsafe since your health will drop to 0 when reaching the final cell.
```

## Constraints

- `m == grid.length`

- `n == grid[i].length`

- `1 <= m, n <= 50`

- `2 <= m * n`

- `1 <= health <= m + n`

- `grid[i][j]` is either 0 or 1.

## Solution

[![Python](https://img.shields.io/badge/-Python-black?style=for-the-badge&logo=python)](./solution.py):w
