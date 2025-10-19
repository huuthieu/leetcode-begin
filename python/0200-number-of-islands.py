"""
LeetCode 200: Number of Islands

Problem:
Given an m x n 2D binary grid grid where '1' represents land and '0' represents water,
return the number of islands. An island is surrounded by water and is formed by connecting
adjacent lands horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

Example:
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Time Complexity: O(m * n)
Space Complexity: O(m * n) for recursion stack or queue
"""


# Approach 1: DFS (Depth-First Search)
def numIslands_DFS(grid):
    """
    Use DFS to explore each connected component.
    Mark visited cells as '0' to avoid revisiting.
    Count each connected component as one island.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    island_count = 0

    def dfs(r, c):
        # Base cases: out of bounds or water or already visited
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
            return

        # Mark as visited
        grid[r][c] = "0"

        # Explore all 4 directions
        dfs(r + 1, c)  # down
        dfs(r - 1, c)  # up
        dfs(r, c + 1)  # right
        dfs(r, c - 1)  # left

    # Iterate through grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                island_count += 1
                dfs(i, j)

    return island_count


# Approach 2: BFS (Breadth-First Search)
def numIslands_BFS(grid):
    """
    Use BFS to explore each connected component using a queue.
    Similar to DFS but uses iterative approach with a queue.
    """
    if not grid or not grid[0]:
        return 0

    from collections import deque

    rows, cols = len(grid), len(grid[0])
    island_count = 0

    def bfs(start_r, start_c):
        queue = deque([(start_r, start_c)])
        grid[start_r][start_c] = "0"

        while queue:
            r, c = queue.popleft()

            # Explore all 4 directions
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                    grid[nr][nc] = "0"
                    queue.append((nr, nc))

    # Iterate through grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                island_count += 1
                bfs(i, j)

    return island_count


# Approach 3: Union-Find (Disjoint Set Union)
def numIslands_UnionFind(grid):
    """
    Use Union-Find data structure to group connected cells.
    Time: O(m*n * α(m*n)) where α is inverse Ackermann function (nearly O(1))
    Space: O(m*n)
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    parent = {}

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    def union(x, y):
        root_x, root_y = find(x), find(y)
        if root_x != root_y:
            parent[root_x] = root_y

    # Initialize parent for all land cells
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                parent[(i, j)] = (i, j)

    # Union adjacent land cells
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                # Check right and down neighbors
                if j + 1 < cols and grid[i][j + 1] == "1":
                    union((i, j), (i, j + 1))
                if i + 1 < rows and grid[i + 1][j] == "1":
                    union((i, j), (i + 1, j))

    # Count unique root parents
    return len(set(find((i, j)) for i in range(rows) for j in range(cols) if grid[i][j] == "1"))


# Test Cases
def test_numIslands():
    test_cases = [
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
        ),
        (
            [
                ["1", "0", "1"],
                ["0", "1", "0"],
                ["1", "0", "1"],
            ],
            5,
        ),
        ([["1"]], 1),
        ([["0"]], 0),
    ]

    for grid, expected in test_cases:
        # DFS
        grid_copy1 = [row[:] for row in grid]
        result_dfs = numIslands_DFS(grid_copy1)

        # BFS
        grid_copy2 = [row[:] for row in grid]
        result_bfs = numIslands_BFS(grid_copy2)

        # Union-Find
        grid_copy3 = [row[:] for row in grid]
        result_uf = numIslands_UnionFind(grid_copy3)

        assert (
            result_dfs == expected
        ), f"DFS failed: got {result_dfs}, expected {expected}"
        assert (
            result_bfs == expected
        ), f"BFS failed: got {result_bfs}, expected {expected}"
        assert (
            result_uf == expected
        ), f"UnionFind failed: got {result_uf}, expected {expected}"

        print(f"Expected {expected} islands ✓")


if __name__ == "__main__":
    test_numIslands()
    print("\nAll tests passed!")
