import java.util.*;

/**
 * LeetCode Problem 0015: 3Sum
 *
 * Problem:
 * Find all unique triplets in the array which gives the sum of zero.
 *
 * Note: The solution set must not contain duplicate triplets.
 *
 * Examples:
 * 1. Input: nums = [-1,0,1,2,-1,-4], Output: [[-1,-1,2],[-1,0,1]]
 * 2. Input: nums = [0], Output: []
 */
public class ThreeSum {

    /**
     * Q1: Sorting + Two Pointer (most efficient)
     *
     * Time Complexity: O(n^2)
     * Space Complexity: O(1) or O(n) depending on sorting
     */
    public static List<List<Integer>> threeSumSorting(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        int n = nums.length;

        for (int i = 0; i < n - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            if (nums[i] + nums[i + 1] + nums[i + 2] > 0) break;
            if (nums[i] + nums[n - 2] + nums[n - 1] < 0) continue;

            int target = -nums[i];
            int left = i + 1, right = n - 1;

            while (left < right) {
                int sum = nums[left] + nums[right];
                if (sum == target) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
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

        return result;
    }

    /**
     * Q2: HashSet based approach
     *
     * Time Complexity: O(n^2)
     * Space Complexity: O(n)
     */
    public static List<List<Integer>> threeSumHashset(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        Set<List<Integer>> resultSet = new HashSet<>();

        for (int i = 0; i < nums.length - 2; i++) {
            Set<Integer> seen = new HashSet<>();
            int target = -nums[i];

            for (int j = i + 1; j < nums.length; j++) {
                int complement = target - nums[j];
                if (seen.contains(complement)) {
                    List<Integer> triplet = Arrays.asList(nums[i], complement, nums[j]);
                    resultSet.add(triplet);
                }
                seen.add(nums[j]);
            }
        }

        result.addAll(resultSet);
        return result;
    }

    /**
     * Q3: Two pointer with different implementation
     *
     * Time Complexity: O(n^2)
     * Space Complexity: O(1)
     */
    public static List<List<Integer>> threeSumTwoPointer(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int left = i + 1, right = nums.length - 1;
            int target = -nums[i];

            while (left < right) {
                int sum = nums[left] + nums[right];
                if (sum == target) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));

                    while (left < right && nums[left + 1] == nums[left]) left++;
                    while (left < right && nums[right - 1] == nums[right]) right--;

                    left++;
                    right--;
                } else if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return result;
    }

    /**
     * Q4: Using Set for result deduplication
     *
     * Time Complexity: O(n^2)
     * Space Complexity: O(n)
     */
    public static List<List<Integer>> threeSumSetDedup(int[] nums) {
        Arrays.sort(nums);
        Set<List<Integer>> resultSet = new HashSet<>();

        for (int i = 0; i < nums.length - 2; i++) {
            int left = i + 1, right = nums.length - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    resultSet.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return new ArrayList<>(resultSet);
    }

    /**
     * Q5: Index-based approach
     *
     * Time Complexity: O(n^2)
     * Space Complexity: O(1)
     */
    public static List<List<Integer>> threeSumIndex(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        int n = nums.length;

        for (int i = 0; i < n - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int left = i + 1, right = n - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];

                if (sum == 0) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));

