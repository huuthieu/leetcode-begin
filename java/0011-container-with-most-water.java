/**
 * LeetCode 0011: Container With Most Water
 *
 * Problem Statement:
 * You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
 * Find two lines that together with the x-axis form a container, such that the container contains the most water.
 * Return the maximum area of water that the container can store.
 * Notice that you may not slant the container.
 *
 * Example 1:
 * Input: height = [1,8,6,2,5,4,8,3,7]
 * Output: 49
 * Explanation: The vertical lines are at indices 0 and 1. Line at 0 has height 1, line at 1 has height 8.
 * The area = min(1, 8) * (1 - 0) = 1 * 1 = 1. But the maximum is at indices 1 and 8 with heights 8 and 7.
 * Area = min(8, 7) * (8 - 1) = 7 * 7 = 49.
 *
 * Example 2:
 * Input: height = [1,1]
 * Output: 1
 *
 * Constraints:
 * - n == height.length
 * - 2 <= n <= 10^5
 * - 0 <= height[i] <= 10^4
 */

import java.util.*;

public class ContainerWithMostWater {

    // Q1: What's the brute force approach?
    // A1: Check all pairs of lines. Time: O(n^2), Space: O(1)
    public int maxAreaBruteForce(int[] height) {
        int maxArea = 0;
        for (int i = 0; i < height.length; i++) {
            for (int j = i + 1; j < height.length; j++) {
                // Width is the distance between indices
                int width = j - i;
                // Height is the minimum of the two lines
                int h = Math.min(height[i], height[j]);
                // Area is width * height
                int area = width * h;
                maxArea = Math.max(maxArea, area);
            }
        }
        return maxArea;
    }

    // Q2: How can we optimize using two pointers?
    // A2: Start from both ends and move the pointer with smaller height. Time: O(n), Space: O(1)
    public int maxAreaTwoPointers(int[] height) {
        int maxArea = 0;
        int left = 0;
        int right = height.length - 1;

        while (left < right) {
            // Calculate current area
            int width = right - left;
            int h = Math.min(height[left], height[right]);
            int area = width * h;
            maxArea = Math.max(maxArea, area);

            // Move the pointer pointing to the shorter line
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea;
    }

    // Q3: Why does the two-pointer approach work?
    // A3: Because area is limited by the shorter line. Moving the longer line inward can only decrease area.
    // So we always move the shorter line hoping to find a taller line.
    /**
     * Why two pointers works:
     * - Area = min(h[i], h[j]) * (j - i)
     * - We start with maximum width
     * - If we move the taller line inward, width decreases and height can't increase (limited by shorter line)
     * - So the area can only decrease
     * - We must move the shorter line to have a chance of finding a taller line that increases area
     */

    // Q4: What if we want to track the indices of the best container?
    // A4: Modify to return both the area and the indices
    public ContainerResult maxAreaWithIndices(int[] height) {
        int maxArea = 0;
        int bestLeft = 0;
        int bestRight = height.length - 1;
        int left = 0;
        int right = height.length - 1;

        while (left < right) {
            int width = right - left;
            int h = Math.min(height[left], height[right]);
            int area = width * h;

            if (area > maxArea) {
                maxArea = area;
                bestLeft = left;
                bestRight = right;
            }

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return new ContainerResult(maxArea, bestLeft, bestRight);
    }

    // Helper class to return multiple values
    public static class ContainerResult {
        public int area;
        public int leftIndex;
        public int rightIndex;

        public ContainerResult(int area, int leftIndex, int rightIndex) {
            this.area = area;
            this.leftIndex = leftIndex;
            this.rightIndex = rightIndex;
        }
    }

    // Q5: How can we use dynamic programming approach?
    // A5: Track the maximum area seen so far, but two pointers is still optimal
    /**
     * DP approach would be:
     * dp[i][j] = maximum area from index i to j
     * But this is O(n^2) which is worse than two pointers
     * Two pointers exploits the structure that we can only move inward
     */

    // Q6: What about edge cases?
    // A6: Empty array (won't happen per constraints), single element (won't happen), equal heights
    public int maxAreaWithValidation(int[] height) {
        if (height == null || height.length < 2) {
            return 0;
        }
        return maxAreaTwoPointers(height);
    }

    // Q7: How does the algorithm decide which pointer to move?
    /**
     * A7: The algorithm moves the pointer with the smaller height because:
     * - Current area = min(h[left], h[right]) * width
     * - If we move the pointer with larger height, the minimum won't increase (limited by smaller)
     * - If we move the pointer with smaller height, we might find a taller line
     * - This greedy choice is optimal
     */

    // Q8: Can we visualize the algorithm?
    public int maxAreaWithTrace(int[] height) {
        /**
         * Example: height = [1,8,6,2,5,4,8,3,7]
         * left=0, right=8: area = min(1,7) * 8 = 8, move left
         * left=1, right=8: area = min(8,7) * 7 = 49, move right (8 > 7)
         * left=1, right=7: area = min(8,3) * 6 = 18, move right
         * ... continue until left >= right
         * Maximum area found: 49
         */
        int maxArea = 0;
        int left = 0;
        int right = height.length - 1;

        while (left < right) {
            int width = right - left;
            int h = Math.min(height[left], height[right]);
            int area = width * h;
            maxArea = Math.max(maxArea, area);

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea;
    }

    // Q9: What are variations of this problem?
    /**
     * A9:
     * - Trapping Rain Water (two pointer with different logic)
     * - Rain Water II (2D version)
     * - Largest Rectangle in Histogram
     * - Maximum Product Subarray
     */

    // Q10: Time and space complexity analysis
    /**
     * A10:
     * Brute Force:
     *   Time: O(n^2) - checking all pairs
     *   Space: O(1) - no extra space
     *
     * Two Pointers:
     *   Time: O(n) - each element visited once
     *   Space: O(1) - only using pointers
     *
     * Two pointers is optimal for this problem because of the greedy property.
     */

    public static void main(String[] args) {
        ContainerWithMostWater solution = new ContainerWithMostWater();

        // Test cases
        int[][] testHeights = {
            {1, 8, 6, 2, 5, 4, 8, 3, 7},
            {1, 1},
            {4, 3, 2, 1, 4},
            {1, 2, 1},
            {2, 3, 4, 5, 18, 17, 6}
        };

        int[] expected = {49, 1, 16, 2, 17};

        System.out.println("Testing all approaches:\n");

        for (int i = 0; i < testHeights.length; i++) {
            int[] height = testHeights[i];
            int exp = expected[i];

            int brute = solution.maxAreaBruteForce(height);
            int twoPtr = solution.maxAreaTwoPointers(height);
            ContainerResult result = solution.maxAreaWithIndices(height);

            System.out.println("height = " + Arrays.toString(height));
            System.out.println("Expected: " + exp + ", Brute Force: " + brute + ", Two Pointers: " + twoPtr);
            System.out.println("Best container: indices (" + result.leftIndex + ", " + result.rightIndex +
                             "), area = " + result.area);

            assert brute == exp : "Brute force failed for " + Arrays.toString(height);
            assert twoPtr == exp : "Two pointers failed for " + Arrays.toString(height);

            System.out.println("✓ Passed\n");
        }

        System.out.println("All tests passed!");
    }
}
