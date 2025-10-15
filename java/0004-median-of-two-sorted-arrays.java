/**
 * LeetCode 0004: Median of Two Sorted Arrays
 *
 * Problem Statement:
 * Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
 * The overall run time complexity should be O(log (m+n)).
 *
 * Example 1:
 * Input: nums1 = [1,3], nums2 = [2]
 * Output: 2.00000
 * Explanation: merged array = [1,2,3] and median is 2.
 *
 * Example 2:
 * Input: nums1 = [1,2], nums2 = [3,4]
 * Output: 2.50000
 * Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 *
 * Constraints:
 * - nums1.length == m
 * - nums2.length == n
 * - 0 <= m <= 1000
 * - 0 <= n <= 1000
 * - 1 <= m + n <= 2000
 * - -10^6 <= nums1[i], nums2[i] <= 10^6
 */

import java.util.*;

public class MedianOfTwoSortedArrays {

    // Q1: What's the brute force approach and its time complexity?
    // A1: Merge both arrays and find median. Time: O(m+n), Space: O(m+n)
    public double findMedianSortedArraysBruteForce(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        int[] merged = new int[m + n];

        int i = 0, j = 0, k = 0;

        // Merge two sorted arrays
        while (i < m && j < n) {
            if (nums1[i] <= nums2[j]) {
                merged[k++] = nums1[i++];
            } else {
                merged[k++] = nums2[j++];
            }
        }

        // Add remaining elements from nums1
        while (i < m) {
            merged[k++] = nums1[i++];
        }

        // Add remaining elements from nums2
        while (j < n) {
            merged[k++] = nums2[j++];
        }

        // Find median
        int total = merged.length;
        if (total % 2 == 0) {
            return (merged[total / 2 - 1] + merged[total / 2]) / 2.0;
        } else {
            return merged[total / 2];
        }
    }

    // Q2: Can we find median without fully merging arrays?
    // A2: Yes! We only need to find middle elements. Time: O(m+n), Space: O(1)
    public double findMedianSortedArraysOptimizedMerge(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        int total = m + n;
        int half = total / 2;

        int i = 0, j = 0;
        int prev = 0, curr = 0;

        // Iterate until we reach the middle
        for (int count = 0; count <= half; count++) {
            prev = curr;

            if (i < m && (j >= n || nums1[i] <= nums2[j])) {
                curr = nums1[i++];
            } else {
                curr = nums2[j++];
            }
        }

        // Return median based on odd/even total length
        if (total % 2 == 0) {
            return (prev + curr) / 2.0;
        } else {
            return curr;
        }
    }

    // Q3: How can we achieve O(log(m+n)) time complexity?
    // A3: Use binary search on the smaller array. Find the correct partition.
    public double findMedianSortedArraysBinarySearch(int[] nums1, int[] nums2) {
        // Ensure nums1 is the smaller array
        if (nums1.length > nums2.length) {
            return findMedianSortedArraysBinarySearch(nums2, nums1);
        }

        int m = nums1.length;
        int n = nums2.length;
        int left = 0, right = m;

        while (left <= right) {
            int partition1 = (left + right) / 2;
            int partition2 = (m + n + 1) / 2 - partition1;

            // Get max elements on left side
            int maxLeft1 = (partition1 == 0) ? Integer.MIN_VALUE : nums1[partition1 - 1];
            int maxLeft2 = (partition2 == 0) ? Integer.MIN_VALUE : nums2[partition2 - 1];

            // Get min elements on right side
            int minRight1 = (partition1 == m) ? Integer.MAX_VALUE : nums1[partition1];
            int minRight2 = (partition2 == n) ? Integer.MAX_VALUE : nums2[partition2];

            // Check if we found the correct partition
            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
                // If total length is even
                if ((m + n) % 2 == 0) {
                    return (Math.max(maxLeft1, maxLeft2) + Math.min(minRight1, minRight2)) / 2.0;
                } else {
                    return Math.max(maxLeft1, maxLeft2);
                }
            } else if (maxLeft1 > minRight2) {
                right = partition1 - 1;
            } else {
                left = partition1 + 1;
            }
        }

