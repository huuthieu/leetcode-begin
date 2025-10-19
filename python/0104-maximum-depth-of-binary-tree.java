/**
 * LeetCode 104: Maximum Depth of Binary Tree
 *
 * Problem:
 * Given the root of a binary tree, return its maximum depth.
 *
 * Example:
 * Input: root = [3,9,20,null,null,15,7]
 * Output: 3
 */

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class MaximumDepthOfBinaryTree {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {}

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    // Approach 1: DFS - Recursive
    public static int maxDepth_DFS(TreeNode root) {
        /**
         * Recursively find maximum depth
         * Time: O(n), Space: O(h) for recursion stack
         */
        if (root == null) return 0;

        return 1 + Math.max(maxDepth_DFS(root.left), maxDepth_DFS(root.right));
    }

    // Approach 2: BFS - Level Order Traversal
    public static int maxDepth_BFS(TreeNode root) {
        /**
         * Use BFS with queue
         * Time: O(n), Space: O(w) where w = max width
         */
        if (root == null) return 0;

        Queue<TreeNode> queue = new LinkedList<>();
        Queue<Integer> depths = new LinkedList<>();

        queue.offer(root);
        depths.offer(1);

        int maxDepth = 0;

        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            int depth = depths.poll();

            maxDepth = Math.max(maxDepth, depth);

            if (node.left != null) {
                queue.offer(node.left);
                depths.offer(depth + 1);
            }
            if (node.right != null) {
                queue.offer(node.right);
                depths.offer(depth + 1);
            }
        }

        return maxDepth;
    }

    // Approach 3: BFS - Counting Levels
    public static int maxDepth_BFS_Levels(TreeNode root) {
        /**
         * BFS counting levels as we traverse
         * Time: O(n), Space: O(w)
         */
        if (root == null) return 0;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int depth = 0;

        while (!queue.isEmpty()) {
            depth++;
            int levelSize = queue.size();

            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();

                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
        }

        return depth;
    }

    // Approach 4: DFS - Iterative with Stack
    public static int maxDepth_DFS_Iterative(TreeNode root) {
        /**
         * Iterative DFS using stack
         * Time: O(n), Space: O(h)
         */
        if (root == null) return 0;

        Stack<TreeNode> nodeStack = new Stack<>();
        Stack<Integer> depthStack = new Stack<>();

        nodeStack.push(root);
        depthStack.push(1);

        int maxDepth = 0;

        while (!nodeStack.isEmpty()) {
            TreeNode node = nodeStack.pop();
            int depth = depthStack.pop();

            maxDepth = Math.max(maxDepth, depth);

            if (node.right != null) {
                nodeStack.push(node.right);
                depthStack.push(depth + 1);
            }
            if (node.left != null) {
                nodeStack.push(node.left);
                depthStack.push(depth + 1);
            }
        }

        return maxDepth;
    }

    // Test Cases
    public static void main(String[] args) {
        // Create test cases manually
        TreeNode test1 = new TreeNode(3);
        test1.left = new TreeNode(9);
        test1.right = new TreeNode(20);
        test1.right.left = new TreeNode(15);
        test1.right.right = new TreeNode(7);

        TreeNode test2 = new TreeNode(1);
        test2.right = new TreeNode(2);

        TreeNode test3 = new TreeNode(1);

        TreeNode[] testCases = {test1, test2, test3, null};
        int[] expectedResults = {3, 2, 1, 0};

        for (int i = 0; i < testCases.length; i++) {
            TreeNode root = testCases[i];
            int expected = expectedResults[i];

            int result_dfs = maxDepth_DFS(root);
            int result_bfs = maxDepth_BFS(root);
            int result_bfs_levels = maxDepth_BFS_Levels(root);
            int result_dfs_iter = maxDepth_DFS_Iterative(root);

            assert result_dfs == expected : "DFS failed";
            assert result_bfs == expected : "BFS failed";
            assert result_bfs_levels == expected : "BFS Levels failed";
            assert result_dfs_iter == expected : "DFS Iterative failed";

            System.out.println("Test case " + i + ": depth " + expected + " ✓");
        }

        System.out.println("\nAll tests passed!");
    }
}
