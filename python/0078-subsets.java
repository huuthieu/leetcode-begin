import java.util.*;

/**
 * LeetCode Problem 0078: Subsets
 *
 * Problem:
 * Given an integer array nums of unique elements, return all the possible subsets (the power set).
 *
 * The solution set must not contain duplicate subsets. You can return the solution in any order.
 *
 * Examples:
 * 1. Input: nums = [1,2,3], Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
 * 2. Input: nums = [0], Output: [[],[0]]
 */
public class Subsets {

    /**
     * Q1: Backtracking approach
     *
     * Time Complexity: O(N * 2^N)
     * Space Complexity: O(N)
     */
    public static List<List<Integer>> subsetsBacktracking(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, 0, new ArrayList<>(), result);
        return result;
    }

    private static void backtrack(int[] nums, int start, List<Integer> path,
                                  List<List<Integer>> result) {
        result.add(new ArrayList<>(path));

        for (int i = start; i < nums.length; i++) {
            path.add(nums[i]);
            backtrack(nums, i + 1, path, result);
            path.remove(path.size() - 1);
        }
    }

    /**
     * Q2: Iterative approach - build incrementally
     *
     * Time Complexity: O(N * 2^N)
     * Space Complexity: O(1) excluding output
     */
    public static List<List<Integer>> subsetsIterative(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<>());

        for (int num : nums) {
            int size = result.size();
            for (int i = 0; i < size; i++) {
                List<Integer> newSubset = new ArrayList<>(result.get(i));
                newSubset.add(num);
                result.add(newSubset);
            }
        }

        return result;
    }

    /**
     * Q3: Bit manipulation approach
     *
     * Time Complexity: O(N * 2^N)
     * Space Complexity: O(1)
     */
    public static List<List<Integer>> subsetsBitManipulation(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        int n = nums.length;
        int totalSubsets = 1 << n;  // 2^n

        for (int i = 0; i < totalSubsets; i++) {
            List<Integer> subset = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                if ((i & (1 << j)) != 0) {
                    subset.add(nums[j]);
                }
            }
            result.add(subset);
        }

        return result;
    }

    /**
     * Q4: Recursive approach with index tracking
     *
     * Time Complexity: O(N * 2^N)
     * Space Complexity: O(N)
     */
    public static List<List<Integer>> subsetsRecursive(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        helper(nums, 0, new ArrayList<>(), result);
        return result;
    }

    private static void helper(int[] nums, int index, List<Integer> path,
                               List<List<Integer>> result) {
        if (index == nums.length) {
            result.add(new ArrayList<>(path));
            return;
        }

        // Include current element
        path.add(nums[index]);
        helper(nums, index + 1, path, result);

        // Exclude current element
        path.remove(path.size() - 1);
        helper(nums, index + 1, path, result);
    }

    /**
     * Q5: DFS approach
     *
     * Time Complexity: O(N * 2^N)
     * Space Complexity: O(N)
     */
    public static List<List<Integer>> subsetsDFS(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        dfs(nums, 0, new ArrayList<>(), result);
        return result;
    }

    private static void dfs(int[] nums, int index, List<Integer> current,
                            List<List<Integer>> result) {
        result.add(new ArrayList<>(current));

        for (int i = index; i < nums.length; i++) {
            current.add(nums[i]);
            dfs(nums, i + 1, current, result);
            current.remove(current.size() - 1);
        }
    }

    /**
     * Q6: Iterative with explicit bit checking
     *
     * Time Complexity: O(N * 2^N)
     * Space Complexity: O(1)
     */
    public static List<List<Integer>> subsetsBitExplicit(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        int n = nums.length;
        int totalMasks = 1 << n;

        for (int mask = 0; mask < totalMasks; mask++) {
            List<Integer> subset = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if (((mask >> i) & 1) == 1) {
                    subset.add(nums[i]);
                }
            }
            result.add(subset);
        }

        return result;
    }

    /**
     * Q7: Nested loop approach
     *
     * Time Complexity: O(N * 2^N)
     * Space Complexity: O(1)
     */
    public static List<List<Integer>> subsetsNestedLoop(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<>());

        for (int num : nums) {
            int size = result.size();
            for (int i = 0; i < size; i++) {
                List<Integer> newSubset = new ArrayList<>(result.get(i));
                newSubset.add(num);
                result.add(newSubset);
            }
        }

        return result;
    }

    /**
     * Q8: Stream-based approach
     *
     * Time Complexity: O(N * 2^N)
     * Space Complexity: O(N)
     */
    public static List<List<Integer>> subsetsStream(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrackStream(nums, 0, new ArrayList<>(), result);
        return result;
    }

    private static void backtrackStream(int[] nums, int start, List<Integer> path,
                                        List<List<Integer>> result) {
        result.add(new ArrayList<>(path));

        for (int i = start; i < nums.length; i++) {
            path.add(nums[i]);
            backtrackStream(nums, i + 1, path, result);
            path.remove(path.size() - 1);
        }
    }

    /**
     * Q9: Include-exclude pattern
     *
     * Time Complexity: O(N * 2^N)
     * Space Complexity: O(N)
     */
    public static List<List<Integer>> subsetsIncludeExclude(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        generate(nums, 0, new ArrayList<>(), result);
        return result;
    }

    private static void generate(int[] nums, int idx, List<Integer> current,
                                 List<List<Integer>> result) {
        if (idx == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }

        // Don't include nums[idx]
        generate(nums, idx + 1, current, result);

        // Include nums[idx]
        current.add(nums[idx]);
        generate(nums, idx + 1, current, result);
        current.remove(current.size() - 1);
    }

    /**
     * Q10: Compact version
     *
     * Time Complexity: O(N * 2^N)
     * Space Complexity: O(N)
     */
    public static List<List<Integer>> subsetsCompact(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(res, new ArrayList<>(), nums, 0);
        return res;
    }

    private static void backtrack(List<List<Integer>> res, List<Integer> path,
                                  int[] nums, int start) {
        res.add(new ArrayList<>(path));
        for (int i = start; i < nums.length; i++) {
            path.add(nums[i]);
            backtrack(res, path, nums, i + 1);
            path.remove(path.size() - 1);
        }
    }

    // Test cases and main function
    public static void main(String[] args) {
        int[][] testCases = {
            {1, 2, 3},
            {0},
            {1},
            {1, 2},
            {1, 2, 3, 4}
        };

        int[] expectedCounts = {8, 2, 2, 4, 16};

        java.lang.reflect.Method[] methods = Subsets.class.getDeclaredMethods();
        List<java.lang.reflect.Method> testMethods = new ArrayList<>();

        for (java.lang.reflect.Method method : methods) {
            if (method.getName().startsWith("subsets") &&
                method.getReturnType() == List.class &&
                method.getParameterCount() == 1) {
                testMethods.add(method);
            }
        }

        Collections.sort(testMethods, Comparator.comparing(java.lang.reflect.Method::getName));

        int questionNum = 1;
        for (java.lang.reflect.Method method : testMethods) {
            System.out.println("\nQ" + questionNum + ": " + method.getName());
            System.out.println("-".repeat(70));

            boolean allPassed = true;
            for (int i = 0; i < testCases.length; i++) {
                try {
                    @SuppressWarnings("unchecked")
                    List<List<Integer>> result = (List<List<Integer>>) method.invoke(null, (Object) testCases[i]);

                    boolean passed = result.size() == expectedCounts[i];
                    allPassed = allPassed && passed;
                    String status = passed ? "✓" : "✗";

                    System.out.println("  " + status + " subsets(" + Arrays.toString(testCases[i]) + ")");
                    System.out.println("      Count: " + result.size() + " (expected: " + expectedCounts[i] + ")");

                    if (result.size() <= 8) {
                        System.out.println("      Result: " + result);
                    }

                } catch (Exception e) {
                    System.out.println("  ✗ Error: " + e.getMessage());
                    allPassed = false;
                }
            }

            if (allPassed) {
                System.out.println("  All tests passed!");
            }

            questionNum++;
        }
    }
}
