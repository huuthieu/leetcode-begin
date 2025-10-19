/**
 * LeetCode Problem 0027: Remove Element
 *
 * Problem:
 * Given an integer array nums and an integer val, remove all occurrences of val
 * in nums in-place. The order of the elements may be changed.
 *
 * Examples:
 * 1. Input: nums = [3,2,2,3], val = 3, Output: k = 2, nums = [2,2,_,_]
 * 2. Input: nums = [0,1,2,2,3,0,4,2], val = 2, Output: k = 5, nums = [0,1,4,0,3,_,_,_]
 */

public class RemoveElement {

    // Q1: Two-pointer approach (optimal)
    public static int removeElement(int[] nums, int val) {
        int k = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }

    // Q2: Two-pointer from ends
    public static int removeElementFromEnds(int[] nums, int val) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            if (nums[left] == val) {
                nums[left] = nums[right];
                right--;
            } else {
                left++;
            }
        }

        return left;
    }

    // Q3: Position tracking
    public static int removeElementPositionTrack(int[] nums, int val) {
        int pos = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[pos] = nums[i];
                pos++;
            }
        }
        return pos;
    }

    // Q4: Count first approach
    public static int removeElementCountFirst(int[] nums, int val) {
        int count = 0;
        for (int num : nums) {
            if (num != val) {
                count++;
            }
        }

        int j = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[j] = nums[i];
                j++;
            }
        }

        return count;
    }

    // Q5: Iterator-based removal
    public static int removeElementIterator(int[] nums, int val) {
        int newLen = 0;
        for (int num : nums) {
            if (num != val) {
                nums[newLen] = num;
                newLen++;
            }
        }
        return newLen;
    }

    // Helper method to print result
    private static void printResult(int[] nums, int k, int val) {
        System.out.print("  [");
        for (int i = 0; i < k; i++) {
            System.out.print(nums[i]);
            if (i < k - 1) System.out.print(",");
        }
        System.out.println("]");
    }

    public static void main(String[] args) {
        int[] test1 = {3, 2, 2, 3};
        System.out.println("Q1: removeElement (Two-pointer)");
        int k1 = removeElement(test1, 3);
        System.out.println("  k = " + k1);
        printResult(test1, k1, 3);

        int[] test2 = {0, 1, 2, 2, 3, 0, 4, 2};
        System.out.println("\nQ2: removeElement (From Ends)");
        int k2 = removeElementFromEnds(test2.clone(), 2);
        System.out.println("  k = " + k2);

        int[] test3 = {1, 2, 3, 4, 5};
        System.out.println("\nQ3: removeElement (Position Track)");
        int k3 = removeElementPositionTrack(test3, 3);
        System.out.println("  k = " + k3);
        printResult(test3, k3, 3);
    }
}
