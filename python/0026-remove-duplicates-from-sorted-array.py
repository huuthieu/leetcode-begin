"""
LeetCode Problem 0026: Remove Duplicates from Sorted Array

Problem:
Given an integer array nums sorted in non-decreasing order, remove the duplicates
in-place such that each unique element appears only once. The relative order of
the elements should be kept the same.

Return k after placing the final result in the first k elements of nums.

Examples:
1. Input: nums = [1,1,2], Output: k = 2, nums = [1,2,_]
2. Input: nums = [0,0,1,1,1,2,2,3,3,4], Output: k = 5, nums = [0,1,2,3,4,_,_,_,_,_]

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order
"""

from typing import List


# Q1: Two-pointer approach (optimal)
def removeDuplicates_two_pointer(nums: List[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Approach: Use two pointers - one for position to fill, one for scanning.
    """
    if not nums:
        return 0

    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k


# Q2: Single pointer with comparison
def removeDuplicates_single_pointer(nums: List[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Approach: Use single pointer and compare with previous element.
    """
    if not nums:
        return 0

    pos = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[pos - 1]:
            nums[pos] = nums[i]
            pos += 1

    return pos


# Q3: Using set (not optimal but valid)
def removeDuplicates_set(nums: List[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    Approach: Use set to track unique values, then rebuild array.
    """
    if not nums:
        return 0

    unique = sorted(set(nums))
    for i in range(len(unique)):
        nums[i] = unique[i]

    return len(unique)


# Q4: Dictionary tracking indices
def removeDuplicates_dict(nums: List[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    Approach: Track seen elements and their positions.
    """
    if not nums:
        return 0

    seen = {}
    pos = 0

    for i, num in enumerate(nums):
        if num not in seen:
            seen[num] = pos
            nums[pos] = num
            pos += 1

    return pos


# Q5: Counting approach
def removeDuplicates_counting(nums: List[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Approach: Count unique elements while iterating.
    """
    if not nums:
        return 0

    k = 1
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            nums[k] = nums[i]
            k += 1

    return k


# Q6: Iterator-based approach
def removeDuplicates_iterator(nums: List[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Approach: Use iterator to track position and value.
    """
    if not nums:
        return 0

    prev_pos = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[prev_pos]:
            prev_pos += 1
            nums[prev_pos] = nums[i]

    return prev_pos + 1


# Q7: Window-based approach
def removeDuplicates_window(nums: List[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Approach: Use sliding window concept.
    """
    if not nums:
        return 0

    write_idx = 0
    read_idx = 0

    while read_idx < len(nums):
        if read_idx == 0 or nums[read_idx] != nums[read_idx - 1]:
            nums[write_idx] = nums[read_idx]
            write_idx += 1
        read_idx += 1

    return write_idx


# Q8: Using while loop with increment
def removeDuplicates_while(nums: List[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Approach: While loop to process elements.
    """
    if not nums:
        return 0

    i = 0
    j = 1

    while j < len(nums):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
        j += 1

    return i + 1


if __name__ == "__main__":
    test_cases = [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([1], 1, [1]),
        ([1, 2], 2, [1, 2]),
        ([1, 1], 1, [1]),
        ([1, 2, 3], 3, [1, 2, 3]),
        ([0], 1, [0]),
        ([-1, 0, 0, 0, 3, 3], 3, [-1, 0, 3]),
    ]

    functions = [
        removeDuplicates_two_pointer,
        removeDuplicates_single_pointer,
        removeDuplicates_set,
        removeDuplicates_dict,
        removeDuplicates_counting,
        removeDuplicates_iterator,
        removeDuplicates_window,
        removeDuplicates_while,
    ]

    for i, func in enumerate(functions, 1):
        print(f"\nQ{i}: {func.__name__}")
        print("-" * 70)
        all_passed = True
        for nums, expected_k, expected_arr in test_cases:
            nums_copy = nums.copy()
            k = func(nums_copy)
            result_arr = nums_copy[:k]
            passed = k == expected_k and result_arr == expected_arr
            all_passed = all_passed and passed
            status = "✓" if passed else "✗"
            print(f"  {status} removeDuplicates({nums}) -> k={k}, arr={result_arr}")

        if all_passed:
            print(f"  All tests passed!")
