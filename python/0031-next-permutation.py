"""
LeetCode 31: Next Permutation

Problem:
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

- For example, for arr = [1,2,3], the following are all the permutations of arr:
  [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
More formally, if all the permutations of the array are sorted in one container according to their
lexicographical order, then the next permutation of that array is the permutation that follows it in the
sorted container.

If such an arrangement is not possible, the array must be rearranged as the lowest possible order
(i.e., sorted in ascending order).

- For example, the next permutation of arr = [1,2,3] is [1,3,2].
- Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
- While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a
  lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 100

Time Complexity: O(n)
Space Complexity: O(1)
"""


# Approach 1: Single Pass with Three Steps - OPTIMAL
def nextPermutation(nums):
    """
    Algorithm (from right to left):
    1. Find the first decreasing element (pivot)
    2. Find the smallest element larger than pivot to its right
    3. Swap them, then reverse everything after pivot position

    Visual Example: [1, 3, 5, 4, 2]
    Step 1: Find pivot (first decrease from right)
           [1, 3, 5, 4, 2]
                ^  (3 < 5, so pivot = 3 at index 1)

    Step 2: Find smallest element > pivot from right
           [1, 3, 5, 4, 2]
                ^     ^  (4 > 3, so swap target = 4)

    Step 3: Swap pivot with target
           [1, 4, 5, 3, 2]

    Step 4: Reverse everything after pivot position
           [1, 4, 2, 3, 5]  ← This is the next permutation!

    Time: O(n) - Each step is O(n) at most
    Space: O(1) - In-place modifications only

    Why this works:
    - The pivot is where the sequence stops being descending from right
    - Everything to the right of pivot is in descending order
    - We need the smallest increase, so we find the smallest element > pivot
    - After swapping, we reverse to get the smallest permutation of that suffix
    """
    n = len(nums)

    # Step 1: Find the pivot (first element that breaks descending order from right)
    pivot = -1
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            pivot = i
            break

    # If no pivot found, array is in descending order (largest permutation)
    # Reverse entire array to get smallest permutation
    if pivot == -1:
        nums.reverse()
        return

    # Step 2: Find the smallest element larger than nums[pivot] from the right
    # (It will be the rightmost element greater than pivot due to descending order)
    for i in range(n - 1, pivot, -1):
        if nums[i] > nums[pivot]:
            # Step 3: Swap
            nums[i], nums[pivot] = nums[pivot], nums[i]
            break

    # Step 4: Reverse the suffix after pivot to get the smallest permutation
    # The suffix is still in descending order, so reversing gives ascending
    nums[pivot + 1:] = reversed(nums[pivot + 1:])


# Approach 2: Verbose Step-by-Step (for learning)
def nextPermutation_verbose(nums):
    """
    Same algorithm but with explicit helper functions and detailed steps
    Useful for understanding the logic

    Time: O(n)
    Space: O(1)
    """
    def find_pivot(arr):
        """Find the first position from right where arr[i] < arr[i+1]"""
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                return i
        return -1

    def find_swap_target(arr, pivot):
        """Find the smallest element > arr[pivot] from the right"""
        for i in range(len(arr) - 1, pivot, -1):
            if arr[i] > arr[pivot]:
                return i
        return -1

    def reverse_suffix(arr, start):
        """Reverse array from start to end"""
        left, right = start, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    # Execute the algorithm
    pivot = find_pivot(nums)

    if pivot == -1:
        # Already largest permutation, return smallest
        nums.reverse()
        return

    swap_target = find_swap_target(nums, pivot)
    nums[pivot], nums[swap_target] = nums[swap_target], nums[pivot]
    reverse_suffix(nums, pivot + 1)


# Approach 3: Two-Pointer Reverse (alternative implementation)
def nextPermutation_two_pointer(nums):
    """
    Same algorithm but uses two pointers for reversal

    Time: O(n)
    Space: O(1)
    """
    n = len(nums)

    # Find pivot
    pivot = -1
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            pivot = i
            break

    if pivot == -1:
        # Reverse entire array using two pointers
        left, right = 0, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return

    # Find swap target
    for i in range(n - 1, pivot, -1):
        if nums[i] > nums[pivot]:
            nums[i], nums[pivot] = nums[pivot], nums[i]
            break

    # Reverse suffix using two pointers
    left, right = pivot + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


