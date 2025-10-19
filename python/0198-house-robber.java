/**
 * LeetCode 198: House Robber
 *
 * Problem:
 * You are a professional robber planning to rob houses along a street.
 * Each house has a certain amount of money stashed, represented by a non-negative integer.
 * You cannot rob two adjacent houses (security system).
 * Return the maximum amount of money you can rob.
 *
 * Example:
 * nums = [1,2,3,1] => 4 (rob house 1 and 3)
 * nums = [2,7,9,3] => 9 (rob house 2 and 3)
 */

public class HouseRobber {

    // Approach 1: Dynamic Programming - Tabulation
    public static int rob_DP(int[] nums) {
        /**
         * dp[i] = max money robbed up to house i
         * dp[i] = max(dp[i-1], dp[i-2] + nums[i])
         * Time: O(n), Space: O(n)
         */
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];

        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);

        for (int i = 2; i < nums.length; i++) {
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
        }

        return dp[nums.length - 1];
    }

    // Approach 2: Space-Optimized DP
    public static int rob_Optimized(int[] nums) {
        /**
         * We only need the last two values
         * Time: O(n), Space: O(1)
         */
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];

        int prev2 = nums[0];
        int prev1 = Math.max(nums[0], nums[1]);

        for (int i = 2; i < nums.length; i++) {
            int current = Math.max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }

    // Approach 3: Memoization (Top-Down DP)
    public static int rob_Memo(int[] nums) {
        int[] memo = new int[nums.length];
        for (int i = 0; i < memo.length; i++) {
            memo[i] = -1;
        }
        return dp(nums, nums.length - 1, memo);
    }

    private static int dp(int[] nums, int index, int[] memo) {
        if (index < 0) return 0;
        if (index == 0) return nums[0];
        if (memo[index] != -1) return memo[index];

        memo[index] = Math.max(dp(nums, index - 1, memo), dp(nums, index - 2, memo) + nums[index]);
        return memo[index];
    }

    // Test Cases
    public static void main(String[] args) {
        int[][] testCases = {
            {1, 2, 3, 1},
            {2, 7, 9, 3},
            {5, 3, 4, 11, 2},
            {1},
            {5},
            {2, 1},
            {1, 3, 1, 3, 100}
        };

        int[] expectedResults = {4, 9, 16, 1, 5, 2, 103};

        for (int i = 0; i < testCases.length; i++) {
            int[] nums = testCases[i];
            int expected = expectedResults[i];

            int result_dp = rob_DP(nums);
            int result_opt = rob_Optimized(nums);
            int result_memo = rob_Memo(nums);

            assert result_dp == expected : "DP failed";
            assert result_opt == expected : "Optimized failed";
            assert result_memo == expected : "Memo failed";

            System.out.println("Test case " + i + ": " + expected + " ✓");
        }

        System.out.println("\nAll tests passed!");

        // Example usage
        int[] example = {2, 7, 9, 3};
        System.out.println("\nHouse Robber Example: " + rob_Optimized(example));
    }
}
