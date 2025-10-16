"""
LeetCode Problem 0018: 4Sum

Problem:
Given an array nums of n integers and an integer target, return all unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:
- 0 <= a, b, c, d < n
- a, b, c, d are distinct
- nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the quadruplets in any order.

Examples:
1. Input: nums = [1,0,-1,0,-2,2], target = 0
   Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

2. Input: nums = [1000000000,1000000000,1000000000,1000000000], target = -294967296
   Output: []

Constraints:
- 1 <= nums.length <= 200
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
"""

# Q1: Sorting + Two pointer approach (similar to 3Sum but with 4 elements)
def fourSum_twopointer(nums: list[int], target: int) -> list[list[int]]:
    """
    Time Complexity: O(n^3)
    Space Complexity: O(1)

    Approach: Sort array, then use nested loop with two pointers.
    """
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 3):
        # Skip duplicate values
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Optimization: if smallest possible sum is too large
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            break

        # Optimization: if largest possible sum is too small
        if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                break

            if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                continue

            left, right = j + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if current_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

    return result


# Q2: Hashset based approach
def fourSum_hashset(nums: list[int], target: int) -> list[list[int]]:
    """
    Time Complexity: O(n^3)
    Space Complexity: O(n)

    Approach: For each pair, use hash set to find complementary pairs.
    """
    nums.sort()
    result_set = set()
    n = len(nums)

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            seen = set()
            for k in range(j + 1, n):
                complement = target - nums[i] - nums[j] - nums[k]
                if complement in seen:
                    quad = tuple(sorted([nums[i], nums[j], complement, nums[k]]))
                    result_set.add(quad)
                seen.add(nums[k])

    return [list(q) for q in result_set]


# Q3: Reduce to 3Sum using nested loops
def fourSum_reduce_3sum(nums: list[int], target: int) -> list[list[int]]:
    """
    Time Complexity: O(n^3)
    Space Complexity: O(1)

    Approach: Reduce 4Sum to 3Sum problem.
    """
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Early termination optimizations
        if nums[i] * 4 > target:
            break

        if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            target_2sum = target - nums[i] - nums[j]
            left, right = j + 1, n - 1

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == target_2sum:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum < target_2sum:
                    left += 1
                else:
                    right -= 1

    return result


# Q4: Using set for deduplication
def fourSum_set_dedup(nums: list[int], target: int) -> list[list[int]]:
    """
    Time Complexity: O(n^3)
    Space Complexity: O(n)

    Approach: Use set to handle duplicate results.
    """
    nums.sort()
    result_set = set()

    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            left, right = j + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if current_sum == target:
                    result_set.add((nums[i], nums[j], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

    return [list(q) for q in result_set]


# Q5: Recursive approach (N-sum generalization)
def fourSum_recursive(nums: list[int], target: int) -> list[list[int]]:
    """
    Time Complexity: O(n^3)
    Space Complexity: O(n)

    Approach: Recursive solution for generalized N-sum problem.
    """
    nums.sort()
    result = []

    def n_sum(nums, n, target, start, current):
        if n == 2:
            left, right = start, len(nums) - 1
            while left < right:
                total = nums[left] + nums[right]
                if total == target:
                    result.append(current + [nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
            return

        for i in range(start, len(nums) - n + 1):
            if i > start and nums[i] == nums[i - 1]:
                continue
            n_sum(nums, n - 1, target - nums[i], i + 1, current + [nums[i]])

    n_sum(nums, 4, target, 0, [])
    return result


# Q6: Dictionary-based memoization
def fourSum_memo(nums: list[int], target: int) -> list[list[int]]:
    """
    Time Complexity: O(n^3)
    Space Complexity: O(n)

    Approach: Use dictionary for storing intermediate results.
    """
    nums.sort()
    result = []
    n = len(nums)
    memo = {}

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        key = (i, target)
        if key in memo:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            target_2sum = target - nums[i] - nums[j]
            left, right = j + 1, n - 1

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == target_2sum:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum < target_2sum:
                    left += 1
                else:
                    right -= 1

        memo[key] = True

    return result


# Q7: Using combinations from itertools
def fourSum_combinations(nums: list[int], target: int) -> list[list[int]]:
    """
    Time Complexity: O(n^4) but with early termination
    Space Complexity: O(1)

    Approach: Generate combinations and check sums (less efficient).
    """
    from itertools import combinations

    nums.sort()
    result_set = set()

    for combo in combinations(range(len(nums)), 4):
        if sum(nums[i] for i in combo) == target:
            result_set.add(tuple(nums[i] for i in combo))

    return [list(q) for q in result_set]


# Q8: Optimized with bounds checking
def fourSum_bounds(nums: list[int], target: int) -> list[list[int]]:
    """
    Time Complexity: O(n^3)
    Space Complexity: O(1)

    Approach: Aggressive bounds checking for early termination.
    """
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 3):
        if nums[i] * 4 > target:
            break
        if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
            continue

        for j in range(i + 1, n - 2):
            if nums[i] + nums[j] * 3 > target:
                break
            if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                continue

            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

    return result


# Q9: Generator approach
def fourSum_generator(nums: list[int], target: int) -> list[list[int]]:
    """
    Time Complexity: O(n^3)
    Space Complexity: O(n)

    Approach: Use generators for lazy evaluation.
    """
    nums.sort()
    result_set = set()
    n = len(nums)

    def generate_quads():
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        yield (nums[i], nums[j], nums[left], nums[right])
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

    for quad in generate_quads():
        result_set.add(quad)

    return [list(q) for q in result_set]


# Q10: Clean implementation
def fourSum_clean(nums: list[int], target: int) -> list[list[int]]:
    """
    Time Complexity: O(n^3)
    Space Complexity: O(1)

    Approach: Simple and clean implementation.
    """
    nums.sort()
    result = []

    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left, right = j + 1, len(nums) - 1
            target_2sum = target - nums[i] - nums[j]

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == target_2sum:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum < target_2sum:
                    left += 1
                else:
                    right -= 1

    return result


if __name__ == "__main__":
    test_cases = [
        ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
        ([1000000000, 1000000000, 1000000000, 1000000000], -294967296, []),
        ([0, 0, 0, 0], 0, [[0, 0, 0, 0]]),
        ([1, 1, 1, 1], 4, [[1, 1, 1, 1]]),
        ([-3, -2, -1, 0, 1, 2, 3], 0, [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
    ]

    functions = [
        fourSum_twopointer,
        fourSum_hashset,
        fourSum_reduce_3sum,
        fourSum_set_dedup,
        fourSum_recursive,
        fourSum_memo,
        fourSum_combinations,
        fourSum_bounds,
        fourSum_generator,
        fourSum_clean,
    ]

    for i, func in enumerate(functions, 1):
        print(f"\nQ{i}: {func.__name__}")
        print("-" * 70)
        all_passed = True
        for nums, target, expected in test_cases:
            result = func(nums[:], target)
            result.sort()
            expected.sort()
            passed = result == expected
            all_passed = all_passed and passed
            status = "✓" if passed else "✗"
            print(f"  {status} fourSum({nums}, {target}) = {result}")

        if all_passed:
            print(f"  All tests passed!")