# Helper function for testing
def get_all_permutations(nums):
    """
    Generate all permutations of nums (for verification)
    Not efficient, just for testing small inputs
    """
    from itertools import permutations
    return sorted(set(permutations(nums)))


# Test Cases
def test_next_permutation():
    print("Testing Next Permutation:\n")

    test_cases = [
        # (input, expected, description)
        ([1, 2, 3], [1, 3, 2], "Simple ascending"),
        ([3, 2, 1], [1, 2, 3], "Descending - wrap to smallest"),
        ([1, 1, 5], [1, 5, 1], "With duplicates"),
        ([1], [1], "Single element"),
        ([1, 3, 2], [2, 1, 3], "Middle permutation"),
        ([2, 3, 1], [3, 1, 2], "Another middle permutation"),
        ([1, 5, 8, 4, 7, 6, 5, 3, 1], [1, 5, 8, 5, 1, 3, 4, 6, 7], "Complex case"),
        ([4, 2, 0, 2, 3, 2, 0], [4, 2, 0, 3, 0, 2, 2], "With zeros and duplicates"),
        ([2, 3, 1, 3, 3], [2, 3, 3, 1, 3], "Multiple same elements"),
        ([1, 3, 5, 4, 2], [1, 4, 2, 3, 5], "Example from docstring"),
    ]

    for i, (nums_input, expected, description) in enumerate(test_cases):
        # Test main implementation
        nums1 = nums_input.copy()
        nextPermutation(nums1)
        assert nums1 == expected, f"Test {i+1} failed: {description}"

        # Test verbose implementation
        nums2 = nums_input.copy()
        nextPermutation_verbose(nums2)
        assert nums2 == expected, f"Verbose test {i+1} failed: {description}"

        # Test two-pointer implementation
        nums3 = nums_input.copy()
        nextPermutation_two_pointer(nums3)
        assert nums3 == expected, f"Two-pointer test {i+1} failed: {description}"

        print(f"[PASS] {description}")
        print(f"  Input: {nums_input}")
        print(f"  Output: {nums1}")
        print(f"  Expected: {expected}\n")


def test_complete_permutation_cycle():
    """
    Test that repeatedly calling nextPermutation cycles through all permutations
    """
    print("Testing Complete Permutation Cycle:\n")

    nums = [1, 2, 3]
    all_perms = []

    # Generate all permutations by repeatedly calling nextPermutation
    for _ in range(6):  # 3! = 6 permutations
        all_perms.append(nums.copy())
        nextPermutation(nums)

    expected_perms = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]

    assert all_perms == expected_perms, "Permutation cycle failed"
    print("[PASS] Complete cycle through all permutations of [1,2,3]")
    for i, perm in enumerate(all_perms):
        print(f"  Step {i+1}: {perm}")

    # Verify it wraps back to the beginning
    assert nums == [1, 2, 3], "Should wrap back to smallest permutation"
    print(f"  Step 7: {nums} (wrapped back to start)\n")


def test_edge_cases():
    """Test edge cases"""
    print("Testing Edge Cases:\n")

    # All same elements
    nums = [1, 1, 1]
    nextPermutation(nums)
    assert nums == [1, 1, 1], "All same elements failed"
    print("[PASS] All same elements: [1,1,1] -> [1,1,1]")

    # Two elements ascending
    nums = [1, 2]
    nextPermutation(nums)
    assert nums == [2, 1], "Two elements ascending failed"
    print("[PASS] Two elements ascending: [1,2] -> [2,1]")

    # Two elements descending
    nums = [2, 1]
    nextPermutation(nums)
    assert nums == [1, 2], "Two elements descending failed"
    print("[PASS] Two elements descending: [2,1] -> [1,2]")

    # Large descending (wraps to ascending)
    nums = [5, 4, 3, 2, 1]
    nextPermutation(nums)
    assert nums == [1, 2, 3, 4, 5], "Large descending failed"
    print("[PASS] Large descending: [5,4,3,2,1] -> [1,2,3,4,5]")

    print()


