"""
LeetCode 53: Maximum Subarray

Problem:
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example:
nums = [-2,1,-3,4,-1,2,1,-5,4] => 6 (subarray [4,-1,2,1] has the largest sum = 6)
nums = [5,4,-1,7,8] => 23 (entire array)
nums = [-1] => -1
nums = [-100000] => -100000

Time Complexity: O(n)
Space Complexity: O(1) - Kadane's algorithm
"""


# Approach 1: Kadane's Algorithm - Optimal
def maxSubArray_Kadane(nums):
    """
    Kadane's Algorithm: Keep track of max_current and max_global.
    At each step, decide whether to extend the current subarray or start a new one.

    max_current = max(num, max_current + num)
    max_global = max(max_global, max_current)

    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0

    max_current = nums[0]
    max_global = nums[0]

    for num in nums[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)

    return max_global


# Approach 2: Dynamic Programming
def maxSubArray_DP(nums):
    """
    dp[i] = maximum sum ending at index i
    dp[i] = max(nums[i], dp[i-1] + nums[i])

    Time: O(n), Space: O(n)
    """
    if not nums:
        return 0

    dp = [0] * len(nums)
    dp[0] = nums[0]

    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])

    return max(dp)


# Approach 3: Divide and Conquer
def maxSubArray_DivideConquer(nums):
    """
    Divide array in half, find max subarray in left, right, and crossing middle.

    Time: O(n log n), Space: O(log n) for recursion
    """

    def helper(left, right):
        if left == right:
            return nums[left]

        mid = (left + right) // 2

        left_max = helper(left, mid)
        right_max = helper(mid + 1, right)

        # Find max crossing the middle
        left_sum = 0
        max_left = float("-inf")
        for i in range(mid, left - 1, -1):
            left_sum += nums[i]
            max_left = max(max_left, left_sum)

        right_sum = 0
        max_right = float("-inf")
        for i in range(mid + 1, right + 1):
            right_sum += nums[i]
            max_right = max(max_right, right_sum)

        cross_max = max_left + max_right

        return max(left_max, right_max, cross_max)

    return helper(0, len(nums) - 1)


# Approach 4: Brute Force (for understanding)
def maxSubArray_BruteForce(nums):
    """
    Check all possible subarrays

    Time: O(n^2), Space: O(1)
    """
    max_sum = float("-inf")

    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)

    return max_sum


# Approach 5: Kadane with Tracking
def maxSubArray_KadaneTracking(nums):
    """
    Kadane's algorithm with tracking of subarray indices
    """
    max_current = nums[0]
    max_global = nums[0]
    start = 0
    end = 0
    s = 0

    for i in range(1, len(nums)):
        if nums[i] > max_current + nums[i]:
            max_current = nums[i]
            s = i
        else:
            max_current = max_current + nums[i]

        if max_current > max_global:
            max_global = max_current
            start = s
            end = i

    print(f"Subarray: {nums[start:end+1]}")
    return max_global


# Test Cases
def test_maxSubArray():
    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([5, 4, -1, 7, 8], 23),
        ([-1], -1),
        ([-100000], -100000),
        ([1], 1),
        ([-2, -3, -1], -1),
        ([1, 2, 3, 4, 5], 15),
        ([-5, -2, 5, -3, 5], 10),
    ]

    for nums, expected in test_cases:
        result_kadane = maxSubArray_Kadane(nums)
        result_dp = maxSubArray_DP(nums)
        result_div = maxSubArray_DivideConquer(nums)
        result_brute = maxSubArray_BruteForce(nums)

        assert (
            result_kadane == expected
        ), f"Kadane failed: got {result_kadane}, expected {expected}"
        assert (
            result_dp == expected
        ), f"DP failed: got {result_dp}, expected {expected}"
        assert (
            result_div == expected
        ), f"DivideConquer failed: got {result_div}, expected {expected}"
        assert (
            result_brute == expected
        ), f"BruteForce failed: got {result_brute}, expected {expected}"

        print(f"nums={nums} => {expected} ✓")


if __name__ == "__main__":
    test_maxSubArray()
    print("\nAll tests passed!")
