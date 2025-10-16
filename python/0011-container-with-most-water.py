"""
LeetCode 0011: Container With Most Water

Problem Statement:
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum area of water that the container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The vertical lines are at indices 0 and 1. Line at 0 has height 1, line at 1 has height 8.
The area = min(1, 8) * (1 - 0) = 1 * 1 = 1. But the maximum is at indices 1 and 8 with heights 8 and 7.
Area = min(8, 7) * (8 - 1) = 7 * 7 = 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4
"""

# Practice Questions and Answers

# Q1: What's the brute force approach?
# A1: Check all pairs of lines. Time: O(n^2), Space: O(1)
def maxArea_brute_force(height):
    max_area = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            # Width is the distance between indices
            width = j - i
            # Height is the minimum of the two lines
            h = min(height[i], height[j])
            # Area is width * height
            area = width * h
            max_area = max(max_area, area)
    return max_area

# Q2: How can we optimize using two pointers?
# A2: Start from both ends and move the pointer with smaller height. Time: O(n), Space: O(1)
def maxArea_two_pointers(height):
    max_area = 0
    left = 0
    right = len(height) - 1

    while left < right:
        # Calculate current area
        width = right - left
        h = min(height[left], height[right])
        area = width * h
        max_area = max(max_area, area)

        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# Q3: Why does the two-pointer approach work?
# A3: Because area is limited by the shorter line. Moving the longer line inward can only decrease area.
# So we always move the shorter line hoping to find a taller line.
def maxArea_explanation():
    """
    Why two pointers works:
    - Area = min(h[i], h[j]) * (j - i)
    - We start with maximum width
    - If we move the taller line inward, width decreases and height can't increase (limited by shorter line)
    - So the area can only decrease
    - We must move the shorter line to have a chance of finding a taller line that increases area
    """
    pass

# Q4: What if we want to track the indices of the best container?
# A4: Modify to return both the area and the indices
def maxArea_with_indices(height):
    max_area = 0
    best_left = 0
    best_right = len(height) - 1
    left = 0
    right = len(height) - 1

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        area = width * h

        if area > max_area:
            max_area = area
            best_left = left
            best_right = right

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area, best_left, best_right

# Q5: How can we use dynamic programming approach?
# A5: Track the maximum area seen so far, but two pointers is still optimal
def maxArea_dp_thought():
    """
    DP approach would be:
    dp[i][j] = maximum area from index i to j
    But this is O(n^2) which is worse than two pointers
    Two pointers exploits the structure that we can only move inward
    """
    pass

# Q6: What about edge cases?
# A6: Empty array (won't happen per constraints), single element (won't happen), equal heights
def maxArea_with_validation(height):
    if not height or len(height) < 2:
        return 0
    return maxArea_two_pointers(height)

# Q7: How does the algorithm decide which pointer to move?
"""
A7: The algorithm moves the pointer with the smaller height because:
- Current area = min(h[left], h[right]) * width
- If we move the pointer with larger height, the minimum won't increase (limited by smaller)
- If we move the pointer with smaller height, we might find a taller line
- This greedy choice is optimal
"""

# Q8: Can we visualize the algorithm?
def maxArea_with_trace(height):
    """
    Example: height = [1,8,6,2,5,4,8,3,7]
    left=0, right=8: area = min(1,7) * 8 = 8, move left
    left=1, right=8: area = min(8,7) * 7 = 49, move right (8 > 7)
    left=1, right=7: area = min(8,3) * 6 = 18, move right
    ... continue until left >= right
    Maximum area found: 49
    """
    max_area = 0
    left = 0
    right = len(height) - 1

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        area = width * h
        max_area = max(max_area, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# Q9: What are variations of this problem?
"""
A9:
- Trapping Rain Water (two pointer with different logic)
- Rain Water II (2D version)
- Largest Rectangle in Histogram
- Maximum Product Subarray
"""

# Q10: Time and space complexity analysis
"""
A10:
Brute Force:
  Time: O(n^2) - checking all pairs
  Space: O(1) - no extra space

Two Pointers:
  Time: O(n) - each element visited once
  Space: O(1) - only using pointers

Two pointers is optimal for this problem because of the greedy property.
"""

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([2, 3, 4, 5, 18, 17, 6], 17),
        ([1], 0),  # Edge case: single element (won't happen per constraints)
    ]

    print("Testing all approaches:\n")

    for height, expected in test_cases:
        if len(height) < 2:
            continue  # Skip invalid cases per constraints

        brute = maxArea_brute_force(height)
        two_ptr = maxArea_two_pointers(height)
        indices = maxArea_with_indices(height)

        print(f"height = {height}")
        print(f"Expected: {expected}, Brute Force: {brute}, Two Pointers: {two_ptr}")
        print(f"Best container: indices ({indices[1]}, {indices[2]}), area = {indices[0]}")

        assert brute == expected, f"Brute force failed for {height}"
        assert two_ptr == expected, f"Two pointers failed for {height}"

        print("✓ Passed\n")
