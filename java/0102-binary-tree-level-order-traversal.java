/**
 * LeetCode 102: Binary Tree Level Order Traversal
 *
 * Problem:
 * Given the root of a binary tree, return the level order traversal of its nodes' values.
 *
 * Example:
 * Input: root = [3,9,20,null,null,15,7]
 * Output: [[3], [9,20], [15,7]]
 */

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class BinaryTreeLevelOrderTraversal {

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

    // Approach 1: BFS with Queue
    public static List<List<Integer>> levelOrder_BFS(TreeNode root) {
        /**
         * Use BFS with a queue to traverse level by level
         * Time: O(n), Space: O(w) where w = max width
         */
        List<List<Integer>> result = new ArrayList<>();

        if (root == null) {
            return result;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            List<Integer> currentLevel = new ArrayList<>();

            // Process all nodes at current level
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                currentLevel.add(node.val);

                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }

            result.add(currentLevel);
        }

        return result;
    }

    // Approach 2: DFS with Level Tracking
    public static List<List<Integer>> levelOrder_DFS(TreeNode root) {
        /**
         * Use DFS with level parameter
         * Time: O(n), Space: O(h) where h = height
         */
        List<List<Integer>> result = new ArrayList<>();
        dfs(root, 0, result);
        return result;
    }

    private static void dfs(TreeNode node, int level, List<List<Integer>> result) {
        if (node == null) {
            return;
        }

        if (level >= result.size()) {
            result.add(new ArrayList<>());
        }

        result.get(level).add(node.val);

        dfs(node.left, level + 1, result);
        dfs(node.right, level + 1, result);
    }

    // Helper: Create tree from array (level-order)
    public static TreeNode createTree(Integer[] values) {
        if (values == null || values.length == 0 || values[0] == null) {
            return null;
        }

        TreeNode root = new TreeNode(values[0]);
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int i = 1;

        while (!queue.isEmpty() && i < values.length) {
            TreeNode node = queue.poll();

            if (i < values.length && values[i] != null) {
                node.left = new TreeNode(values[i]);
                queue.offer(node.left);
            }
            i++;

            if (i < values.length && values[i] != null) {
                node.right = new TreeNode(values[i]);
                queue.offer(node.right);
            }
            i++;
        }

        return root;
    }

    // Test Cases
    public static void main(String[] args) {
        Integer[][] testCases = {
            {3, 9, 20, null, null, 15, 7},
            {1},
            {},
            {1, 2, 3},
            {1, 2, 3, 4, 5}
        };

        List<List<Integer>>[] expectedResults = new List[5];
        expectedResults[0] = new ArrayList<>();
        expectedResults[0].add(new ArrayList<>(java.util.Arrays.asList(3)));
        expectedResults[0].add(new ArrayList<>(java.util.Arrays.asList(9, 20)));
        expectedResults[0].add(new ArrayList<>(java.util.Arrays.asList(15, 7)));

        expectedResults[1] = new ArrayList<>();
        expectedResults[1].add(new ArrayList<>(java.util.Arrays.asList(1)));

        expectedResults[2] = new ArrayList<>();

        expectedResults[3] = new ArrayList<>();
        expectedResults[3].add(new ArrayList<>(java.util.Arrays.asList(1)));
        expectedResults[3].add(new ArrayList<>(java.util.Arrays.asList(2, 3)));

        expectedResults[4] = new ArrayList<>();
        expectedResults[4].add(new ArrayList<>(java.util.Arrays.asList(1)));
        expectedResults[4].add(new ArrayList<>(java.util.Arrays.asList(2, 3)));
        expectedResults[4].add(new ArrayList<>(java.util.Arrays.asList(4, 5)));

        for (int i = 0; i < testCases.length; i++) {
            TreeNode root = createTree(testCases[i]);

            List<List<Integer>> result_bfs = levelOrder_BFS(root);
            List<List<Integer>> result_dfs = levelOrder_DFS(root);

            assert result_bfs.equals(expectedResults[i]) : "BFS failed";
            assert result_dfs.equals(expectedResults[i]) : "DFS failed";

            System.out.println("Test case " + i + ": ✓");
        }

        System.out.println("\nAll tests passed!");
    }
}
