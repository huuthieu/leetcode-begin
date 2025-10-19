/**
 * LeetCode 200: Number of Islands
 *
 * Problem:
 * Given an m x n 2D binary grid where '1' represents land and '0' represents water,
 * return the number of islands. An island is surrounded by water and is formed by connecting
 * adjacent lands horizontally or vertically.
 *
 * Example:
 * grid = [
 *   ["1","1","1","1","0"],
 *   ["1","1","0","1","0"],
 *   ["1","1","0","0","0"],
 *   ["0","0","0","0","0"]
 * ]
 * Output: 1
 */

import java.util.LinkedList;
import java.util.Queue;

public class NumberOfIslands {

    // Approach 1: DFS (Depth-First Search)
    public static int numIslands_DFS(char[][] grid) {
        /**
         * Use DFS to explore each connected component
         * Time: O(m*n), Space: O(m*n) for recursion stack
         */
        if (grid == null || grid.length == 0) return 0;

        int rows = grid.length;
        int cols = grid[0].length;
        int islandCount = 0;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == '1') {
                    islandCount++;
                    dfs(grid, i, j, rows, cols);
                }
            }
        }

        return islandCount;
    }

    private static void dfs(char[][] grid, int r, int c, int rows, int cols) {
        // Base cases
        if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == '0') {
            return;
        }

        // Mark as visited
        grid[r][c] = '0';

        // Explore all 4 directions
        dfs(grid, r + 1, c, rows, cols); // down
        dfs(grid, r - 1, c, rows, cols); // up
        dfs(grid, r, c + 1, rows, cols); // right
        dfs(grid, r, c - 1, rows, cols); // left
    }

    // Approach 2: BFS (Breadth-First Search)
    public static int numIslands_BFS(char[][] grid) {
        /**
         * Use BFS with a queue to explore each connected component
         * Time: O(m*n), Space: O(min(m,n)) for queue
         */
        if (grid == null || grid.length == 0) return 0;

        int rows = grid.length;
        int cols = grid[0].length;
        int islandCount = 0;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == '1') {
                    islandCount++;
                    bfs(grid, i, j, rows, cols);
                }
            }
        }

        return islandCount;
    }

    private static void bfs(char[][] grid, int startR, int startC, int rows, int cols) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{startR, startC});
        grid[startR][startC] = '0';

        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int r = cell[0];
            int c = cell[1];

            for (int[] dir : directions) {
                int nr = r + dir[0];
                int nc = c + dir[1];

                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == '1') {
                    grid[nr][nc] = '0';
                    queue.offer(new int[]{nr, nc});
                }
            }
        }
    }

    // Test Cases
    public static void main(String[] args) {
        char[][][] testCases = {
            {
                {'1', '1', '1', '1', '0'},
                {'1', '1', '0', '1', '0'},
                {'1', '1', '0', '0', '0'},
                {'0', '0', '0', '0', '0'}
            },
            {
                {'1', '1', '0', '0', '0'},
                {'1', '1', '0', '0', '0'},
                {'0', '0', '1', '0', '0'},
                {'0', '0', '0', '1', '1'}
            },
            {
                {'1', '0', '1'},
                {'0', '1', '0'},
                {'1', '0', '1'}
            },
            {{'1'}}
        };

        int[] expectedResults = {1, 4, 5, 1};

        for (int i = 0; i < testCases.length; i++) {
            char[][] grid1 = copyGrid(testCases[i]);
            char[][] grid2 = copyGrid(testCases[i]);

            int result_dfs = numIslands_DFS(grid1);
            int result_bfs = numIslands_BFS(grid2);
            int expected = expectedResults[i];

            assert result_dfs == expected : "DFS failed";
            assert result_bfs == expected : "BFS failed";

            System.out.println("Test case " + i + ": " + expected + " islands ✓");
        }

        System.out.println("\nAll tests passed!");
    }

    private static char[][] copyGrid(char[][] grid) {
        char[][] copy = new char[grid.length][];
        for (int i = 0; i < grid.length; i++) {
            copy[i] = grid[i].clone();
        }
        return copy;
    }
}
