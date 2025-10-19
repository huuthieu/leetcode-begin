/**
 * LeetCode 217: Contains Duplicate
 *
 * Problem:
 * Given an integer array nums, return true if any value appears at least twice in the array,
 * and return false if every element is distinct.
 *
 * Example:
 * nums = [1,2,3,1] => true
 * nums = [1,2,3,4] => false
 * nums = [99,99] => true
 */

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class ContainsDuplicate {

    // Approach 1: Hash Set
    public static boolean containsDuplicate_HashSet(int[] nums) {
        /**
         * Keep track of seen numbers using a set
         * Time: O(n), Space: O(n)
         */
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (seen.contains(num)) {
                return true;
            }
            seen.add(num);
        }
        return false;
    }

    // Approach 2: Sorting
    public static boolean containsDuplicate_Sorting(int[] nums) {
        /**
         * Sort the array, then check if any adjacent elements are equal
         * Time: O(n log n), Space: O(1) or O(n)
         */
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                return true;
            }
        }
        return false;
    }

    // Approach 3: Set Length Comparison
    public static boolean containsDuplicate_SetLength(int[] nums) {
        /**
         * If set length < array length, there are duplicates
         * Time: O(n), Space: O(n)
         */
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        return set.size() < nums.length;
    }

    // Approach 4: Early Exit
    public static boolean containsDuplicate_EarlyExit(int[] nums) {
        /**
         * Similar to hash set with explicit early exit
         * Time: O(n), Space: O(n)
         */
        if (nums.length <= 1) return false;

        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (seen.contains(num)) {
                return true;
            }
            seen.add(num);
        }
        return false;
    }

    // Test Cases
    public static void main(String[] args) {
        int[][] testCases = {
            {1, 2, 3, 1},
            {1, 2, 3, 4},
            {99, 99},
            {1},
            {1, 1},
            {1, 2, 3, 4, 5, 1},
            {-1, -1, -1},
            {0, 1, 2, 3, 4}
        };

        boolean[] expectedResults = {true, false, true, false, true, true, true, false};

        for (int i = 0; i < testCases.length; i++) {
            int[] nums = testCases[i];
            boolean expected = expectedResults[i];

            // Make copies since sorting modifies the array
            int[] copy1 = nums.clone();
            int[] copy2 = nums.clone();

            assert containsDuplicate_HashSet(nums) == expected : "HashSet failed";
            assert containsDuplicate_Sorting(copy1) == expected : "Sorting failed";
            assert containsDuplicate_SetLength(copy2) == expected : "SetLength failed";
            assert containsDuplicate_EarlyExit(nums) == expected : "EarlyExit failed";

            System.out.println("Test case " + i + ": " + expected + " ✓");
        }

        System.out.println("\nAll tests passed!");

        // Example usage
        int[] example = {1, 2, 3, 1};
        System.out.println("\nContains Duplicate Example: " + containsDuplicate_HashSet(example));
    }
}
