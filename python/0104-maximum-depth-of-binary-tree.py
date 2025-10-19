"""
LeetCode 104: Maximum Depth of Binary Tree

Problem:
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Example:
Input: root = [3,9,20,null,null,15,7]
       3
      / \
     9  20
       /  \
      15   7
Output: 3

Input: root = [1,null,2]
    1
     \
      2
Output: 2

Time Complexity: O(n)
Space Complexity: O(h) where h is height
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach 1: DFS - Recursive
def maxDepth_DFS(root):
    """
    Recursively find maximum depth
    maxDepth = 1 + max(maxDepth(left), maxDepth(right))

    Time: O(n), Space: O(h) for recursion stack
    """
    if not root:
        return 0

    return 1 + max(maxDepth_DFS(root.left), maxDepth_DFS(root.right))


# Approach 2: BFS - Level Order Traversal
def maxDepth_BFS(root):
    """
    Use BFS to traverse level by level
    The number of levels is the maximum depth

    Time: O(n), Space: O(w) where w = max width
    """
    if not root:
        return 0

    from collections import deque

    queue = deque([(root, 1)])  # (node, depth)

    while queue:
        node, depth = queue.popleft()

        if not node.left and not node.right:
            return depth

        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

    return 0


# Approach 3: BFS - Counting Levels
def maxDepth_BFS_Levels(root):
    """
    BFS counting levels as we go
    """
    if not root:
        return 0

    from collections import deque

    queue = deque([root])
    depth = 0

    while queue:
        depth += 1
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth


# Approach 4: DFS - Iterative
def maxDepth_DFS_Iterative(root):
    """
    Iterative DFS using stack (post-order)
    """
    if not root:
        return 0

    stack = [(root, 1)]
    max_depth = 0

    while stack:
        node, depth = stack.pop()
        max_depth = max(max_depth, depth)

        if node.right:
            stack.append((node.right, depth + 1))
        if node.left:
            stack.append((node.left, depth + 1))

    return max_depth


# Helper function to create tree
def create_tree(values):
    if not values or values[0] is None:
        return None

    from collections import deque

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
def test_maxDepth():
    test_cases = [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
        ([1], 1),
        ([], 0),
        ([1, 2], 2),
        ([1, None, 2, None, 3], 3),
    ]

    for values, expected in test_cases:
        root = create_tree(values)

        result_dfs = maxDepth_DFS(root)
        result_bfs = maxDepth_BFS(root)
        result_bfs_levels = maxDepth_BFS_Levels(root)
        result_dfs_iter = maxDepth_DFS_Iterative(root)

        assert (
            result_dfs == expected
        ), f"DFS failed: got {result_dfs}, expected {expected}"
        assert (
            result_bfs == expected
        ), f"BFS failed: got {result_bfs}, expected {expected}"
        assert (
            result_bfs_levels == expected
        ), f"BFS Levels failed: got {result_bfs_levels}, expected {expected}"
        assert (
            result_dfs_iter == expected
        ), f"DFS Iterative failed: got {result_dfs_iter}, expected {expected}"

        print(f"Tree {values} => depth {expected} ✓")


if __name__ == "__main__":
    test_maxDepth()
    print("\nAll tests passed!")
