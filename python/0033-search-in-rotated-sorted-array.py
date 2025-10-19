"""
LeetCode Problem 0033: Search in Rotated Sorted Array

Problem:
There is an integer array nums sorted in ascending order (with distinct values),
and it is rotated at some unknown pivot. Given the rotated array nums and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Examples:
1. Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
2. Input: nums = [4,5,6,7,0,1,2], target = 3, Output: -1
3. Input: nums = [1], target = 1, Output: 0
4. Input: nums = [1,3], target = 3, Output: 1

Constraints:
- 1 <= nums.length <= 5000
- -10^9 <= nums[i] <= 10^9
- All values of nums are unique
- nums is guaranteed to be rotated at some pivot
- -10^9 <= target <= 10^9
"""


# Q1: Binary search - identify which half is sorted, then search
def search_binary_halves(nums: list[int], target: int) -> int:
    """
    Time Complexity: O(log n)
    Space Complexity: O(1)

    Approach: Use binary search. At each step, determine which half is properly sorted,
    then decide whether target is in that sorted half or the other half.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            # Target is in the sorted left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            # Target is in the sorted right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# Q2: Find pivot first, then binary search
def search_find_pivot(nums: list[int], target: int) -> int:
    """
    Time Complexity: O(log n)
    Space Complexity: O(1)

    Approach: First find the pivot point (where rotation happens),
    then determine which half the target is in and binary search there.
    """
    def find_pivot():
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return left

    def binary_search(arr, target, left, right):
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    pivot = find_pivot()

    # Check which side has the target
    if target >= nums[0]:
        return binary_search(nums, target, 0, pivot - 1)
    else:
        return binary_search(nums, target, pivot, len(nums) - 1)


# Q3: Compare with boundaries
def search_boundary_compare(nums: list[int], target: int) -> int:
    """
    Time Complexity: O(log n)
    Space Complexity: O(1)

    Approach: Similar to Q1 but with explicit boundary comparisons.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Determine which half is sorted
        if nums[left] <= nums[mid]:
            # Left half is sorted
            if nums[left] <= target <= nums[mid]:
                # Target is in sorted left half
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            if nums[mid] <= target <= nums[right]:
                # Target is in sorted right half
                left = mid + 1
            else:
                right = mid - 1

    return -1


# Q4: Iterative with comparison chain
def search_comparison_chain(nums: list[int], target: int) -> int:
    """
    Time Complexity: O(log n)
    Space Complexity: O(1)

    Approach: Use a chain of comparisons to determine search direction.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Check if left part is sorted
        if nums[left] < nums[mid]:
            # Left part is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        elif nums[left] > nums[mid]:
            # Right part is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            # nums[left] == nums[mid], need to move left pointer
            left += 1

    return -1


# Q5: Simple and clean version
def search_clean(nums: list[int], target: int) -> int:
    """
    Time Complexity: O(log n)
    Space Complexity: O(1)

    Approach: Clean implementation with clear logic flow.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Determine which part is sorted
        if nums[mid] >= nums[left]:
            # Left part is sorted
            if target < nums[mid] and target >= nums[left]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right part is sorted
            if target > nums[mid] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# Q6: Using division approach
def search_division(nums: list[int], target: int) -> int:
    """
    Time Complexity: O(log n)
    Space Complexity: O(1)

    Approach: Explicitly divide the array and check each part.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Left half is in order
        if nums[left] <= nums[mid]:
            # Target in left half?
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is in order
        else:
            # Target in right half?
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# Q7: Recursive approach
def search_recursive(nums: list[int], target: int) -> int:
    """
    Time Complexity: O(log n)
    Space Complexity: O(log n) for recursion stack

    Approach: Use recursion with binary search logic.
    """
    def helper(left, right):
        if left > right:
            return -1

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                return helper(left, mid - 1)
            else:
                return helper(mid + 1, right)
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                return helper(mid + 1, right)
            else:
                return helper(left, mid - 1)

    return helper(0, len(nums) - 1)


# Q8: With early exits
def search_early_exit(nums: list[int], target: int) -> int:
    """
    Time Complexity: O(log n)
    Space Complexity: O(1)

    Approach: Add early exit conditions for optimization.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Check if target is beyond boundaries
        if target < nums[left] and target > nums[right]:
            return -1

        # Determine sorted half
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# Q9: Using modulo approach
def search_modulo(nums: list[int], target: int) -> int:
    """
    Time Complexity: O(log n)
    Space Complexity: O(1)

    Approach: Determine pivot and use modulo arithmetic.
    """
    left, right = 0, len(nums) - 1
    min_idx = 0

    # Find rotation point
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
        min_idx = left

    # Determine which sorted array to search in
    if target >= nums[0]:
        left, right = 0, min_idx - 1
    else:
        left, right = min_idx, len(nums) - 1

    # Standard binary search
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Q10: Compact version
def search_compact(nums: list[int], target: int) -> int:
    """
    Time Complexity: O(log n)
    Space Complexity: O(1)

    Approach: Most compact while maintaining clarity.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


if __name__ == "__main__":
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 1, 0),
        ([1, 3], 3, 1),
        ([1, 3], 1, 0),
        ([3, 1], 1, 1),
        ([1, 2, 3, 4, 5, 6, 7], 7, 6),
        ([7, 1, 2, 3, 4, 5, 6], 7, 0),
        ([1, 2, 3, 4, 5, 6, 7], 1, 0),
        ([3, 5, 1], 3, 0),
        ([3, 1, 2], 2, 2),
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 2, 6),
        ([1, 3, 5], 5, 2),
    ]

    functions = [
        search_binary_halves,
        search_find_pivot,
        search_boundary_compare,
        search_comparison_chain,
        search_clean,
        search_division,
        search_recursive,
        search_early_exit,
        search_modulo,
        search_compact,
    ]

    for i, func in enumerate(functions, 1):
        print(f"\nQ{i}: {func.__name__}")
        print("-" * 70)
        all_passed = True
        for nums, target, expected in test_cases:
            result = func(nums, target)
            passed = result == expected
            all_passed = all_passed and passed
            status = "✓" if passed else "✗"
            print(f"  {status} search({nums}, {target}) = {result} (expected: {expected})")

        if all_passed:
            print(f"  All tests passed!")
