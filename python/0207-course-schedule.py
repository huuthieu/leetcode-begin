"""
LeetCode 207: Course Schedule

Problem:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must
take course bi first if you want to take course ai.

For example, the pair [0, 1] indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

This is a cycle detection problem in a directed graph (topological sort).

Example:
numCourses = 2, prerequisites = [[1,0]]
Output: true (You can finish course 1 first, then course 0)

numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false (There's a cycle: 0 -> 1 -> 0)

Time Complexity: O(V + E) where V = numCourses, E = len(prerequisites)
Space Complexity: O(V + E) for graph
"""

from collections import defaultdict, deque


# Approach 1: DFS (Depth-First Search) - Cycle Detection
def canFinish_DFS(numCourses, prerequisites):
    """
    Build adjacency list and use DFS to detect cycles.
    Use three states:
    - 0: Not visited
    - 1: Currently visiting (in current DFS path)
    - 2: Visited (all descendants processed)

    If we encounter a node with state 1, there's a cycle.
    """
    if not prerequisites:
        return True

    # Build adjacency list
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    # States: 0 = unvisited, 1 = visiting, 2 = visited
    state = [0] * numCourses

    def has_cycle(course):
        if state[course] == 1:
            # Currently visiting - found a cycle
            return True
        if state[course] == 2:
            # Already visited - no cycle from here
            return False

        state[course] = 1  # Mark as visiting

        # Check all prerequisites
        for prereq in graph[course]:
            if has_cycle(prereq):
                return True

        state[course] = 2  # Mark as visited
        return False

    # Check each course
    for course in range(numCourses):
        if state[course] == 0:
            if has_cycle(course):
                return False

    return True


# Approach 2: BFS (Topological Sort with Kahn's Algorithm)
def canFinish_BFS(numCourses, prerequisites):
    """
    Use BFS with in-degree calculation.
    If all courses can be processed (in-degree becomes 0), no cycle exists.
    """
    if not prerequisites:
        return True

    # Build graph and calculate in-degrees
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Start with courses that have no prerequisites
    queue = deque([course for course in range(numCourses) if in_degree[course] == 0])
    courses_taken = 0

    while queue:
        course = queue.popleft()
        courses_taken += 1

        # For each course that depends on current course
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)

    # If all courses can be taken, no cycle
    return courses_taken == numCourses


# Approach 3: DFS with Stack
def canFinish_DFS_Stack(numCourses, prerequisites):
    """
    Similar to Approach 1 but using explicit stack (iterative DFS)
    """
    if not prerequisites:
        return True

    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    state = [0] * numCourses

    def has_cycle(start_course):
        stack = [start_course]

        while stack:
            course = stack[-1]

            if state[course] == 1:
                # We've processed all children, mark as visited
                state[course] = 2
                stack.pop()
            elif state[course] == 0:
                # Start visiting this course
                state[course] = 1
                for prereq in graph[course]:
                    if state[prereq] == 1:
                        # Found a cycle
                        return True
                    elif state[prereq] == 0:
                        stack.append(prereq)
            else:
                # Already visited
                stack.pop()

        return False

    for course in range(numCourses):
        if state[course] == 0:
            if has_cycle(course):
                return False

    return True


# Test Cases
def test_canFinish():
    test_cases = [
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
        (3, [[0, 1], [0, 2], [1, 2]], True),
        (1, [], True),
        (2, [], True),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], True),
        (3, [[0, 1], [1, 2], [2, 0]], False),
    ]

    for numCourses, prerequisites, expected in test_cases:
        result_dfs = canFinish_DFS(numCourses, prerequisites)
        result_bfs = canFinish_BFS(numCourses, prerequisites)
        result_dfs_stack = canFinish_DFS_Stack(numCourses, prerequisites)

        assert (
            result_dfs == expected
        ), f"DFS failed: got {result_dfs}, expected {expected}"
        assert (
            result_bfs == expected
        ), f"BFS failed: got {result_bfs}, expected {expected}"
        assert (
            result_dfs_stack == expected
        ), f"DFS Stack failed: got {result_dfs_stack}, expected {expected}"

        print(f"numCourses={numCourses}, prerequisites={prerequisites} => {expected} ✓")


if __name__ == "__main__":
    test_canFinish()
    print("\nAll tests passed!")
