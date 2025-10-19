/**
 * LeetCode 70: Climbing Stairs
 *
 * Problem:
 * You are climbing a staircase. It takes n steps to reach the top.
 * Each time you can climb 1 or 2 steps. In how many distinct ways can you climb to the top?
 *
 * Example:
 * n = 2 => 2 ways (1+1, 2)
 * n = 3 => 3 ways (1+1+1, 1+2, 2+1)
 * n = 4 => 5 ways (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2)
 */

public class ClimbingStairs {

    // Approach 1: Dynamic Programming - Tabulation
    public static int climbStairs_DP(int n) {
        /**
         * dp[i] = dp[i-1] + dp[i-2]
         * Why? To reach step i, you can come from step i-1 (1 step) or step i-2 (2 steps)
         * Time: O(n), Space: O(n)
         */
        if (n <= 2) return n;

        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;

        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[n];
    }

    // Approach 2: Space-Optimized DP
    public static int climbStairs_Optimized(int n) {
        /**
         * We only need the last two values
         * Time: O(n), Space: O(1)
         */
        if (n <= 2) return n;

        int prev2 = 1, prev1 = 2;

        for (int i = 3; i <= n; i++) {
            int current = prev1 + prev2;
            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }

    // Approach 3: Memoization (Top-Down DP)
    public static int climbStairs_Memo(int n) {
        int[] memo = new int[n + 1];
        return dp(n, memo);
    }

    private static int dp(int n, int[] memo) {
        if (n <= 2) return n;
        if (memo[n] != 0) return memo[n];

        memo[n] = dp(n - 1, memo) + dp(n - 2, memo);
        return memo[n];
    }

    // Test Cases
    public static void main(String[] args) {
        int[][] testCases = {
            {1, 1},
            {2, 2},
            {3, 3},
            {4, 5},
            {5, 8},
            {6, 13},
            {10, 89}
        };

        for (int[] testCase : testCases) {
            int n = testCase[0];
            int expected = testCase[1];

            assert climbStairs_DP(n) == expected : "DP failed for n=" + n;
            assert climbStairs_Optimized(n) == expected : "Optimized failed for n=" + n;
            assert climbStairs_Memo(n) == expected : "Memo failed for n=" + n;

            System.out.println("n=" + n + ": " + expected + " ways ✓");
        }

        System.out.println("\nAll tests passed!");

        // Example usage
        System.out.println("\nFor n=45: " + climbStairs_Optimized(45) + " ways");
    }
}
