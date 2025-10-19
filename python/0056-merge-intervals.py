"""
LeetCode 56: Merge Intervals

Problem:
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping
intervals, and return an array of the non-overlapping intervals that cover all the
intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^4

Time Complexity: O(n log n) due to sorting
Space Complexity: O(n) for the result
"""


# Approach 1: Sort + Merge - OPTIMAL
def merge_intervals(intervals):
    """
    Sort intervals by start time, then merge overlapping ones

    Algorithm:
    1. Sort intervals by start time
    2. Iterate through sorted intervals
    3. If current interval overlaps with last merged interval, merge them
    4. Otherwise, add current interval to result

    Two intervals [a, b] and [c, d] overlap if: a <= c <= b

    Time: O(n log n) - dominated by sorting
    Space: O(n) - for result array (not counting sort space)
    """
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        current = intervals[i]
        last_merged = merged[-1]

        # Check if current interval overlaps with last merged interval
        if current[0] <= last_merged[1]:
            # Merge: extend the end of last merged interval
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # No overlap: add current interval as new
            merged.append(current)

    return merged


# Approach 2: Sort + Merge (slightly different style)
def merge_intervals_v2(intervals):
    """
    Same approach but with cleaner code style

    Time: O(n log n)
    Space: O(n)
    """
    if not intervals:
        return []

    intervals.sort()  # Sort by first element by default
    result = []

    for interval in intervals:
        # If result is empty or no overlap, add interval
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            # Merge with last interval
            result[-1][1] = max(result[-1][1], interval[1])

    return result


# Approach 3: Using Stack
def merge_intervals_stack(intervals):
    """
    Use a stack to store merged intervals

    Time: O(n log n)
    Space: O(n)
    """
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    stack = [intervals[0]]

    for i in range(1, len(intervals)):
        current = intervals[i]
        top = stack[-1]

        if current[0] <= top[1]:
            # Merge
            top[1] = max(top[1], current[1])
        else:
            stack.append(current)

    return stack


# Follow-up 1: Check if a new interval can be added without merging
def can_add_without_merge(intervals, new_interval):
    """
    Check if adding new_interval would require merging

    Returns: True if no merge needed, False otherwise
    Time: O(n)
    """
    for interval in intervals:
        # Check for overlap
        if not (new_interval[1] < interval[0] or new_interval[0] > interval[1]):
            return False
    return True


# Follow-up 2: Insert a new interval (LeetCode 57)
def insert_interval(intervals, new_interval):
    """
    Insert new_interval into intervals and merge if necessary

    Time: O(n) - no sorting needed if input is already sorted
    Space: O(n)
    """
    result = []
    i = 0
    n = len(intervals)

    # Add all intervals that come before new_interval
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # Merge all overlapping intervals
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    result.append(new_interval)

    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result


# Follow-up 3: Count non-overlapping intervals after merging
def count_merged_intervals(intervals):
    """
    Return the number of intervals after merging

    Time: O(n log n)
    Space: O(1) if we don't count the sort
    """
    if not intervals:
        return 0

    intervals.sort()
    count = 1
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] > end:
            count += 1
            end = intervals[i][1]
        else:
            end = max(end, intervals[i][1])

    return count


# Follow-up 4: Find the minimum number of intervals to remove to make rest non-overlapping (LeetCode 435)
def erase_overlap_intervals(intervals):
    """
    Find minimum number of intervals to remove so that the rest don't overlap

    Greedy approach: Always keep interval with earliest end time

    Time: O(n log n)
    Space: O(1)
    """
    if not intervals:
        return 0

    # Sort by end time
    intervals.sort(key=lambda x: x[1])

    count = 0
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            # Overlap detected, remove this interval
            count += 1
        else:
            # No overlap, update end
            end = intervals[i][1]

    return count


