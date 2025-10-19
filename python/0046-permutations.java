import java.util.*;

/**
 * LeetCode Problem 0046: Permutations
 *
 * Problem:
 * Given an array nums of distinct integers, return all the possible permutations.
 * You can return the answer in any order.
 *
 * Examples:
 * 1. Input: nums = [1,2,3], Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 * 2. Input: nums = [0,1], Output: [[0,1],[1,0]]
 * 3. Input: nums = [1], Output: [[1]]
 */
public class Permutations {

    /**
     * Q1: Backtracking with used array
     *
     * Time Complexity: O(N * N!)
     * Space Complexity: O(N)
     */
    public static List<List<Integer>> permuteBacktrackingUsed(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        backtrack(nums, new ArrayList<>(), used, result);
        return result;
    }

    private static void backtrack(int[] nums, List<Integer> path,
                                  boolean[] used, List<List<Integer>> result) {
        if (path.size() == nums.length) {
            result.add(new ArrayList<>(path));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (!used[i]) {
                path.add(nums[i]);
                used[i] = true;

                backtrack(nums, path, used, result);

                path.remove(path.size() - 1);
                used[i] = false;
            }
        }
    }

    /**
     * Q2: Swap-based in-place permutation
     *
     * Time Complexity: O(N * N!)
     * Space Complexity: O(N)
     */
    public static List<List<Integer>> permuteSwap(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrackSwap(nums, 0, result);
        return result;
    }

    private static void backtrackSwap(int[] nums, int first, List<List<Integer>> result) {
        if (first == nums.length) {
            List<Integer> perm = new ArrayList<>();
            for (int num : nums) {
                perm.add(num);
            }
            result.add(perm);
            return;
        }

        for (int i = first; i < nums.length; i++) {
            swap(nums, first, i);
            backtrackSwap(nums, first + 1, result);
            swap(nums, first, i);
        }
    }

    private static void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    /**
     * Q3: Backtracking with remaining set
     *
     * Time Complexity: O(N * N!)
     * Space Complexity: O(N)
     */
    public static List<List<Integer>> permuteBacktrackingSet(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Set<Integer> remaining = new HashSet<>();
        for (int num : nums) {
            remaining.add(num);
        }
        backtrackSet(nums, new ArrayList<>(), remaining, result);
        return result;
    }

    private static void backtrackSet(int[] nums, List<Integer> path,
                                     Set<Integer> remaining, List<List<Integer>> result) {
        if (remaining.isEmpty()) {
            result.add(new ArrayList<>(path));
            return;
        }

        for (int num : remaining) {
            path.add(num);
            Set<Integer> newRemaining = new HashSet<>(remaining);
            newRemaining.remove(num);
            backtrackSet(nums, path, newRemaining, result);
            path.remove(path.size() - 1);
        }
    }

    /**
     * Q4: Iterative approach
     *
     * Time Complexity: O(N!)
     * Space Complexity: O(N!)
     */
    public static List<List<Integer>> permuteIterative(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<>());

        for (int num : nums) {
            List<List<Integer>> newResult = new ArrayList<>();
            for (List<Integer> perm : result) {
                for (int i = 0; i <= perm.size(); i++) {
                    List<Integer> newPerm = new ArrayList<>(perm);
                    newPerm.add(i, num);
                    newResult.add(newPerm);
                }
            }
            result = newResult;
        }

