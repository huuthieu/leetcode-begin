/**
 * LeetCode 53: Maximum Subarray (Kadane's Algorithm)
 *
 * Problem:
 * Given an integer array nums, find the contiguous subarray which has the largest sum
 * and return its sum.
 *
 * Example:
 * nums = [-2,1,-3,4,-1,2,1,-5,4] => 6
 * nums = [5,4,-1,7,8] => 23
 */

public class MaximumSubarray {

    // Approach 1: Kadane's Algorithm - Optimal
    public static int maxSubArray_Kadane(int[] nums) {
        /**
         * Track max_current (max sum ending here) and max_global (overall max)
         * Time: O(n), Space: O(1)
         */
        int maxCurrent = nums[0];
        int maxGlobal = nums[0];

        for (int i = 1; i < nums.length; i++) {
            maxCurrent = Math.max(nums[i], maxCurrent + nums[i]);
            maxGlobal = Math.max(maxGlobal, maxCurrent);
        }

        return maxGlobal;
    }

    // Approach 2: Dynamic Programming
    public static int maxSubArray_DP(int[] nums) {
        /**
         * dp[i] = maximum sum ending at index i
         * Time: O(n), Space: O(n)
         */
        int[] dp = new int[nums.length];
        dp[0] = nums[0];

        int max = dp[0];
        for (int i = 1; i < nums.length; i++) {
            dp[i] = Math.max(nums[i], dp[i - 1] + nums[i]);
            max = Math.max(max, dp[i]);
        }

        return max;
    }

    // Approach 3: Kadane with Space Optimization
    public static int maxSubArray_Optimized(int[] nums) {
        /**
         * Same as Kadane but with cleaner variable names
         */
        int maxEndingHere = nums[0];
        int maxSoFar = nums[0];

        for (int i = 1; i < nums.length; i++) {
            maxEndingHere = Math.max(nums[i], maxEndingHere + nums[i]);
            maxSoFar = Math.max(maxSoFar, maxEndingHere);
        }

        return maxSoFar;
    }

    // Test Cases
    public static void main(String[] args) {
        int[][] testCases = {
            {-2, 1, -3, 4, -1, 2, 1, -5, 4},
            {5, 4, -1, 7, 8},
            {-1},
            {-100000},
            {1},
            {-2, -3, -1},
            {1, 2, 3, 4, 5},
            {-5, -2, 5, -3, 5}
        };

        int[] expectedResults = {6, 23, -1, -100000, 1, -1, 15, 10};

        for (int i = 0; i < testCases.length; i++) {
            int[] nums = testCases[i];
            int expected = expectedResults[i];

            int result_kadane = maxSubArray_Kadane(nums);
            int result_dp = maxSubArray_DP(nums);
            int result_opt = maxSubArray_Optimized(nums);

            assert result_kadane == expected : "Kadane failed";
            assert result_dp == expected : "DP failed";
            assert result_opt == expected : "Optimized failed";

            System.out.println("Test case " + i + ": " + expected + " ✓");
        }

        System.out.println("\nAll tests passed!");
    }
}
