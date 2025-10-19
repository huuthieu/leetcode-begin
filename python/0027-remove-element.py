"""
LeetCode Problem 0027: Remove Element

Problem:
Given an integer array nums and an integer val, remove all occurrences of val
in nums in-place. The order of the elements may be changed.

Return k after placing the final result in the first k elements of nums.

Examples:
1. Input: nums = [3,2,2,3], val = 3, Output: k = 2, nums = [2,2,_,_]
2. Input: nums = [0,1,2,2,3,0,4,2], val = 2, Output: k = 5, nums = [0,1,4,0,3,_,_,_]

Constraints:
- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100
"""

from typing import List


# Q1: Two-pointer approach (optimal)
def removeElement_two_pointer(nums: List[int], val: int) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Approach: Use two pointers - one to write, one to scan. Skip val elements.
    """
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


# Q2: Two-pointer from ends
def removeElement_from_ends(nums: List[int], val: int) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Approach: Use pointers from both ends to reduce writes.
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        if nums[left] == val:
            nums[left] = nums[right]
            right -= 1
        else:
            left += 1

    return left


# Q3: Single pass with position tracking
def removeElement_position_track(nums: List[int], val: int) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Approach: Track position and only update when necessary.
    """
    pos = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[pos] = nums[i]
            pos += 1
    return pos


# Q4: Using list comprehension (not optimal)
def removeElement_comprehension(nums: List[int], val: int) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    Approach: Use list operations (not in-place, for comparison).
    """
    filtered = [x for x in nums if x != val]
    for i in range(len(filtered)):
        nums[i] = filtered[i]
    return len(filtered)


# Q5: While loop approach
def removeElement_while(nums: List[int], val: int) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Approach: Use while loop to iterate and modify.
    """
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums[i] = nums[-1]
            nums.pop()
        else:
            i += 1
    return len(nums)


# Q6: Count first approach
def removeElement_count_first(nums: List[int], val: int) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Approach: Count occurrences first, then reorder.
    """
    count = 0
    for num in nums:
        if num != val:
            count += 1

    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1

    return count


# Q7: In-place swap approach
def removeElement_swap(nums: List[int], val: int) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Approach: Swap values and shrink array conceptually.
    """
    if not nums:
        return 0

    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k], nums[i] = nums[i], nums[k]
            k += 1

    return k


# Q8: Iterator-based removal
def removeElement_iterator(nums: List[int], val: int) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Approach: Iterator-based approach to track non-val elements.
    """
    new_len = 0
    for num in nums:
        if num != val:
            nums[new_len] = num
            new_len += 1
    return new_len


# Q9: Reverse iteration approach
def removeElement_reverse(nums: List[int], val: int) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Approach: Use reverse iteration to handle removals.
    """
    i = len(nums) - 1
    count = 0

    while i >= 0:
        if nums[i] == val:
            nums.pop(i)
            count += 1
        i -= 1

    return len(nums)


if __name__ == "__main__":
    test_cases = [
        ([3, 2, 2, 3], 3, 2, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4]),
        ([1], 1, 0, []),
        ([1, 2], 3, 2, [1, 2]),
        ([2], 2, 0, []),
        ([1, 2, 3, 4, 5], 3, 4, [1, 2, 4, 5]),
        ([], 0, 0, []),
    ]

    functions = [
        removeElement_two_pointer,
        removeElement_from_ends,
        removeElement_position_track,
        removeElement_comprehension,
        removeElement_count_first,
        removeElement_swap,
        removeElement_iterator,
    ]

    for i, func in enumerate(functions, 1):
        print(f"\nQ{i}: {func.__name__}")
        print("-" * 70)
        all_passed = True
        for nums, val, expected_k, expected_arr in test_cases:
            nums_copy = nums.copy()
            k = func(nums_copy, val)
            result_arr = sorted(nums_copy[:k])
            expected_arr_sorted = sorted(expected_arr)
            passed = k == expected_k and result_arr == expected_arr_sorted
            all_passed = all_passed and passed
            status = "✓" if passed else "✗"
            print(f"  {status} removeElement({nums}, {val}) -> k={k}")

        if all_passed:
            print(f"  All tests passed!")