        return result;
    }

    /**
     * Q5: DFS approach
     *
     * Time Complexity: O(N * N!)
     * Space Complexity: O(N)
     */
    public static List<List<Integer>> permuteDFS(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> numList = new ArrayList<>();
        for (int num : nums) {
            numList.add(num);
        }
        dfs(new ArrayList<>(), numList, result);
        return result;
    }

    private static void dfs(List<Integer> path, List<Integer> remaining,
                            List<List<Integer>> result) {
        if (remaining.isEmpty()) {
            result.add(new ArrayList<>(path));
            return;
        }

        for (int i = 0; i < remaining.size(); i++) {
            int num = remaining.get(i);
            path.add(num);

            List<Integer> newRemaining = new ArrayList<>(remaining);
            newRemaining.remove(i);

            dfs(path, newRemaining, result);
            path.remove(path.size() - 1);
        }
    }

    /**
     * Q6: Using index swapping
     *
     * Time Complexity: O(N * N!)
     * Space Complexity: O(N)
     */
    public static List<List<Integer>> permuteIndexSwap(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        permuteHelper(nums, 0, result);
        return result;
    }

    private static void permuteHelper(int[] arr, int start, List<List<Integer>> result) {
        if (start == arr.length) {
            List<Integer> perm = new ArrayList<>();
            for (int num : arr) {
                perm.add(num);
            }
            result.add(perm);
            return;
        }

        for (int i = start; i < arr.length; i++) {
            swap(arr, start, i);
            permuteHelper(arr, start + 1, result);
            swap(arr, start, i);
        }
    }

    /**
     * Q7: With explicit list tracking
     *
     * Time Complexity: O(N * N!)
     * Space Complexity: O(N)
     */
    public static List<List<Integer>> permuteWithList(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> numList = Arrays.asList(nums[0]);
        for (int i = 1; i < nums.length; i++) {
            numList = new ArrayList<>(Arrays.asList(nums));
        }
        backtrackWithList(nums, new ArrayList<>(), new HashSet<>(), result);
        return result;
    }

    private static void backtrackWithList(int[] nums, List<Integer> path,
                                          Set<Integer> used, List<List<Integer>> result) {
        if (path.size() == nums.length) {
            result.add(new ArrayList<>(path));
            return;
        }

        for (int num : nums) {
            if (!used.contains(num)) {
                path.add(num);
                used.add(num);
                backtrackWithList(nums, path, used, result);
                path.remove(path.size() - 1);
                used.remove(num);
            }
        }
    }

    /**
     * Q8: Clean recursive approach
     *
     * Time Complexity: O(N * N!)
     * Space Complexity: O(N)
     */
    public static List<List<Integer>> permuteClean(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        solve(new ArrayList<>(), nums, new boolean[nums.length], result);
        return result;
    }

    private static void solve(List<Integer> path, int[] nums,
                              boolean[] used, List<List<Integer>> result) {
        if (path.size() == nums.length) {
            result.add(new ArrayList<>(path));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (!used[i]) {
                path.add(nums[i]);
                used[i] = true;
                solve(path, nums, used, result);
                used[i] = false;
                path.remove(path.size() - 1);
            }
        }
    }

    /**
     * Q9: Using two-pointer swap
     *
     * Time Complexity: O(N * N!)
     * Space Complexity: O(N)
     */
    public static List<List<Integer>> permuteTwoPointer(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        permuteInPlace(nums, 0, nums.length, result);
        return result;
    }

    private static void permuteInPlace(int[] nums, int low, int high,
                                       List<List<Integer>> result) {
        if (low + 1 == high) {
            List<Integer> perm = new ArrayList<>();
            for (int num : nums) {
                perm.add(num);
            }
            result.add(perm);
            return;
        }

        for (int i = low; i < high; i++) {
            swap(nums, low, i);
            permuteInPlace(nums, low + 1, high, result);
            swap(nums, low, i);
        }
    }

    /**
     * Q10: Compact version
     *
     * Time Complexity: O(N * N!)
     * Space Complexity: O(N)
     */
    public static List<List<Integer>> permuteCompact(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(res, new ArrayList<>(), nums, new boolean[nums.length]);
        return res;
    }

    private static void backtrack(List<List<Integer>> res, List<Integer> path,
                                  int[] nums, boolean[] used) {
        if (path.size() == nums.length) {
            res.add(new ArrayList<>(path));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (!used[i]) {
                used[i] = true;
                path.add(nums[i]);
                backtrack(res, path, nums, used);
                path.remove(path.size() - 1);
                used[i] = false;
            }
        }
    }

    // Test cases and main function
    public static void main(String[] args) {
        int[][] testCases = {
            {1, 2, 3},
            {0, 1},
            {1},
            {1, 2},
            {1, 2, 3, 4}
        };

        int[] expectedCounts = {6, 2, 1, 2, 24};

        java.lang.reflect.Method[] methods = Permutations.class.getDeclaredMethods();
        List<java.lang.reflect.Method> testMethods = new ArrayList<>();

        for (java.lang.reflect.Method method : methods) {
            if (method.getName().startsWith("permute") &&
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
                    int[] nums = testCases[i].clone();
                    @SuppressWarnings("unchecked")
                    List<List<Integer>> result = (List<List<Integer>>) method.invoke(null, (Object) nums);

                    boolean passed = result.size() == expectedCounts[i];
                    allPassed = allPassed && passed;
                    String status = passed ? "✓" : "✗";

                    System.out.println("  " + status + " permute(" + Arrays.toString(testCases[i]) + ")");
                    System.out.println("      Count: " + result.size() + " (expected: " + expectedCounts[i] + ")");

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