                    while (left + 1 < right && nums[left] == nums[left + 1]) left++;
                    while (right - 1 > left && nums[right] == nums[right - 1]) right--;

                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return result;
    }

    /**
     * Q6: Optimized with early termination
     *
     * Time Complexity: O(n^2)
     * Space Complexity: O(1)
     */
    public static List<List<Integer>> threeSumOptimized(int[] nums) {
        if (nums == null || nums.length < 3) return new ArrayList<>();

        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            twoSum(nums, i, result);
        }

        return result;
    }

    private static void twoSum(int[] nums, int i, List<List<Integer>> result) {
        int left = i + 1, right = nums.length - 1;
        int target = -nums[i];

        while (left < right) {
            int sum = nums[left] + nums[right];
            if (sum == target) {
                result.add(Arrays.asList(nums[i], nums[left], nums[right]));
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

    /**
     * Q7: Using TreeSet for sorted unique results
     *
     * Time Complexity: O(n^2 log n)
     * Space Complexity: O(n)
     */
    public static List<List<Integer>> threeSumTreeSet(int[] nums) {
        Arrays.sort(nums);
        TreeSet<List<Integer>> resultSet = new TreeSet<>((a, b) -> {
            for (int i = 0; i < 3; i++) {
                if (!a.get(i).equals(b.get(i))) {
                    return a.get(i) - b.get(i);
                }
            }
            return 0;
        });

        for (int i = 0; i < nums.length - 2; i++) {
            int left = i + 1, right = nums.length - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    resultSet.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return new ArrayList<>(resultSet);
    }

    /**
     * Q8: Optimized with bounds checking
     *
     * Time Complexity: O(n^2)
     * Space Complexity: O(1)
     */
    public static List<List<Integer>> threeSumBounds(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            if (nums[i] + nums[i + 1] + nums[i + 2] > 0) break;
            if (nums[i] + nums[nums.length - 2] + nums[nums.length - 1] < 0)
                continue;

            int target = -nums[i];
            int left = i + 1, right = nums.length - 1;

            while (left < right) {
                int sum = nums[left] + nums[right];
                if (sum == target) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
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

        return result;
    }

    /**
     * Q9: Stream-based approach
     *
     * Time Complexity: O(n^2)
     * Space Complexity: O(n)
     */
    public static List<List<Integer>> threeSumStream(int[] nums) {
        Arrays.sort(nums);
        Set<List<Integer>> resultSet = new HashSet<>();

        for (int i = 0; i < nums.length - 2; i++) {
            Set<Integer> seen = new HashSet<>();
            int target = -nums[i];

            for (int j = i + 1; j < nums.length; j++) {
                int complement = target - nums[j];
                if (seen.contains(complement)) {
                    resultSet.add(Arrays.asList(nums[i], complement, nums[j]));
                }
                seen.add(nums[j]);
            }
        }

        return new ArrayList<>(resultSet);
    }

    /**
     * Q10: Clean implementation with helper
     *
     * Time Complexity: O(n^2)
     * Space Complexity: O(1)
     */
    public static List<List<Integer>> threeSumClean(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            if (nums[i] > 0) break;

            int target = -nums[i];
            int left = i + 1, right = nums.length - 1;

            while (left < right) {
                int sum = nums[left] + nums[right];
                if (sum == target) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    skipDuplicates(nums, left, right, result);
                    left++;
                    right--;
                } else if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return result;
    }

    private static void skipDuplicates(int[] nums, int left, int right,
                                       List<List<Integer>> result) {
        while (left < right && nums[left] == nums[left + 1]) left++;
        while (left < right && nums[right] == nums[right - 1]) right--;
    }

    // Test cases and main function
    public static void main(String[] args) {
        int[][] testCases = {
                {-1, 0, 1, 2, -1, -4},
                {0},
                {-2, 0, 1, 1, 2},
                {0, 0, 0, 0},
        };

        List<List<Integer>>[] expectedResults = new List[]{
                Arrays.asList(
                        Arrays.asList(-1, -1, 2),
                        Arrays.asList(-1, 0, 1)
                ),
                new ArrayList<>(),
                Arrays.asList(
                        Arrays.asList(-2, 0, 2),
                        Arrays.asList(-2, 1, 1)
                ),
                Arrays.asList(Arrays.asList(0, 0, 0))
        };

        java.lang.reflect.Method[] methods = ThreeSum.class.getDeclaredMethods();
        List<java.lang.reflect.Method> testMethods = new ArrayList<>();

        for (java.lang.reflect.Method method : methods) {
            if (method.getName().startsWith("threeSum") &&
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
                        method.invoke(null, (Object) testCases[i]);

                    result.sort((a, b) -> {
                        for (int j = 0; j < 3; j++) {
                            if (!a.get(j).equals(b.get(j))) {
                                return a.get(j) - b.get(j);
                            }
                        }
                        return 0;
                    });

                    List<List<Integer>> expected = expectedResults[i];
                    expected.sort((a, b) -> {
                        for (int j = 0; j < 3; j++) {
                            if (!a.get(j).equals(b.get(j))) {
                                return a.get(j) - b.get(j);
                            }
                        }
                        return 0;
                    });

                    boolean passed = result.equals(expected);
                    allPassed = allPassed && passed;
                    String status = passed ? "✓" : "✗";
                    System.out.println("  " + status + " threeSum(" +
                        Arrays.toString(testCases[i]) + ") = " + result);
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
