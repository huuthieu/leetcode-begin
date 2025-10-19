/**
 * LeetCode 42: Trapping Rain Water
 *
 * Problem:
 * Given n non-negative integers representing an elevation map where the width of each bar is 1,
 * compute how much water it can trap after raining.
 *
 * Example:
 * Input: height = [0,1,0,2,1,0,1,3,2,1,2,1] => Output: 6
 * Input: height = [4,2,0,3,2,5] => Output: 9
 */

import java.util.Stack;

public class TrappingRainWater {

    // Approach 1: Two Pointer - Most Optimal
    public static int trap_TwoPointer(int[] height) {
        /**
         * Use two pointers from both ends
         * Water trapped = min(max_left, max_right) - height[i]
         * Time: O(n), Space: O(1)
         */
        if (height == null || height.length == 0) return 0;

        int left = 0, right = height.length - 1;
        int leftMax = 0, rightMax = 0;
        int waterTrapped = 0;

        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] >= leftMax) {
                    leftMax = height[left];
                } else {
                    waterTrapped += leftMax - height[left];
                }
                left++;
            } else {
                if (height[right] >= rightMax) {
                    rightMax = height[right];
                } else {
                    waterTrapped += rightMax - height[right];
                }
                right--;
            }
        }

        return waterTrapped;
    }

    // Approach 2: DP with Pre-computed Max Heights
    public static int trap_DP(int[] height) {
        /**
         * Pre-compute max heights to left and right
         * Time: O(n), Space: O(n)
         */
        if (height == null || height.length == 0) return 0;

        int n = height.length;
        int[] leftMax = new int[n];
        int[] rightMax = new int[n];

        leftMax[0] = height[0];
        for (int i = 1; i < n; i++) {
            leftMax[i] = Math.max(leftMax[i - 1], height[i]);
        }

        rightMax[n - 1] = height[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            rightMax[i] = Math.max(rightMax[i + 1], height[i]);
        }

        int waterTrapped = 0;
        for (int i = 0; i < n; i++) {
            int minHeight = Math.min(leftMax[i], rightMax[i]);
            waterTrapped += minHeight - height[i];
        }

        return waterTrapped;
    }

    // Approach 3: Stack-based
    public static int trap_Stack(int[] height) {
        /**
         * Use a stack to track indices
         * Time: O(n), Space: O(n)
         */
        if (height == null || height.length == 0) return 0;

        Stack<Integer> stack = new Stack<>();
        int waterTrapped = 0;

        for (int i = 0; i < height.length; i++) {
            while (!stack.isEmpty() && height[i] > height[stack.peek()]) {
                int top = stack.pop();

                if (stack.isEmpty()) break;

                int width = i - stack.peek() - 1;
                int waterLevel = Math.min(height[i], height[stack.peek()]) - height[top];
                waterTrapped += width * waterLevel;
            }

            stack.push(i);
        }

        return waterTrapped;
    }

    // Test Cases
    public static void main(String[] args) {
        int[][] testCases = {
            {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1},
            {4, 2, 0, 3, 2, 5},
            {3, 0, 2, 0, 4},
            {2, 0, 2},
            {0, 1, 2, 3},
            {3, 2, 1, 0},
            {5},
            {5, 5, 5}
        };

        int[] expectedResults = {6, 9, 7, 2, 0, 0, 0, 0};

        for (int i = 0; i < testCases.length; i++) {
            int[] height = testCases[i];
            int expected = expectedResults[i];

            int result_twoPtr = trap_TwoPointer(height);
            int result_dp = trap_DP(height);
            int result_stack = trap_Stack(height);

            assert result_twoPtr == expected : "TwoPointer failed";
            assert result_dp == expected : "DP failed";
            assert result_stack == expected : "Stack failed";

            System.out.println("Test case " + i + ": " + expected + " units ✓");
        }

        System.out.println("\nAll tests passed!");
    }
}
