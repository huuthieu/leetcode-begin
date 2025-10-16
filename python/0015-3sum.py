"""
LeetCode Problem 0015: 3Sum

Problem:
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets, and you may return
the solution set in any order.

Examples:
1. Input: nums = [-1,0,1,2,-1,-4], Output: [[-1,-1,2],[-1,0,1]]
2. Input: nums = [0], Output: []
3. Input: nums = [-2,0,1,1,2], Output: [[-2,0,2],[-2,1,1]]

Constraints:
- 0 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
"""

# Q1: Sorting + Two Pointer (most efficient)
def threeSum_sorting(nums: list[int]) -> list[list[int]]:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1) or O(n) depending on sorting algorithm

    Approach: Sort array, then for each element, use two pointers to find pairs
    that sum to the negative of current element.
    """
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        # Skip duplicate values
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # If smallest possible sum is positive, break
        if nums[i] + nums[i + 1] + nums[i + 2] > 0:
            break

        # If largest possible sum is negative, continue
        if nums[i] + nums[n - 2] + nums[n - 1] < 0:
            continue

        target = -nums[i]
        left, right = i + 1, n - 1

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
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


# Q2: Hash set based approach
def threeSum_hashset(nums: list[int]) -> list[list[int]]:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(n)

    Approach: For each pair, use hash set to check if complement exists.
    """
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        if nums[i] > 0:
            break

        seen = set()
        for j in range(i + 1, n):
            complement = -nums[i] - nums[j]
            if complement in seen:
                result.append([nums[i], complement, nums[j]])
                while j + 1 < n and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])

    return result


# Q3: Two pointer with no sorting optimization
def threeSum_two_pointer(nums: list[int]) -> list[list[int]]:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)

    Approach: Similar to Q1 but with different implementation style.
    """
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        target = -nums[i]

        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left + 1] == nums[left]:
                    left += 1
                while left < right and nums[right - 1] == nums[right]:
                    right -= 1

                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1

    return result


# Q4: Dictionary-based approach
def threeSum_dict(nums: list[int]) -> list[list[int]]:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(n)

    Approach: Build a dictionary and use it for lookups.
    """
    nums.sort()
    result = []
    seen = set()

    for i in range(len(nums) - 2):
        if nums[i] in seen:
            continue
        seen.add(nums[i])

        pairs = {}
        for j in range(i + 1, len(nums)):
            complement = -nums[i] - nums[j]
            if complement in pairs:
                triplet = tuple(sorted([nums[i], complement, nums[j]]))
                result.append(list(triplet))
            pairs[nums[j]] = j

    return result


# Q5: Using set for triplet deduplication
def threeSum_set_dedup(nums: list[int]) -> list[list[int]]:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(n)

    Approach: Use set to automatically handle duplicates in results.
    """
    nums.sort()
    result_set = set()

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result_set.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return [list(t) for t in result_set]


# Q6: Recursive approach (less efficient)
def threeSum_recursive(nums: list[int]) -> list[list[int]]:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(n) for recursion

    Approach: Recursively reduce to 2Sum problem.
    """
    nums.sort()
    result = []

    def n_sum(nums, n, target, start=0, current=[]):
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

    n_sum(nums, 3, 0)
    return result


# Q7: Generator-based approach
def threeSum_generator(nums: list[int]) -> list[list[int]]:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(n)

    Approach: Use generator for lazy evaluation.
    """
    nums.sort()
    result = []
    seen = set()

    def generate_triplets():
        for i in range(len(nums) - 2):
            if nums[i] in seen:
                continue
            seen.add(nums[i])

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    yield (nums[i], nums[left], nums[right])
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

    return [list(t) for t in generate_triplets()]


# Q8: Counting sort optimization
def threeSum_counting(nums: list[int]) -> list[list[int]]:
    """
    Time Complexity: O(n^2 + k) where k is range of numbers
    Space Complexity: O(k)

    Approach: Use counting for better performance on small range inputs.
    """
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i]
        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result


# Q9: Using bisect for sorted operations
def threeSum_bisect(nums: list[int]) -> list[list[int]]:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)

    Approach: Standard two-pointer after sorting.
    """
    import bisect

    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i]
        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1

    return result


# Q10: Index-based approach
def threeSum_index(nums: list[int]) -> list[list[int]]:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)

    Approach: Track indices instead of values for deduplication.
    """
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates
                while left + 1 < right and nums[left] == nums[left + 1]:
                    left += 1
                while right - 1 > left and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


if __name__ == "__main__":
    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0], []),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([-1, -1, -1, 2], []),
        ([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6], [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2], [0, 0, 0]]),
    ]

    functions = [
        threeSum_sorting,
        threeSum_hashset,
        threeSum_two_pointer,
        threeSum_dict,
        threeSum_set_dedup,
        threeSum_recursive,
        threeSum_generator,
        threeSum_counting,
        threeSum_bisect,
        threeSum_index,
    ]

    for i, func in enumerate(functions, 1):
        print(f"\nQ{i}: {func.__name__}")
        print("-" * 70)
        all_passed = True
        for nums, expected in test_cases:
            result = func(nums[:])
            result.sort()
            expected.sort()
            passed = result == expected
            all_passed = all_passed and passed
            status = "✓" if passed else "✗"
            print(f"  {status} threeSum({nums}) = {result}")
            if not passed:
                print(f"      Expected: {expected}")

        if all_passed:
            print(f"  All tests passed!")
