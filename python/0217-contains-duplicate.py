"""
LeetCode 217: Contains Duplicate

Problem:
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example:
nums = [1,2,3,1] => True
nums = [1,2,3,4] => False
nums = [99,99] => True

Time Complexity: O(n) for hash set, O(n log n) for sorting
Space Complexity: O(n) for hash set, O(1) for sorting (with modified input)
"""


# Approach 1: Hash Set
def containsDuplicate_HashSet(nums):
    """
    Keep track of seen numbers using a set
    If we encounter a number already in the set, return True
    Time: O(n), Space: O(n)
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# Approach 2: Sorting
def containsDuplicate_Sorting(nums):
    """
    Sort the array, then check if any adjacent elements are equal
    Time: O(n log n), Space: O(1) or O(n) depending on sorting implementation
    """
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


# Approach 3: Set Length Comparison
def containsDuplicate_SetLength(nums):
    """
    If the length of the set is less than the length of the array,
    there must be duplicates
    Time: O(n), Space: O(n)
    """
    return len(set(nums)) < len(nums)


# Approach 4: Hash Map with Counter
def containsDuplicate_Counter(nums):
    """
    Count occurrences of each number
    Time: O(n), Space: O(n)
    """
    from collections import Counter

    count = Counter(nums)
    return any(v > 1 for v in count.values())


# Approach 5: Early Exit with Set
def containsDuplicate_EarlyExit(nums):
    """
    Similar to hash set but with more explicit early exit
    Time: O(n), Space: O(n)
    """
    if len(nums) <= 1:
        return False

    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


# Test Cases
def test_containsDuplicate():
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([99, 99], True),
        ([], False),
        ([1], False),
        ([1, 1], True),
        ([1, 2, 3, 4, 5, 1], True),
        ([-1, -1, -1], True),
        ([0, 1, 2, 3, 4], False),
    ]

    for nums, expected in test_cases:
        # Make copies since sorting modifies the array
        nums_copy1 = nums.copy()
        nums_copy2 = nums.copy()

        assert (
            containsDuplicate_HashSet(nums) == expected
        ), f"HashSet failed for {nums}"
        assert (
            containsDuplicate_Sorting(nums_copy1) == expected
        ), f"Sorting failed for {nums}"
        assert (
            containsDuplicate_SetLength(nums) == expected
        ), f"SetLength failed for {nums}"
        assert (
            containsDuplicate_Counter(nums) == expected
        ), f"Counter failed for {nums}"
        assert (
            containsDuplicate_EarlyExit(nums) == expected
        ), f"EarlyExit failed for {nums}"

        print(f"nums={nums} => {expected} ✓")


if __name__ == "__main__":
    test_containsDuplicate()
    print("\nAll tests passed!")

    # Example usage
    print(f"\nContains Duplicate Example: {containsDuplicate_HashSet([1, 2, 3, 1])}")
