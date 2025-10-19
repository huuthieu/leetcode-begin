import java.util.*;

/**
 * LeetCode Problem 0039: Combination Sum
 *
 * Problem:
 * Given an array of distinct integers candidates and a target integer target,
 * return a list of all unique combinations of candidates where the chosen numbers
 * sum to target. You may return the combinations in any order.
 *
 * The same number in candidates may be chosen an unlimited number of times.
 *
 * Examples:
 * 1. Input: candidates = [2,3,6,7], target = 7, Output: [[2,2,3],[7]]
 * 2. Input: candidates = [2,3,5], target = 8, Output: [[2,2,2,2],[2,3,3],[3,5]]
 * 3. Input: candidates = [2], target = 1, Output: []
 */
public class CombinationSum {

    /**
     * Q1: Backtracking with recursive approach
     *
     * Time Complexity: O(N^(T/M))
     * Space Complexity: O(T/M) for recursion depth
     */
    public static List<List<Integer>> combinationSumBacktracking(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(candidates, target, 0, new ArrayList<>(), result);
        return result;
    }

    private static void backtrack(int[] candidates, int remaining, int start,
                                   List<Integer> combination, List<List<Integer>> result) {
        if (remaining == 0) {
            result.add(new ArrayList<>(combination));
            return;
        }

        if (remaining < 0) {
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            combination.add(candidates[i]);
            backtrack(candidates, remaining - candidates[i], i, combination, result);
            combination.remove(combination.size() - 1);
        }
    }

    /**
     * Q2: Backtracking with immediate pruning
     *
     * Time Complexity: O(N^(T/M))
     * Space Complexity: O(T/M)
     */
    public static List<List<Integer>> combinationSumPruning(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        backtrackPruning(candidates, target, 0, new ArrayList<>(), result);
        return result;
    }

    private static void backtrackPruning(int[] candidates, int remaining, int start,
                                          List<Integer> combination, List<List<Integer>> result) {
        if (remaining == 0) {
            result.add(new ArrayList<>(combination));
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            if (candidates[i] <= remaining) {
                combination.add(candidates[i]);
                backtrackPruning(candidates, remaining - candidates[i], i, combination, result);
                combination.remove(combination.size() - 1);
            }
        }
    }

    /**
     * Q3: Sorted candidates with early termination
     *
     * Time Complexity: O(N^(T/M))
     * Space Complexity: O(T/M)
     */
    public static List<List<Integer>> combinationSumSorted(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(candidates);
        backtrackSorted(candidates, target, 0, new ArrayList<>(), result);
        return result;
    }

    private static void backtrackSorted(int[] candidates, int remaining, int start,
                                         List<Integer> combination, List<List<Integer>> result) {
        if (remaining == 0) {
            result.add(new ArrayList<>(combination));
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            if (candidates[i] > remaining) {
                break;
            }
            combination.add(candidates[i]);
            backtrackSorted(candidates, remaining - candidates[i], i, combination, result);
            combination.remove(combination.size() - 1);
        }
    }

    /**
     * Q4: Iterative approach with queue
     *
     * Time Complexity: O(N^(T/M))
     * Space Complexity: O(N^(T/M))
     */
    public static List<List<Integer>> combinationSumIterative(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Queue<State> queue = new LinkedList<>();
        queue.offer(new State(target, new ArrayList<>(), 0));

        while (!queue.isEmpty()) {
            State current = queue.poll();

            if (current.remaining == 0) {
                result.add(current.combination);
                continue;
            }

            for (int i = current.start; i < candidates.length; i++) {
                if (candidates[i] <= current.remaining) {
                    List<Integer> newCombination = new ArrayList<>(current.combination);
                    newCombination.add(candidates[i]);
                    queue.offer(new State(current.remaining - candidates[i], newCombination, i));
                }
            }
        }

        return result;
    }

    static class State {
        int remaining;
        List<Integer> combination;
        int start;

        State(int remaining, List<Integer> combination, int start) {
            this.remaining = remaining;
            this.combination = combination;
            this.start = start;
        }
    }

    /**
     * Q5: DP with memoization
     *
     * Time Complexity: O(N^(T/M))
     * Space Complexity: O(T)
     */
    public static List<List<Integer>> combinationSumDP(int[] candidates, int target) {
        Map<Integer, List<List<Integer>>> memo = new HashMap<>();
        return dpHelper(candidates, target, 0, memo);
    }

    private static List<List<Integer>> dpHelper(int[] candidates, int remaining, int start,
                                                 Map<Integer, List<List<Integer>>> memo) {
        if (remaining == 0) {
            return new ArrayList<>(Arrays.asList(new ArrayList<>()));
        }

        if (remaining < 0) {
            return new ArrayList<>();
        }

        if (memo.containsKey(remaining)) {
            return memo.get(remaining);
        }

        List<List<Integer>> result = new ArrayList<>();

        for (int i = start; i < candidates.length; i++) {
            if (candidates[i] <= remaining) {
                for (List<Integer> subCombination : dpHelper(candidates, remaining - candidates[i], i, memo)) {
                    List<Integer> newCombination = new ArrayList<>();
                    newCombination.add(candidates[i]);
                    newCombination.addAll(subCombination);
                    result.add(newCombination);
                }
            }
        }

        memo.put(remaining, result);
        return result;
    }

