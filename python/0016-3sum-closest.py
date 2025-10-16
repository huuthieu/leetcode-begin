"""
LeetCode Problem 0016: 3Sum Closest

Problem:
Given an integer array nums of length n and an integer target, find three integers
in nums such that the sum is closest to target.

Return the sum of the three integers. You may assume each input has exactly one solution.

Examples:
1. Input: nums = [-1,2,1,-4], target = 1, Output: 2 (sum -1 + 2 + 1 = 2)
2. Input: nums = [0,0,0], target = 1, Output: 0 (sum 0 + 0 + 0 = 0)
3. Input: nums = [1,1,1,0], target = -100, Output: 2

Constraints:
- 3 <= nums.length <= 500
- -1000 <= nums[i] <= 1000
- -10^4 <= target <= 10^4
"""

# Q1: Two pointer approach (optimal)
def threeSumClosest_twopointer(nums: list[int], target: int) -> int:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)

    Approach: Sort array, then use two pointers to find closest sum.
    """
    nums.sort()
    n = len(nums)
    closest_sum = float('inf')
    min_diff = float('inf')

    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            diff = abs(current_sum - target)

            if diff < min_diff:
                min_diff = diff
                closest_sum = current_sum

            if current_sum == target:
                return current_sum
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return closest_sum


# Q2: Greedy with early termination
def threeSumClosest_greedy(nums: list[int], target: int) -> int:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)

    Approach: Track closest difference and return early if sum equals target.
    """
    nums.sort()
    closest = float('inf')

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            diff = abs(total - target)

            if diff < abs(closest - target):
                closest = total

            if total == target:
                return total
            elif total < target:
                left += 1
            else:
                right -= 1

    return closest


# Q3: Using min with key function
def threeSumClosest_min(nums: list[int], target: int) -> int:
    """
    Time Complexity: O(n^3) but practical for small inputs
    Space Complexity: O(1)

    Approach: Generate all triplets and find minimum difference (less efficient).
    """
    nums.sort()
    closest = float('inf')

    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                total = nums[i] + nums[j] + nums[k]
                if abs(total - target) < abs(closest - target):
                    closest = total

    return closest


# Q4: Binary search optimization
def threeSumClosest_binary_search(nums: list[int], target: int) -> int:
    """
    Time Complexity: O(n^2 log n)
    Space Complexity: O(1)

    Approach: Use two pointers and binary search for third element.
    """
    import bisect

    nums.sort()
    closest = float('inf')
    n = len(nums)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            needed = target - nums[i] - nums[j]
            pos = bisect.bisect_left(nums, needed, j + 1, n)

            candidates = []
            if pos < n:
                candidates.append(nums[pos])
            if pos > j + 1:
                candidates.append(nums[pos - 1])

            for k_val in candidates:
                total = nums[i] + nums[j] + k_val
                if abs(total - target) < abs(closest - target):
                    closest = total

    return closest


# Q5: Optimized with bounds
def threeSumClosest_optimized(nums: list[int], target: int) -> int:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)

    Approach: Early termination with boundary checks.
    """
    nums.sort()
    n = len(nums)
    result = nums[0] + nums[1] + nums[2]

    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target:
                return target

            if abs(current_sum - target) < abs(result - target):
                result = current_sum

            if current_sum < target:
                left += 1
            else:
                right -= 1

    return result


# Q6: Recursive approach
def threeSumClosest_recursive(nums: list[int], target: int) -> int:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(n) for recursion stack

    Approach: Recursive two-pointer search.
    """
    nums.sort()
    closest = [float('inf')]

    def search(i, left, right):
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            diff = abs(current_sum - target)

            if diff < abs(closest[0] - target):
                closest[0] = current_sum

            if current_sum == target:
                return
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    for i in range(len(nums) - 2):
        search(i, i + 1, len(nums) - 1)

    return closest[0]


# Q7: Triple nested loop with optimization
def threeSumClosest_nested(nums: list[int], target: int) -> int:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)

    Approach: Use three nested loops with early termination.
    """
    nums.sort()
    closest = sum(nums[:3])

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if abs(total - target) < abs(closest - target):
                closest = total

            if total < target:
                left += 1
            else:
                right -= 1

    return closest


# Q8: Using heap for closest values
def threeSumClosest_heap(nums: list[int], target: int) -> int:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(n)

    Approach: Generate sums and track closest.
    """
    import heapq

    nums.sort()
    sums = []

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            heapq.heappush(sums, (abs(current_sum - target), current_sum))

            if current_sum == target:
                return current_sum
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return heapq.heappop(sums)[1]


# Q9: Two-pointer with distance tracking
def threeSumClosest_distance(nums: list[int], target: int) -> int:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)

    Approach: Track difference explicitly.
    """
    nums.sort()
    closest_sum = sum(nums[:3])
    min_distance = abs(closest_sum - target)

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            distance = abs(current_sum - target)

            if distance < min_distance:
                min_distance = distance
                closest_sum = current_sum

            if current_sum == target:
                return current_sum
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return closest_sum


# Q10: Clean implementation
def threeSumClosest_clean(nums: list[int], target: int) -> int:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)

    Approach: Simple and clear two-pointer implementation.
    """
    nums.sort()
    best_sum = nums[0] + nums[1] + nums[2]

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if abs(target - total) < abs(target - best_sum):
                best_sum = total

            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return total

    return best_sum


if __name__ == "__main__":
    test_cases = [
        ([-1, 2, 1, -4], 1, 2),
        ([0, 0, 0], 1, 0),
        ([1, 1, 1, 0], -100, 2),
        ([-1, -1, 1, 1, 0], 0, 0),
        ([1, 2, 3, 4], 5, 6),
        ([-100, -99, -98, 0, 1, 2, 100], 0, 0),
        ([2, 3, 4], 11, 9),
        ([1000, 1000, 1000, 1000], 1, 3000),
        ([-1000, -1000, 1000, 1000], 0, 0),
        ([0, 2, 1, -3], 0, 0),
    ]

    functions = [
        threeSumClosest_twopointer,
        threeSumClosest_greedy,
        threeSumClosest_min,
        threeSumClosest_binary_search,
        threeSumClosest_optimized,
        threeSumClosest_recursive,
        threeSumClosest_nested,
        threeSumClosest_heap,
        threeSumClosest_distance,
        threeSumClosest_clean,
    ]

    for i, func in enumerate(functions, 1):
        print(f"\nQ{i}: {func.__name__}")
        print("-" * 70)
        all_passed = True
        for nums, target, expected in test_cases:
            result = func(nums[:], target)
            passed = result == expected
            all_passed = all_passed and passed
            status = "✓" if passed else "✗"
            print(f"  {status} threeSumClosest({nums}, {target}) = {result} (expected: {expected})")

        if all_passed:
            print(f"  All tests passed!")
