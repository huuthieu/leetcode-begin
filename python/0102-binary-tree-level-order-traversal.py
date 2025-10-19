"""
LeetCode 102: Binary Tree Level Order Traversal

Problem:
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level)

Example:
Input: root = [3,9,20,null,null,15,7]
       3
      / \
     9  20
       /  \
      15   7
Output: [[3], [9,20], [15,7]]

Input: root = [1]
Output: [[1]]

Time Complexity: O(n) where n is number of nodes
Space Complexity: O(w) where w is maximum width (max nodes at any level)
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach 1: BFS with Queue
def levelOrder_BFS(root):
    """
    Use BFS with a queue to traverse level by level
    Time: O(n), Space: O(w) where w = max width
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        # Process all nodes at current level
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result


# Approach 2: DFS with Level Tracking
def levelOrder_DFS(root):
    """
    Use DFS with level parameter to build result
    Time: O(n), Space: O(h) where h = height (for recursion stack)
    """
    result = []

    def dfs(node, level):
        if not node:
            return

        # Create new level if needed
        if len(result) == level:
            result.append([])

        result[level].append(node.val)

        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)
    return result


# Approach 3: DFS Recursive (Alternative)
def levelOrder_DFS_Alt(root):
    """
    Alternative DFS approach using helper function
    """
    result = []

    def dfs(node, level):
        if not node:
            return

        if level >= len(result):
            result.append([])

        result[level].append(node.val)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)
    return result


# Helper function to create tree from list
def create_tree(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


# Test Cases
def test_levelOrder():
    test_cases = [
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),
        ([], []),
        ([1, 2, 3], [[1], [2, 3]]),
        ([1, 2, 3, 4, 5], [[1], [2, 3], [4, 5]]),
    ]

    for values, expected in test_cases:
        root = create_tree(values)

        result_bfs = levelOrder_BFS(root)
        result_dfs = levelOrder_DFS(root)
        result_dfs_alt = levelOrder_DFS_Alt(root)

        assert (
            result_bfs == expected
        ), f"BFS failed: got {result_bfs}, expected {expected}"
        assert (
            result_dfs == expected
        ), f"DFS failed: got {result_dfs}, expected {expected}"
        assert (
            result_dfs_alt == expected
        ), f"DFS Alt failed: got {result_dfs_alt}, expected {expected}"

        print(f"Tree {values} => {expected} ✓")


if __name__ == "__main__":
    test_levelOrder()
    print("\nAll tests passed!")