        throw new IllegalArgumentException("Input arrays are not sorted");
    }

    // Q4: What if one array is empty?
    // A4: Handle edge case where one array is empty
    public double findMedianSortedArraysWithEmptyCheck(int[] nums1, int[] nums2) {
        if (nums1.length == 0) {
            int n = nums2.length;
            if (n % 2 == 0) {
                return (nums2[n / 2 - 1] + nums2[n / 2]) / 2.0;
            }
            return nums2[n / 2];
        }

        if (nums2.length == 0) {
            int m = nums1.length;
            if (m % 2 == 0) {
                return (nums1[m / 2 - 1] + nums1[m / 2]) / 2.0;
            }
            return nums1[m / 2];
        }

        // Use binary search approach
        return findMedianSortedArraysBinarySearch(nums1, nums2);
    }

    // Q5: How does the binary search partitioning work?
    /**
     * A5: The key insight is to partition both arrays such that:
     * - All elements on the left are smaller than all elements on the right
     * - The left partition has the same number of elements as right (or one more)
     *
     * For correct partition:
     * - maxLeft1 <= minRight2
     * - maxLeft2 <= minRight1
     *
     * If these conditions are met, the median is:
     * - Odd total length: max(maxLeft1, maxLeft2)
     * - Even total length: (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
     */

    // Q6: What's the step-by-step process for binary search approach?
    public double findMedianSortedArraysDetailed(int[] nums1, int[] nums2) {
        /**
         * Step 1: Ensure nums1 is smaller (for efficiency)
         * Step 2: Binary search on nums1 to find partition point
         * Step 3: Calculate corresponding partition in nums2
         * Step 4: Check if partition is valid
         * Step 5: Return median based on partition
         */
        if (nums1.length > nums2.length) {
            return findMedianSortedArraysDetailed(nums2, nums1);
        }

        int m = nums1.length;
        int n = nums2.length;
        int imin = 0, imax = m;
        int halfLen = (m + n + 1) / 2;

        while (imin <= imax) {
            int i = (imin + imax) / 2;
            int j = halfLen - i;

            if (i < m && nums2[j - 1] > nums1[i]) {
                // i is too small, increase it
                imin = i + 1;
            } else if (i > 0 && nums1[i - 1] > nums2[j]) {
                // i is too big, decrease it
                imax = i - 1;
            } else {
                // Found the correct partition
                int maxOfLeft;
                if (i == 0) {
                    maxOfLeft = nums2[j - 1];
                } else if (j == 0) {
                    maxOfLeft = nums1[i - 1];
                } else {
                    maxOfLeft = Math.max(nums1[i - 1], nums2[j - 1]);
                }

                if ((m + n) % 2 == 1) {
                    return maxOfLeft;
                }

                int minOfRight;
                if (i == m) {
                    minOfRight = nums2[j];
                } else if (j == n) {
                    minOfRight = nums1[i];
                } else {
                    minOfRight = Math.min(nums1[i], nums2[j]);
                }

                return (maxOfLeft + minOfRight) / 2.0;
            }
        }

        return 0.0;
    }

    // Q7: How do we handle arrays of very different sizes?
    // A7: Always binary search on the smaller array (already handled in our solution)
    public double findMedianSortedArraysSizeOptimized(int[] nums1, int[] nums2) {
        // This automatically chooses the smaller array for binary search
        return findMedianSortedArraysBinarySearch(nums1, nums2);
    }

    // Q8: What are common mistakes in this problem?
    /**
     * A8: Common mistakes include:
     * 1. Not handling empty arrays
     * 2. Not ensuring binary search on smaller array
     * 3. Off-by-one errors in partition calculation
     * 4. Not handling edge cases (i=0, i=m, j=0, j=n)
     * 5. Integer division issues with odd/even lengths
     * 6. Incorrect median calculation for even total length
     */

    // Q9: Can we use a different approach with heaps?
    // A9: Yes, but it won't meet the O(log(m+n)) requirement
    public double findMedianSortedArraysHeap(int[] nums1, int[] nums2) {
        /**
         * Using two heaps approach (similar to Find Median from Data Stream)
         * Time: O((m+n)log(m+n)), Space: O(m+n)
         * This doesn't meet the optimal time complexity requirement.
         */
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a); // Left half
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(); // Right half

        // Add all elements
        for (int num : nums1) {
            addToHeaps(maxHeap, minHeap, num);
        }
        for (int num : nums2) {
            addToHeaps(maxHeap, minHeap, num);
        }

        if (maxHeap.size() > minHeap.size()) {
            return maxHeap.peek();
        }
        return (maxHeap.peek() + minHeap.peek()) / 2.0;
    }

    private void addToHeaps(PriorityQueue<Integer> maxHeap, PriorityQueue<Integer> minHeap, int num) {
        if (maxHeap.isEmpty() || num <= maxHeap.peek()) {
            maxHeap.offer(num);
        } else {
            minHeap.offer(num);
        }

        // Balance heaps
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.offer(maxHeap.poll());
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.offer(minHeap.poll());
        }
    }

    // Q10: What are related problems and variations?
    /**
     * A10: Related problems include:
     * - Find Kth Smallest Element in Two Sorted Arrays
     * - Find Median from Data Stream
     * - Merge K Sorted Arrays
     * - Kth Smallest Element in a Sorted Matrix
     * - Find Median in a Row-wise Sorted Matrix
     *
     * Key concepts:
     * - Binary search on answer space
     * - Two pointers technique
     * - Heap-based approaches
     * - Partitioning strategies
     */

    public static void main(String[] args) {
        MedianOfTwoSortedArrays solution = new MedianOfTwoSortedArrays();

        // Test cases
        int[][][] testCases = {
            {{1, 3}, {2}},
            {{1, 2}, {3, 4}},
            {{0, 0}, {0, 0}},
            {{}, {1}},
            {{2}, {}},
            {{1, 3, 5, 7, 9}, {2, 4, 6, 8, 10}},
            {{1, 2}, {1, 2}},
            {{1}, {2, 3, 4, 5}}
        };

        double[] expected = {2.0, 2.5, 0.0, 1.0, 2.0, 5.5, 1.5, 3.0};

        System.out.println("Testing Binary Search Solution (Optimal):");
        for (int i = 0; i < testCases.length; i++) {
            int[] nums1 = testCases[i][0];
            int[] nums2 = testCases[i][1];
            double result = solution.findMedianSortedArraysBinarySearch(nums1, nums2);
            System.out.println("Input: nums1=" + Arrays.toString(nums1) + ", nums2=" + Arrays.toString(nums2));
            System.out.printf("Output: %.5f, Expected: %.5f%n", result, expected[i]);
            System.out.println("Correct: " + (Math.abs(result - expected[i]) < 1e-5));
            System.out.println();
        }
    }
}
