/**
 * LeetCode 207: Course Schedule
 *
 * Problem:
 * There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
 * You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must
 * take course bi first if you want to take course ai.
 *
 * Return true if you can finish all courses. Otherwise, return false.
 * This is a cycle detection problem in a directed graph.
 *
 * Example:
 * numCourses = 2, prerequisites = [[1,0]] => true
 * numCourses = 2, prerequisites = [[1,0],[0,1]] => false (cycle)
 */

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class CourseSchedule {

    // Approach 1: DFS (Depth-First Search) - Cycle Detection
    public static boolean canFinish_DFS(int numCourses, int[][] prerequisites) {
        /**
         * Use DFS to detect cycles in the graph
         * States: 0 = unvisited, 1 = visiting, 2 = visited
         * Time: O(V + E), Space: O(V + E)
         */
        // Build adjacency list
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] prereq : prerequisites) {
            graph.get(prereq[0]).add(prereq[1]);
        }

        int[] state = new int[numCourses]; // 0 = unvisited, 1 = visiting, 2 = visited

        for (int i = 0; i < numCourses; i++) {
            if (state[i] == 0) {
                if (hasCycle(i, state, graph)) {
                    return false;
                }
            }
        }

        return true;
    }

    private static boolean hasCycle(int course, int[] state, List<List<Integer>> graph) {
        if (state[course] == 1) {
            return true; // Found a cycle
        }
        if (state[course] == 2) {
            return false; // Already visited, no cycle from here
        }

        state[course] = 1; // Mark as visiting

        for (int prereq : graph.get(course)) {
            if (hasCycle(prereq, state, graph)) {
                return true;
            }
        }

        state[course] = 2; // Mark as visited
        return false;
    }

    // Approach 2: BFS (Topological Sort with Kahn's Algorithm)
    public static boolean canFinish_BFS(int numCourses, int[][] prerequisites) {
        /**
         * Use BFS with in-degree calculation
         * If all courses can be processed, no cycle exists
         * Time: O(V + E), Space: O(V + E)
         */
        // Build graph and calculate in-degrees
        List<List<Integer>> graph = new ArrayList<>();
        int[] inDegree = new int[numCourses];

        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] prereq : prerequisites) {
            graph.get(prereq[1]).add(prereq[0]);
            inDegree[prereq[0]]++;
        }

        // Start with courses that have no prerequisites
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                queue.offer(i);
            }
        }

        int coursesTaken = 0;
        while (!queue.isEmpty()) {
            int course = queue.poll();
            coursesTaken++;

            for (int nextCourse : graph.get(course)) {
                inDegree[nextCourse]--;
                if (inDegree[nextCourse] == 0) {
                    queue.offer(nextCourse);
                }
            }
        }

        return coursesTaken == numCourses;
    }

    // Test Cases
    public static void main(String[] args) {
        int[][][] testCases = {
            {new int[]{1, 0}},
            {new int[]{1, 0}, new int[]{0, 1}},
            {new int[]{0, 1}, new int[]{0, 2}, new int[]{1, 2}},
            {},
            {new int[]{1, 0}, new int[]{2, 0}, new int[]{3, 1}, new int[]{3, 2}},
            {new int[]{0, 1}, new int[]{1, 2}, new int[]{2, 0}}
        };

        int[] numCourses = {2, 2, 3, 1, 4, 3};
        boolean[] expectedResults = {true, false, true, true, true, false};

        for (int i = 0; i < testCases.length; i++) {
            int numC = numCourses[i];
            int[][] prereqs = testCases[i];
            boolean expected = expectedResults[i];

            boolean result_dfs = canFinish_DFS(numC, prereqs);
            boolean result_bfs = canFinish_BFS(numC, prereqs);

            assert result_dfs == expected : "DFS failed";
            assert result_bfs == expected : "BFS failed";

            System.out.println("Test case " + i + ": " + expected + " ✓");
        }

        System.out.println("\nAll tests passed!");
    }
}