# Practice Questions
def practice_questions():
    """
    Q1: Why do we search from right to left?
    A1: We want the NEXT permutation (smallest increase). Changes on the right
        affect lexicographical order less than changes on the left. By finding
        the rightmost pivot, we ensure the minimal change needed.

    Q2: Why is everything after the pivot in descending order?
    A2: By definition of the pivot! The pivot is where the sequence stops being
        descending from the right. Everything after it must be descending,
        otherwise we would have found a pivot further right.

    Q3: Why do we reverse the suffix after swapping?
    A3: After the swap, the suffix is still in descending order (largest permutation).
        We want the next smallest, so we reverse it to get ascending order.

    Q4: What if there are duplicate elements?
    A4: The algorithm still works! When finding the swap target, we find the
        rightmost element > pivot, which handles duplicates correctly.

    Q5: Can we modify this to find the previous permutation?
    A5: Yes! Just reverse the logic:
        - Find first increasing element from right (instead of decreasing)
        - Find largest element smaller than pivot
        - Swap and reverse suffix

    Q6: What's the time complexity in best and worst cases?
    A6: Best: O(n) - need to scan to find pivot
        Worst: O(n) - scan + swap + reverse, all O(n)
        So it's always O(n)

    Q7: How many next permutations until we cycle back?
    A7: For n distinct elements, there are n! permutations. So we'd need
        to call nextPermutation n! times to cycle back to the start.

    Q8: What are real-world applications?
    A8: - Generating test cases (try all input combinations)
        - Combinatorial optimization (traveling salesman)
        - Password cracking (systematic permutation testing)
        - Generating unique arrangements (seating, scheduling)

    Q9: Why is this better than generating all permutations?
    A9: Space efficient (O(1) vs O(n!)), can stop anytime, and generates
        permutations in lexicographical order on-demand.

    Q10: How does this relate to counting sort or bucket sort?
    A10: The key insight is recognizing when a sequence is in descending order
         (maximum permutation). This is similar to recognizing when an array
         is sorted, which is fundamental to many sorting algorithms.

    Q11: Can we find the kth next permutation efficiently?
    A11: For small k, just call nextPermutation k times (O(kn)).
         For large k, use the factorial number system to compute directly.
         See LeetCode 60: Permutation Sequence.

    Q12: What if we want to generate permutations in different orders?
    A12: This algorithm gives lexicographical order. For other orders:
         - Random: use Fisher-Yates shuffle
         - Specific pattern: use backtracking with custom comparison
         - Reverse lexicographical: use previous permutation algorithm
    """
    pass


# Follow-up Problems
def follow_up_problems():
    """
    Related LeetCode Problems:

    1. LeetCode 46: Permutations
       Generate all permutations of distinct integers using backtracking

    2. LeetCode 47: Permutations II
       Generate all unique permutations when there are duplicates

    3. LeetCode 60: Permutation Sequence
       Find the kth permutation sequence directly without generating all

    4. LeetCode 567: Permutation in String
       Check if one string is a permutation of another's substring

    5. LeetCode 784: Letter Case Permutation
       Generate all permutations by changing letter case

    6. Previous Permutation
       Implement the reverse: find the previous lexicographical permutation
       Algorithm: Reverse the logic of next permutation

    7. kth Next Permutation
       Find the permutation after k next permutations
       Solution: Call nextPermutation k times, or use factorial number system

    8. Count Permutations Between Two Arrays
       Given two permutations, count how many next permutations to go from A to B
       Solution: Convert permutations to factorial representation and subtract
    """
    pass


if __name__ == "__main__":
    test_next_permutation()
    print("="*50)
    test_complete_permutation_cycle()
    print("="*50)
    test_edge_cases()
    print("="*50)
    print("All tests passed!")
    print("="*50)

    # Uncomment to see practice questions
    # help(practice_questions)
    # help(follow_up_problems)