    /**
     * Q6: Bottom-up DP
     *
     * Time Complexity: O(target * N)
     * Space Complexity: O(target)
     */
    public static List<List<Integer>> combinationSumBottomUp(int[] candidates, int target) {
        @SuppressWarnings("unchecked")
        List<List<Integer>>[] dp = new ArrayList[target + 1];

        for (int i = 0; i <= target; i++) {
            dp[i] = new ArrayList<>();
        }

        dp[0].add(new ArrayList<>());

        for (int amount = 1; amount <= target; amount++) {
            for (int candidate : candidates) {
                if (candidate <= amount) {
                    for (List<Integer> combination : dp[amount - candidate]) {
                        List<Integer> newCombination = new ArrayList<>(combination);
                        newCombination.add(candidate);
                        dp[amount].add(newCombination);
                    }
                }
            }
        }

        return dp[target];
    }

    /**
     * Q7: With helper function
     *
     * Time Complexity: O(N^(T/M))
     * Space Complexity: O(T/M)
     */
    public static List<List<Integer>> combinationSumHelper(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        helper(candidates, target, 0, new ArrayList<>(), result);
        return result;
    }

    private static void helper(int[] candidates, int target, int start,
                               List<Integer> current, List<List<Integer>> result) {
        if (target < 0) return;
        if (target == 0) {
            result.add(new ArrayList<>(current));
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            current.add(candidates[i]);
            helper(candidates, target - candidates[i], i, current, result);
            current.remove(current.size() - 1);
        }
    }

    /**
     * Q8: Clean and simple
     *
     * Time Complexity: O(N^(T/M))
     * Space Complexity: O(T/M)
     */
    public static List<List<Integer>> combinationSumClean(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        findCombinations(candidates, target, 0, new ArrayList<>(), result);
        return result;
    }

    private static void findCombinations(int[] candidates, int remaining, int start,
                                         List<Integer> path, List<List<Integer>> result) {
        if (remaining == 0) {
            result.add(new ArrayList<>(path));
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            if (candidates[i] <= remaining) {
                path.add(candidates[i]);
                findCombinations(candidates, remaining - candidates[i], i, path, result);
                path.remove(path.size() - 1);
            }
        }
    }

    /**
     * Q9: With explicit index tracking
     *
     * Time Complexity: O(N^(T/M))
     * Space Complexity: O(T/M)
     */
    public static List<List<Integer>> combinationSumIndexed(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        solve(candidates, 0, target, new ArrayList<>(), result);
        return result;
    }

    private static void solve(int[] candidates, int idx, int remaining,
                              List<Integer> current, List<List<Integer>> result) {
        if (remaining == 0) {
            result.add(new ArrayList<>(current));
            return;
        }

        if (idx == candidates.length || remaining < 0) {
            return;
        }

        // Include current element (can reuse)
        current.add(candidates[idx]);
        solve(candidates, idx, remaining - candidates[idx], current, result);
        current.remove(current.size() - 1);

        // Exclude current element
        solve(candidates, idx + 1, remaining, current, result);
    }

    /**
     * Q10: Compact version
     *
     * Time Complexity: O(N^(T/M))
     * Space Complexity: O(T/M)
     */
    public static List<List<Integer>> combinationSumCompact(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        backtrackCompact(candidates, target, 0, new ArrayList<>(), result);
        return result;
    }

    private static void backtrackCompact(int[] c, int t, int s,
                                         List<Integer> path, List<List<Integer>> res) {
        if (t == 0) {
            res.add(new ArrayList<>(path));
        } else {
            for (int i = s; i < c.length && c[i] <= t; i++) {
                path.add(c[i]);
                backtrackCompact(c, t - c[i], i, path, res);
                path.remove(path.size() - 1);
            }
        }
    }

    // Test cases and main function
    public static void main(String[] args) {
        int[][] testCandidates = {
            {2, 3, 6, 7},
            {2, 3, 5},
            {2},
            {2, 3, 6, 7},
            {2, 3, 6, 7},
            {2, 3, 6, 7}
        };

        int[] testTargets = {7, 8, 1, 2, 3, 6};

        java.lang.reflect.Method[] methods = CombinationSum.class.getDeclaredMethods();
        List<java.lang.reflect.Method> testMethods = new ArrayList<>();

        for (java.lang.reflect.Method method : methods) {
            if (method.getName().startsWith("combinationSum") &&
                method.getReturnType() == List.class &&
                method.getParameterCount() == 2) {
                testMethods.add(method);
            }
        }

        Collections.sort(testMethods, Comparator.comparing(java.lang.reflect.Method::getName));

        int questionNum = 1;
        for (java.lang.reflect.Method method : testMethods) {
            System.out.println("\nQ" + questionNum + ": " + method.getName());
            System.out.println("-".repeat(70));

            boolean allPassed = true;
            for (int i = 0; i < testCandidates.length; i++) {
                try {
                    @SuppressWarnings("unchecked")
                    List<List<Integer>> result = (List<List<Integer>>) method.invoke(null,
                        testCandidates[i], testTargets[i]);

                    String status = "✓";
                    System.out.println("  " + status + " combinationSum(" +
                        Arrays.toString(testCandidates[i]) + ", " + testTargets[i] + ")");
                    System.out.println("      Result: " + result);

                } catch (Exception e) {
                    System.out.println("  ✗ Error: " + e.getMessage());
                    allPassed = false;
                }
            }

            questionNum++;
        }
    }
}
