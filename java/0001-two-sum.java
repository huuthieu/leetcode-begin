/**
 * LeetCode 0001: Two Sum
 * 
 * Problem Statement:
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 * You can return the answer in any order.
 * 
 * Example 1:
 * Input: nums = [2,7,11,15], target = 9
 * Output: [0,1]
 * Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
 * 
 * Example 2:
 * Input: nums = [3,2,4], target = 6
 * Output: [1,2]
 * 
 * Example 3:
 * Input: nums = [3,3], target = 6
 * Output: [0,1]
 * 
 * Constraints:
 * - 2 <= nums.length <= 10^4
 * - -10^9 <= nums[i] <= 10^9
 * - -10^9 <= target <= 10^9
 * - Only one valid answer exists.
 */

import java.util.*;

public class TwoSum {
    
    // Q1: What's the brute force approach and its time complexity?
    // A1: Check every pair of numbers. Time: O(n^2), Space: O(1)
    public int[] twoSumBruteForce(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{};
    }
    
    // Q2: How can we optimize using a hash map?
    // A2: Store complement values with indices. Time: O(n), Space: O(n)
    public int[] twoSumHashMap(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seen.containsKey(complement)) {
                return new int[]{seen.get(complement), i};
            }
            seen.put(nums[i], i);
        }
        return new int[]{};
    }
    
    // Q3: What if we need to return the actual values instead of indices?
    // A3: Same logic, but return the values
    public int[] twoSumValues(int[] nums, int target) {
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            int complement = target - num;
            if (seen.contains(complement)) {
                return new int[]{complement, num};
            }
            seen.add(num);
        }
        return new int[]{};
    }
    
    // Q4: What if the array is sorted? Can we do better than O(n) space?
    // A4: Use two pointers approach. Time: O(n), Space: O(1)
    public int[] twoSumSorted(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left < right) {
            int currentSum = nums[left] + nums[right];
            if (currentSum == target) {
                return new int[]{left, right};
            } else if (currentSum < target) {
                left++;
            } else {
                right--;
            }
        }
        return new int[]{};
    }
    
    // Q5: What if there are multiple valid pairs? Return all of them.
    // A5: Continue searching instead of returning immediately
    public List<int[]> twoSumAllPairs(int[] nums, int target) {
        Map<Integer, List<Integer>> seen = new HashMap<>();
        List<int[]> result = new ArrayList<>();
        
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seen.containsKey(complement)) {
                for (int j : seen.get(complement)) {
                    result.add(new int[]{j, i});
                }
            }
            seen.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }
        return result;
    }
    
    // Q6: What about edge cases we should consider?
    // A6: Empty array, single element, no solution, duplicate numbers
    public int[] twoSumWithValidation(int[] nums, int target) {
        if (nums == null || nums.length < 2) {
            return new int[]{};
        }
        
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seen.containsKey(complement)) {
                return new int[]{seen.get(complement), i};
            }
            seen.put(nums[i], i);
        }
        return new int[]{};
    }
    
    // Q7: How would you handle very large numbers or potential overflow?
    // A7: Use long for calculations to prevent overflow
    public int[] twoSumSafe(int[] nums, int target) {
        Map<Long, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            long num = nums[i];
            long complement = (long) target - num;
            if (seen.containsKey(complement)) {
                return new int[]{seen.get(complement), i};
            }
            seen.put(num, i);
        }
        return new int[]{};
    }
    
    // Q8: What's the space-time tradeoff analysis?
    /**
     * A8: 
     * Brute Force: O(n^2) time, O(1) space
     * Hash Map: O(n) time, O(n) space
     * Two Pointers (sorted): O(n) time, O(1) space (but requires sorted array)
     * 
     * The hash map approach is generally preferred for unsorted arrays.
     */
    
    // Q9: How would you implement this without using built-in hash maps?
    // A9: Use a simple array-based approach (less efficient)
    public int[] twoSumNoHashMap(int[] nums, int target) {
        List<Integer> seen = new ArrayList<>();
        List<Integer> indices = new ArrayList<>();
        
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            int complementIndex = seen.indexOf(complement);
            if (complementIndex != -1) {
                return new int[]{indices.get(complementIndex), i};
            }
            seen.add(nums[i]);
            indices.add(i);
        }
        return new int[]{};
    }
    
    // Q10: What variations of this problem exist?
    /**
     * A10: Common variations include:
     * - Two Sum II (sorted array)
     * - Three Sum
     * - Four Sum
     * - Two Sum with BST
     * - Two Sum with duplicates allowed
     * - Two Sum closest to target
     * - Two Sum in a stream of data
     */
    
    public static void main(String[] args) {
        TwoSum solution = new TwoSum();
        
        // Test cases
        int[][] testNums = {
            {2, 7, 11, 15},
            {3, 2, 4},
            {3, 3},
            {1, 2, 3, 4, 5},
            {-1, -2, -3, -4, -5}
        };
        
        int[] targets = {9, 6, 6, 9, -8};
        int[][] expected = {
            {0, 1},
            {1, 2},
            {0, 1},
            {3, 4},
            {2, 4}
        };
        
        for (int i = 0; i < testNums.length; i++) {
            int[] result = solution.twoSumHashMap(testNums[i], targets[i]);
            System.out.println("Input: nums=" + Arrays.toString(testNums[i]) + ", target=" + targets[i]);
            System.out.println("Output: " + Arrays.toString(result) + ", Expected: " + Arrays.toString(expected[i]));
            System.out.println("Correct: " + Arrays.equals(result, expected[i]));
            System.out.println();
        }
    }
}
