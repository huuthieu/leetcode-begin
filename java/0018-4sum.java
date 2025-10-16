import java.util.*;

/**
 * LeetCode Problem 0018: 4Sum
 *
 * Problem:
 * Given an array nums of n integers and an integer target, return all unique
 * quadruplets [nums[a], nums[b], nums[c], nums[d]] such that the sum equals target.
 *
 * Examples:
 * 1. Input: nums = [1,0,-1,0,-2,2], target = 0
 *    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
 */
public class FourSum {

    /**
     * Q1: Sorting + Two pointer approach
     *
     * Time Complexity: O(n^3)
     * Space Complexity: O(1)
     */
    public static List<List<Integer>> fourSumTwoPointer(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        int n = nums.length;

        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            if ((long) nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target)
                break;

            if ((long) nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target)
                continue;

            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;

                if ((long) nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target)
                    break;

                if ((long) nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target)
                    continue;

                int left = j + 1, right = n - 1;
                while (left < right) {
                    long sum = (long) nums[i] + nums[j] + nums[left] + nums[right];

                    if (sum == target) {
                        result.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));

                        while (left < right && nums[left] == nums[left + 1]) left++;
                        while (left < right && nums[right] == nums[right - 1]) right--;

                        left++;
                        right--;
                    } else if (sum < target) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }

        return result;
    }

    /**
     * Q2: Using Set for deduplication
     *
     * Time Complexity: O(n^3)
     * Space Complexity: O(n)
     */
    public static List<List<Integer>> fourSumSetDedup(int[] nums, int target) {
        Arrays.sort(nums);
        Set<List<Integer>> resultSet = new HashSet<>();
        int n = nums.length;

        for (int i = 0; i < n - 3; i++) {
            for (int j = i + 1; j < n - 2; j++) {
                int left = j + 1, right = n - 1;

                while (left < right) {
                    long sum = (long) nums[i] + nums[j] + nums[left] + nums[right];

                    if (sum == target) {
                        resultSet.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));
                        left++;
                        right--;
                    } else if (sum < target) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }

        return new ArrayList<>(resultSet);
    }

    /**
     * Q3: Reduce to 2Sum using nested loops
     *
     * Time Complexity: O(n^3)
     * Space Complexity: O(1)
     */
    public static List<List<Integer>> fourSumReduce2Sum(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        int n = nums.length;

        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            long target2Sum = target - nums[i];

            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;

                target2Sum -= nums[j];
                int left = j + 1, right = n - 1;

                while (left < right) {
                    long sum = (long) nums[left] + nums[right];

                    if (sum == target2Sum) {
                        result.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));

                        while (left < right && nums[left] == nums[left + 1]) left++;
                        while (left < right && nums[right] == nums[right - 1]) right--;

                        left++;
                        right--;
                    } else if (sum < target2Sum) {
                        left++;
                    } else {
                        right--;
                    }
                }

                target2Sum += nums[j];
            }
        }

        return result;
    }

    /**
     * Q4: With aggressive bounds checking
     *
     * Time Complexity: O(n^3)
     * Space Complexity: O(1)
     */
    public static List<List<Integer>> fourSumBounds(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        int n = nums.length;

        for (int i = 0; i < n - 3; i++) {
            if ((long) nums[i] * 4 > target) break;
            if ((long) nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target)
                continue;

            for (int j = i + 1; j < n - 2; j++) {
                if ((long) nums[i] + nums[j] * 3 > target) break;
                if ((long) nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target)
                    continue;

                int left = j + 1, right = n - 1;
                while (left < right) {
                    long sum = (long) nums[i] + nums[j] + nums[left] + nums[right];

                    if (sum == target) {
                        result.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));

                        while (left < right && nums[left] == nums[left + 1]) left++;
                        while (left < right && nums[right] == nums[right - 1]) right--;

                        left++;
                        right--;
                    } else if (sum < target) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }

        return result;
    }

    /**
     * Q5: Clean implementation
     *
     * Time Complexity: O(n^3)
     * Space Complexity: O(1)
     */
    public static List<List<Integer>> fourSumClean(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < nums.length - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            for (int j = i + 1; j < nums.length - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;

                int left = j + 1, right = nums.length - 1;
                long target2Sum = (long) target - nums[i] - nums[j];

                while (left < right) {
                    long sum = (long) nums[left] + nums[right];

                    if (sum == target2Sum) {
                        result.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));

                        while (left < right && nums[left] == nums[left + 1]) left++;
                        while (left < right && nums[right] == nums[right - 1]) right--;

                        left++;
                        right--;
                    } else if (sum < target2Sum) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }

        return result;
    }

    /**
     * Q6: Using TreeSet for ordered results
     *
     * Time Complexity: O(n^3 log n)
     * Space Complexity: O(n)
     */
    public static List<List<Integer>> fourSumTreeSet(int[] nums, int target) {
        Arrays.sort(nums);
        TreeSet<List<Integer>> resultSet = new TreeSet<>((a, b) -> {
            for (int i = 0; i < 4; i++) {
                if (!a.get(i).equals(b.get(i))) {
                    return a.get(i) - b.get(i);
                }
            }
            return 0;
        });

        int n = nums.length;
        for (int i = 0; i < n - 3; i++) {
            for (int j = i + 1; j < n - 2; j++) {
                int left = j + 1, right = n - 1;

                while (left < right) {
                    long sum = (long) nums[i] + nums[j] + nums[left] + nums[right];

                    if (sum == target) {
                        resultSet.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));
                        left++;
                        right--;
                    } else if (sum < target) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }

        return new ArrayList<>(resultSet);
    }

    /**
     * Q7: Nested two-pointer
     *
     * Time Complexity: O(n^3)
     * Space Complexity: O(1)
     */
    public static List<List<Integer>> fourSumNested(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            for (int j = i + 1; j < n; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;

                twoSum(nums, j, target - nums[i] - nums[j], result);
            }
        }

        return result;
    }

    private static void twoSum(int[] nums, int start, long target, List<List<Integer>> result) {
        int left = start + 1, right = nums.length - 1;

        while (left < right) {
            long sum = (long) nums[left] + nums[right];

            if (sum == target) {
                result.add(Arrays.asList((int)(target + nums[start + 1] - sum + nums[right]), nums[start + 1], nums[left], nums[right]));
                // Note: This approach is complex, simplified version above
                left++;
                right--;
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
    }

    /**
     * Q8: Using HashMap
     *
     * Time Complexity: O(n^3)
     * Space Complexity: O(n)
     */
    public static List<List<Integer>> fourSumHashMap(int[] nums, int target) {
        Arrays.sort(nums);
        Set<List<Integer>> resultSet = new HashSet<>();
        int n = nums.length;

        for (int i = 0; i < n - 3; i++) {
            for (int j = i + 1; j < n - 2; j++) {
                Map<Integer, Integer> map = new HashMap<>();

                for (int k = j + 1; k < n; k++) {
                    int complement = (int)(target - (long) nums[i] - nums[j] - nums[k]);

                    if (map.containsKey(complement)) {
                        List<Integer> quad = Arrays.asList(nums[i], nums[j], complement, nums[k]);
                        Collections.sort(quad);
                        resultSet.add(quad);
                    }

                    map.put(nums[k], k);
                }
            }
        }

        return new ArrayList<>(resultSet);
    }

    /**
     * Q9: Iterative approach
     *
     * Time Complexity: O(n^3)
     * Space Complexity: O(1)
     */
    public static List<List<Integer>> fourSumIterative(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < nums.length - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            for (int j = i + 1; j < nums.length - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;

                int left = j + 1, right = nums.length - 1;

                while (left < right) {
                    long sum = (long) nums[i] + nums[j] + nums[left] + nums[right];

                    if (sum == target) {
                        result.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));

                        while (left < right && nums[left] == nums[left + 1]) left++;
                        while (left < right && nums[right] == nums[right - 1]) right--;

                        left++;
                        right--;
                    } else if (sum < target) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }

        return result;
    }

    /**
     * Q10: Optimized with early termination
     *
     * Time Complexity: O(n^3)
     * Space Complexity: O(1)
     */
    public static List<List<Integer>> fourSumOptimized(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        int n = nums.length;

        for (int i = 0; i < n - 3; i++) {
            if (nums[i] > 0 && target > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;

                int left = j + 1, right = n - 1;

                while (left < right) {
                    long sum = (long) nums[i] + nums[j] + nums[left] + nums[right];

                    if (sum == target) {
                        result.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));

                        while (left < right && nums[left] == nums[left + 1]) left++;
                        while (left < right && nums[right] == nums[right - 1]) right--;

                        left++;
                        right--;
                    } else if (sum < target) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }

        return result;
    }

    // Test cases and main function
    public static void main(String[] args) {
        int[][] testCases = {
                {1, 0, -1, 0, -2, 2},
                {1000000000, 1000000000, 1000000000, 1000000000},
                {0, 0, 0, 0},
        };
        int[] targets = {0, -294967296, 0};
        int[] expectedSizes = {3, 0, 1};

        java.lang.reflect.Method[] methods = FourSum.class.getDeclaredMethods();
        List<java.lang.reflect.Method> testMethods = new ArrayList<>();

        for (java.lang.reflect.Method method : methods) {
            if (method.getName().startsWith("fourSum") &&
                method.getReturnType() == List.class) {
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
                    List<List<Integer>> result = (List<List<Integer>>)
                        method.invoke(null, (Object) testCases[i], targets[i]);
                    boolean passed = result.size() == expectedSizes[i];
                    allPassed = allPassed && passed;
                    String status = passed ? "✓" : "✗";
                    System.out.println("  " + status + " fourSum(" +
                        Arrays.toString(testCases[i]) + ", " + targets[i] + ") = " +
                        result + " (size: " + result.size() + ")");
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
