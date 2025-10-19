/**
 * LeetCode Problem 0026: Remove Duplicates from Sorted Array
 *
 * Problem:
 * Given an integer array nums sorted in non-decreasing order, remove the duplicates
 * in-place such that each unique element appears only once.
 *
 * Examples:
 * 1. Input: nums = [1,1,2], Output: k = 2, nums = [1,2,_]
 * 2. Input: nums = [0,0,1,1,1,2,2,3,3,4], Output: k = 5, nums = [0,1,2,3,4,_,_,_,_,_]
 */

public class RemoveDuplicates {

    // Q1: Two-pointer approach (optimal)
    public static int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;

        int k = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) {
                nums[k] = nums[i];
                k++;
            }
        }

        return k;
    }

    // Q2: Single pointer with comparison
    public static int removeDuplicates2(int[] nums) {
        if (nums.length == 0) return 0;

        int pos = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[pos - 1]) {
                nums[pos] = nums[i];
                pos++;
            }
        }

        return pos;
    }

    // Q3: While loop approach
    public static int removeDuplicates3(int[] nums) {
        if (nums.length == 0) return 0;

        int i = 0;
        int j = 1;

        while (j < nums.length) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
            j++;
        }

        return i + 1;
    }

    // Q4: Window-based approach
    public static int removeDuplicates4(int[] nums) {
        if (nums.length == 0) return 0;

        int writeIdx = 0;
        int readIdx = 0;

        while (readIdx < nums.length) {
            if (readIdx == 0 || nums[readIdx] != nums[readIdx - 1]) {
                nums[writeIdx] = nums[readIdx];
                writeIdx++;
            }
            readIdx++;
        }

        return writeIdx;
    }

    // Helper method to print array
    private static void printArray(int[] arr, int k) {
        System.out.print("[");
        for (int i = 0; i < k; i++) {
            System.out.print(arr[i]);
            if (i < k - 1) System.out.print(",");
        }
        System.out.println("]");
    }

    public static void main(String[] args) {
        int[] test1 = {1, 1, 2};
        System.out.println("Q1: removeDuplicates");
        int k1 = removeDuplicates(test1);
        System.out.print("  Result: k = " + k1 + ", nums = ");
        printArray(test1, k1);

        int[] test2 = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
        System.out.println("\nQ2: removeDuplicates2");
        int k2 = removeDuplicates2(test2);
        System.out.print("  Result: k = " + k2 + ", nums = ");
        printArray(test2, k2);
    }
}
