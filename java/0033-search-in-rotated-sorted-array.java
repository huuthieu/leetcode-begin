import java.util.*;

/**
 * LeetCode Problem 0033: Search in Rotated Sorted Array
 *
 * Problem:
 * There is an integer array nums sorted in ascending order (with distinct values),
 * and it is rotated at some unknown pivot. Given the rotated array nums and an integer target,
 * return the index of target if it is in nums, or -1 if it is not in nums.
 *
 * You must write an algorithm with O(log n) runtime complexity.
 *
 * Examples:
 * 1. Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
 * 2. Input: nums = [4,5,6,7,0,1,2], target = 3, Output: -1
 * 3. Input: nums = [1], target = 1, Output: 0
 */
public class SearchInRotatedSortedArray {

    /**
     * Q1: Binary search - identify which half is sorted
     *
     * Time Complexity: O(log n)
     * Space Complexity: O(1)
     */
    public static int searchBinaryHalves(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            // Left half is sorted
            if (nums[left] <= nums[mid]) {
                // Target is in the sorted left half
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                // Right half is sorted
                // Target is in the sorted right half
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return -1;
    }

    /**
     * Q2: Find pivot first, then binary search
     *
     * Time Complexity: O(log n)
     * Space Complexity: O(1)
     */
    public static int searchFindPivot(int[] nums, int target) {
        int pivot = findPivot(nums);

        // Check which side has the target
        if (target >= nums[0]) {
            return binarySearch(nums, target, 0, pivot - 1);
        } else {
            return binarySearch(nums, target, pivot, nums.length - 1);
        }
    }

    private static int findPivot(int[] nums) {
        int left = 0, right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }

    private static int binarySearch(int[] nums, int target, int left, int right) {
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }

    /**
     * Q3: Compare with boundaries
     *
     * Time Complexity: O(log n)
     * Space Complexity: O(1)
     */
    public static int searchBoundaryCompare(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            // Determine which half is sorted
            if (nums[left] <= nums[mid]) {
                // Left half is sorted
                if (nums[left] <= target && target <= nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                // Right half is sorted
                if (nums[mid] <= target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return -1;
    }

    /**
     * Q4: Iterative with comparison chain
     *
     * Time Complexity: O(log n)
     * Space Complexity: O(1)
     */
    public static int searchComparisonChain(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            if (nums[left] < nums[mid]) {
                // Left part is sorted
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else if (nums[left] > nums[mid]) {
                // Right part is sorted
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            } else {
                left++;
            }
        }

        return -1;
    }

    /**
     * Q5: Simple and clean version
     *
     * Time Complexity: O(log n)
     * Space Complexity: O(1)
     */
    public static int searchClean(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            // Determine which part is sorted
            if (nums[mid] >= nums[left]) {
                // Left part is sorted
                if (target < nums[mid] && target >= nums[left]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                // Right part is sorted
                if (target > nums[mid] && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return -1;
    }

    /**
     * Q6: Using division approach
     *
     * Time Complexity: O(log n)
     * Space Complexity: O(1)
     */
    public static int searchDivision(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            // Left half is in order
            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                // Right half is in order
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return -1;
    }

    /**
     * Q7: Recursive approach
     *
     * Time Complexity: O(log n)
     * Space Complexity: O(log n) for recursion stack
     */
    public static int searchRecursive(int[] nums, int target) {
        return searchRecursiveHelper(nums, target, 0, nums.length - 1);
    }

    private static int searchRecursiveHelper(int[] nums, int target, int left, int right) {
        if (left > right) {
            return -1;
        }

        int mid = left + (right - left) / 2;

        if (nums[mid] == target) {
            return mid;
        }

        // Left half is sorted
        if (nums[left] <= nums[mid]) {
            if (nums[left] <= target && target < nums[mid]) {
                return searchRecursiveHelper(nums, target, left, mid - 1);
            } else {
                return searchRecursiveHelper(nums, target, mid + 1, right);
            }
        } else {
            // Right half is sorted
            if (nums[mid] < target && target <= nums[right]) {
                return searchRecursiveHelper(nums, target, mid + 1, right);
            } else {
                return searchRecursiveHelper(nums, target, left, mid - 1);
            }
        }
    }

    /**
     * Q8: With early exits
     *
     * Time Complexity: O(log n)
     * Space Complexity: O(1)
     */
    public static int searchEarlyExit(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            // Determine sorted half
            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target <= nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                if (nums[mid] <= target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return -1;
    }

    /**
     * Q9: Using array operations
     *
     * Time Complexity: O(log n)
     * Space Complexity: O(1)
     */
    public static int searchArrayOps(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            // Check which side is properly sorted
            if ((nums[mid] >= nums[left] && target >= nums[left] && target < nums[mid]) ||
                (nums[mid] < nums[left] && (target >= nums[left] || target < nums[mid]))) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return -1;
    }

    /**
     * Q10: Compact version
     *
     * Time Complexity: O(log n)
     * Space Complexity: O(1)
     */
    public static int searchCompact(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) return mid;

            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return -1;
    }

    // Test cases and main function
    public static void main(String[] args) {
        int[][] testNums = {
            {4, 5, 6, 7, 0, 1, 2},
            {4, 5, 6, 7, 0, 1, 2},
            {1},
            {1, 3},
            {1, 3},
            {3, 1},
            {1, 2, 3, 4, 5, 6, 7},
            {7, 1, 2, 3, 4, 5, 6},
            {1, 2, 3, 4, 5, 6, 7},
            {3, 5, 1},
            {3, 1, 2},
            {4, 5, 6, 7, 0, 1, 2},
            {4, 5, 6, 7, 0, 1, 2},
            {1, 3, 5}
        };

        int[] testTargets = {0, 3, 1, 3, 1, 1, 7, 7, 1, 3, 2, 0, 2, 5};
        int[] expected = {4, -1, 0, 1, 0, 1, 6, 0, 0, 0, 2, 4, 6, 2};

        java.lang.reflect.Method[] methods = SearchInRotatedSortedArray.class.getDeclaredMethods();
        List<java.lang.reflect.Method> testMethods = new ArrayList<>();

        for (java.lang.reflect.Method method : methods) {
            if (method.getName().startsWith("search") &&
                method.getReturnType() == int.class &&
                method.getParameterCount() == 2) {
                testMethods.add(method);
            }
        }

        Collections.sort(testMethods, Comparator.comparing(java.lang.reflect.Method::getName));

        int questionNum = 1;
        for (java.lang.reflect.Method method : testMethods) {
            System.out.println("\nQ" + questionNum + ": " + method.getName());
            System.out.println("-".repeat(70));

            boolean allPassed = true;
            for (int i = 0; i < testNums.length; i++) {
                try {
                    int result = (int) method.invoke(null, testNums[i], testTargets[i]);
                    boolean passed = result == expected[i];
                    allPassed = allPassed && passed;
                    String status = passed ? "✓" : "✗";
                    System.out.println("  " + status + " search(" + Arrays.toString(testNums[i]) +
                        ", " + testTargets[i] + ") = " + result + " (expected: " + expected[i] + ")");
                } catch (Exception e) {
                    System.out.println("  ✗ Error: " + e.getMessage());
                    allPassed = false;
                }
            }

            if (allPassed) {
                System.out.println("  All tests passed!");
            }

            questionNum++;
        }
    }
}
