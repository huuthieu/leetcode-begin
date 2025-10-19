"""
LeetCode 42: Trapping Rain Water

Problem:
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: 6 units of rain water (shown in blue) are trapped on the map

Input: height = [4,2,0,3,2,5]
Output: 9

Time Complexity: O(n)
Space Complexity: O(n) for array approach, O(1) for two-pointer
"""


# Approach 1: Two Pointer - Most Optimal
def trap_TwoPointer(height):
    """
    Use two pointers from both ends.
    Water trapped at a position = min(max_left, max_right) - height[i]

    Key insight: We only need to know the maximum height on each side,
    we don't need to precompute all of them. We can maintain running maxes
    from both ends.

    Time: O(n), Space: O(1)
    """
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water_trapped = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water_trapped += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water_trapped += right_max - height[right]
            right -= 1

    return water_trapped


# Approach 2: DP with Pre-computed Max Heights
def trap_DP(height):
    """
    Pre-compute max heights to the left and right of each position.
    Then calculate water trapped at each position.

    Time: O(n), Space: O(n)
    """
    if not height:
        return 0

    n = len(height)
    left_max = [0] * n
    right_max = [0] * n

    # Compute max heights to the left
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    # Compute max heights to the right
    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    # Calculate water trapped
    water_trapped = 0
    for i in range(n):
        min_height = min(left_max[i], right_max[i])
        water_trapped += min_height - height[i]

    return water_trapped


# Approach 3: Stack-based
# Use stack to save patterns of descreasing and increasing of heights (-> <-)
def trap_Stack(height):
    """
    Use a stack to keep track of indices.
    When we find a bar higher than stack top, we calculate trapped water.

    Time: O(n), Space: O(n)
    """
    if not height:
        return 0

    stack = []
    water_trapped = 0

    for i, h in enumerate(height):
        while stack and h > height[stack[-1]]:
            top = stack.pop()

            if not stack:
                break

            width = i - stack[-1] - 1
            water_level = min(h, height[stack[-1]]) - height[top]
            water_trapped += width * water_level

        stack.append(i)

    return water_trapped


# Approach 4: Brute Force (O(n^2) - for understanding)
def trap_BruteForce(height):
    """
    For each element, find max to left and max to right
    Water trapped = min(left_max, right_max) - height[i]

    Time: O(n^2), Space: O(1)
    """
    if not height:
        return 0

    water_trapped = 0

    for i in range(len(height)):
        left_max = max(height[:i + 1]) if i >= 0 else 0
        right_max = max(height[i:]) if i < len(height) else 0

        water_level = min(left_max, right_max)
        water_trapped += max(0, water_level - height[i])

    return water_trapped


# Test Cases
def test_trap():
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([3, 0, 2, 0, 4], 7),
        ([2, 0, 2], 2),
        ([0, 1, 2, 3], 0),  # No water
        ([3, 2, 1, 0], 0),  # Decreasing
        ([], 0),
        ([5], 0),
        ([5, 5, 5], 0),
    ]

    for height, expected in test_cases:
        result_two_ptr = trap_TwoPointer(height)
        result_dp = trap_DP(height)
        result_stack = trap_Stack(height)
        result_brute = trap_BruteForce(height)

        assert (
            result_two_ptr == expected
        ), f"TwoPointer failed: got {result_two_ptr}, expected {expected}"
        assert (
            result_dp == expected
        ), f"DP failed: got {result_dp}, expected {expected}"
        assert (
            result_stack == expected
        ), f"Stack failed: got {result_stack}, expected {expected}"
        assert (
            result_brute == expected
        ), f"BruteForce failed: got {result_brute}, expected {expected}"

        print(f"height={height} => {expected} units ✓")


if __name__ == "__main__":
    test_trap()
    print("\nAll tests passed!")
