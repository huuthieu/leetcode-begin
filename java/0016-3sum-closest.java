import java.util.*;

/**
 * LeetCode Problem 0016: 3Sum Closest
 *
 * Problem:
 * Given an integer array nums of length n and an integer target, find three integers
 * in nums such that the sum is closest to target.
 *
 * Return the sum of the three integers. You may assume each input has exactly one solution.
 *
 * Examples:
 * 1. Input: nums = [-1,2,1,-4], target = 1, Output: 2
 * 2. Input: nums = [0,0,0], target = 1, Output: 0
 */
public class ThreeSumClosest {

    /**
     * Q1: Two pointer approach (optimal)
     *
     * Time Complexity: O(n^2)
     * Space Complexity: O(1)
     */
    public static int threeSumClosestTwoPointer(int[] nums, int target) {
        Arrays.sort(nums);
        int n = nums.length;
        int closestSum = Integer.MAX_VALUE;
        int minDiff = Integer.MAX_VALUE;

        for (int i = 0; i < n - 2; i++) {
            int left = i + 1, right = n - 1;

            while (left < right) {
                int currentSum = nums[i] + nums[left] + nums[right];
                int diff = Math.abs(currentSum - target);

                if (diff < minDiff) {
                    minDiff = diff;
                    closestSum = currentSum;
                }

                if (currentSum == target) {
                    return currentSum;
                } else if (currentSum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return closestSum;
    }

    /**
     * Q2: Greedy with early termination
     *
     * Time Complexity: O(n^2)
     * Space Complexity: O(1)
     */
    public static int threeSumClosestGreedy(int[] nums, int target) {
        Arrays.sort(nums);
        int closest = Integer.MAX_VALUE;

        for (int i = 0; i < nums.length - 2; i++) {
            int left = i + 1, right = nums.length - 1;

            while (left < right) {
                int total = nums[i] + nums[left] + nums[right];
                int diff = Math.abs(total - target);

                if (Math.abs(closest - target) > diff) {
                    closest = total;
                }

                if (total == target) {
                    return total;
                } else if (total < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return closest;
    }

    /**
     * Q3: Optimized with bounds checking
     *
     * Time Complexity: O(n^2)
     * Space Complexity: O(1)
     */
    public static int threeSumClosestOptimized(int[] nums, int target) {
        Arrays.sort(nums);
        int n = nums.length;
        int result = nums[0] + nums[1] + nums[2];

        for (int i = 0; i < n - 2; i++) {
            int left = i + 1, right = n - 1;

            while (left < right) {
                int currentSum = nums[i] + nums[left] + nums[right];

                if (currentSum == target) {
                    return target;
                }

                if (Math.abs(currentSum - target) < Math.abs(result - target)) {
                    result = currentSum;
                }

                if (currentSum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return result;
    }

    /**
     * Q4: Clean implementation with distance tracking
     *
     * Time Complexity: O(n^2)
     * Space Complexity: O(1)
     */
    public static int threeSumClosestClean(int[] nums, int target) {
        Arrays.sort(nums);
        int closestSum = nums[0] + nums[1] + nums[2];
        int minDistance = Math.abs(closestSum - target);

        for (int i = 0; i < nums.length - 2; i++) {
            int left = i + 1, right = nums.length - 1;

            while (left < right) {
                int currentSum = nums[i] + nums[left] + nums[right];
                int distance = Math.abs(currentSum - target);

                if (distance < minDistance) {
                    minDistance = distance;
                    closestSum = currentSum;
                }

                if (currentSum == target) {
                    return currentSum;
                } else if (currentSum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return closestSum;
    }

    /**
     * Q5: Early exit optimization
     *
     * Time Complexity: O(n^2)
     * Space Complexity: O(1)
     */
    public static int threeSumClosestEarlyExit(int[] nums, int target) {
        Arrays.sort(nums);
        int best = nums[0] + nums[1] + nums[2];

        for (int i = 0; i < nums.length - 2; i++) {
            int left = i + 1, right = nums.length - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];

                if (sum == target) return target;

                if (Math.abs(sum - target) < Math.abs(best - target)) {
                    best = sum;
                }

                if (sum < target) left++;
                else right--;
            }
        }

        return best;
    }

    /**
     * Q6: Two-pointer with explicit difference tracking
     *
     * Time Complexity: O(n^2)
     * Space Complexity: O(1)
     */
    public static int threeSumClosestDifference(int[] nums, int target) {
        Arrays.sort(nums);
        int result = nums[0] + nums[1] + nums[2];
        int minDifference = Math.abs(result - target);

        for (int i = 0; i < nums.length - 2; i++) {
            int left = i + 1, right = nums.length - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                int diff = Math.abs(sum - target);

                if (diff < minDifference) {
                    minDifference = diff;
                    result = sum;
                }

                if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return result;
    }

    /**
     * Q7: Using helper method for clarity
     *
     * Time Complexity: O(n^2)
     * Space Complexity: O(1)
     */
    public static int threeSumClosestHelper(int[] nums, int target) {
        Arrays.sort(nums);
        int closest = nums[0] + nums[1] + nums[2];

        for (int i = 0; i < nums.length - 2; i++) {
            int currentClosest = findClosestTwoSum(nums, i, target - nums[i]);
            int sum = nums[i] + currentClosest;

            if (Math.abs(sum - target) < Math.abs(closest - target)) {
                closest = sum;
            }
        }

        return closest;
    }

    private static int findClosestTwoSum(int[] nums, int start, int target) {
        int left = start + 1, right = nums.length - 1;
        int closest = nums[left] + nums[right];

        while (left < right) {
            int sum = nums[left] + nums[right];
            if (Math.abs(sum - target) < Math.abs(closest - target)) {
                closest = sum;
            }

            if (sum < target) {
                left++;
            } else {
                right--;
            }
        }

        return closest;
    }

    /**
     * Q8: Stream-based approach for academic purposes
     *
     * Time Complexity: O(n^3) - less efficient
     * Space Complexity: O(n)
     */
    public static int threeSumClosestStream(int[] nums, int target) {
        int closest = nums[0] + nums[1] + nums[2];

        for (int i = 0; i < nums.length - 2; i++) {
            for (int j = i + 1; j < nums.length - 1; j++) {
                for (int k = j + 1; k < nums.length; k++) {
                    int sum = nums[i] + nums[j] + nums[k];
                    if (Math.abs(sum - target) < Math.abs(closest - target)) {
                        closest = sum;
                    }
                }
            }
        }

        return closest;
    }

    /**
     * Q9: Iterative with intermediate tracking
     *
     * Time Complexity: O(n^2)
     * Space Complexity: O(1)
     */
    public static int threeSumClosestIterative(int[] nums, int target) {
        Arrays.sort(nums);
        int n = nums.length;
        int closest = nums[0] + nums[1] + nums[2];

        for (int i = 0; i < n - 2; i++) {
            int left = i + 1, right = n - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];

                if (isCloser(sum, closest, target)) {
                    closest = sum;
                }

                if (sum == target) {
                    return target;
                } else if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return closest;
    }

    private static boolean isCloser(int sum, int current, int target) {
        return Math.abs(sum - target) < Math.abs(current - target);
    }

    /**
     * Q10: Optimized with bounds and early termination
     *
     * Time Complexity: O(n^2)
     * Space Complexity: O(1)
     */
    public static int threeSumClosestBounds(int[] nums, int target) {
        Arrays.sort(nums);
        int n = nums.length;
        int result = nums[0] + nums[1] + nums[2];

        for (int i = 0; i < n - 2; i++) {
            int left = i + 1, right = n - 1;
            int minSum = nums[i] + nums[left] + nums[left + 1];
            int maxSum = nums[i] + nums[right - 1] + nums[right];

            if (target < minSum) {
                if (minSum - target < Math.abs(result - target)) {
                    result = minSum;
                }
                continue;
            }

            if (target > maxSum) {
                if (target - maxSum < Math.abs(result - target)) {
                    result = maxSum;
                }
                continue;
            }

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];

                if (sum == target) return target;

                if (Math.abs(sum - target) < Math.abs(result - target)) {
                    result = sum;
                }

                if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return result;
    }

    // Test cases and main function
    public static void main(String[] args) {
        int[][] testCases = {
                {-1, 2, 1, -4},
                {0, 0, 0},
                {1, 1, 1, 0},
                {-1, -1, 1, 1, 0},
                {1, 2, 3, 4},
        };
        int[] targets = {1, 1, -100, 0, 5};
        int[] expected = {2, 0, 2, 0, 6};

        java.lang.reflect.Method[] methods = ThreeSumClosest.class.getDeclaredMethods();
        List<java.lang.reflect.Method> testMethods = new ArrayList<>();

        for (java.lang.reflect.Method method : methods) {
            if (method.getName().startsWith("threeSumClosest") &&
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
            for (int i = 0; i < testCases.length; i++) {
                try {
                    int result = (int) method.invoke(null, (Object) testCases[i], targets[i]);
                    boolean passed = result == expected[i];
                    allPassed = allPassed && passed;
                    String status = passed ? "✓" : "✗";
                    System.out.println("  " + status + " threeSumClosest(" +
                        Arrays.toString(testCases[i]) + ", " + targets[i] + ") = " +
                        result + " (expected: " + expected[i] + ")");
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