# Test Cases
def test_merge_intervals():
    print("Testing Merge Intervals:\n")

    test_cases = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[1, 4], [0, 4]], [[0, 4]]),
        ([[1, 4], [0, 1]], [[0, 4]]),
        ([[1, 4], [2, 3]], [[1, 4]]),
        ([[1, 4]], [[1, 4]]),
        ([[1, 4], [5, 6]], [[1, 4], [5, 6]]),
        ([[1, 10], [2, 3], [4, 5], [6, 7], [8, 9]], [[1, 10]]),
    ]

    for intervals, expected in test_cases:
        # Test all approaches
        result1 = merge_intervals([list(interval) for interval in intervals])
        result2 = merge_intervals_v2([list(interval) for interval in intervals])
        result3 = merge_intervals_stack([list(interval) for interval in intervals])

        assert result1 == expected, f"Approach 1 failed: got {result1}, expected {expected}"
        assert result2 == expected, f"Approach 2 failed: got {result2}, expected {expected}"
        assert result3 == expected, f"Approach 3 failed: got {result3}, expected {expected}"

        print(f"[PASS] Input: {intervals}")
        print(f"       Output: {expected}\n")

    print("\nTesting Insert Interval:\n")

    insert_test_cases = [
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
        ([], [5, 7], [[5, 7]]),
        ([[1, 5]], [2, 3], [[1, 5]]),
        ([[1, 5]], [6, 8], [[1, 5], [6, 8]]),
    ]

    for intervals, new_interval, expected in insert_test_cases:
        result = insert_interval([list(i) for i in intervals], list(new_interval))
        assert result == expected, f"Insert failed: got {result}, expected {expected}"
        print(f"[PASS] Insert {new_interval} into {intervals}")
        print(f"       Result: {expected}\n")

    print("\nTesting Erase Overlap Intervals:\n")

    erase_test_cases = [
        ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
        ([[1, 2], [1, 2], [1, 2]], 2),
        ([[1, 2], [2, 3]], 0),
    ]

    for intervals, expected in erase_test_cases:
        result = erase_overlap_intervals([list(i) for i in intervals])
        assert result == expected, f"Erase failed: got {result}, expected {expected}"
        print(f"[PASS] Min intervals to remove from {intervals}: {expected}\n")


# Practice Questions
def practice_questions():
    """
    Q1: Why do we need to sort the intervals first?
    A1: Sorting by start time ensures that we process intervals in order,
        making it easy to check if current interval overlaps with the last
        merged one. Without sorting, we'd need to check against all previous
        intervals.

    Q2: What's the time complexity breakdown?
    A2: - Sorting: O(n log n)
        - Merging: O(n) single pass
        - Total: O(n log n) dominated by sorting

    Q3: Can we solve this without sorting?
    A3: Not in O(n log n) time. We could use a brute force O(n^2) approach
        or use more complex data structures like interval trees, but sorting
        is the most efficient standard approach.

    Q4: What if intervals are already sorted?
    A4: We can skip sorting and achieve O(n) time complexity. This is the
        case in the "Insert Interval" problem.

    Q5: How do we determine if two intervals overlap?
    A5: Intervals [a, b] and [c, d] overlap if: a <= c <= b or c <= a <= d
        Simplified: not (b < c or d < a)

    Q6: Why do we use max(last_merged[1], current[1]) when merging?
    A6: The current interval might be completely contained within the last
        merged interval. Example: [1, 6] and [2, 3]. The merged interval
        should be [1, 6], not [1, 3].

    Q7: What if we need to find total time covered by intervals?
    A7: Merge intervals first, then sum up the lengths of merged intervals.
        This avoids double-counting overlapping periods.

    Q8: Real-world applications?
    A8: - Meeting room scheduling
        - Calendar event merging
        - Resource allocation (CPU, memory time slots)
        - Flight scheduling
        - Task scheduling in operating systems

    Q9: How to handle closed vs open intervals?
    A9: For closed intervals [a, b], overlap if a <= c <= b
        For open intervals (a, b), overlap if a < c < b
        Adjust comparison operators accordingly.

    Q10: What if we need to find maximum overlap (most concurrent intervals)?
    A10: Use a different approach: create events for start (+1) and end (-1),
         sort events, track running count. Max count is the answer.
    """
    pass


# Follow-up Problems
def follow_up_problems():
    """
    1. LeetCode 57: Insert Interval - Insert into sorted intervals
       Solution: O(n) without sorting since input is sorted

    2. LeetCode 435: Non-overlapping Intervals - Min intervals to remove
       Solution: Greedy - always keep interval with earliest end time

    3. LeetCode 252: Meeting Rooms - Check if person can attend all meetings
       Solution: Sort and check for any overlap

    4. LeetCode 253: Meeting Rooms II - Min conference rooms needed
       Solution: Track concurrent meetings using start/end events

    5. LeetCode 986: Interval List Intersections - Find intersections of two lists
       Solution: Two pointers to traverse both lists

    6. LeetCode 452: Minimum Number of Arrows to Burst Balloons
       Solution: Similar to non-overlapping intervals

    7. LeetCode 715: Range Module - Track and query ranges
       Solution: Use TreeMap or segment tree for efficient queries
    """
    pass


if __name__ == "__main__":
    test_merge_intervals()
    print("="*50)
    print("All tests passed!")
    print("="*50)

    # Uncomment to see practice questions
    # help(practice_questions)
    # help(follow_up_problems)
