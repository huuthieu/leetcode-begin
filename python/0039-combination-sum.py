"""
LeetCode Problem 0039: Combination Sum

Problem:
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers
sum to target. You may return the combinations in any order.

The same number in candidates may be chosen an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that
sum up to target is less than 150 combinations for the given input.

Examples:
1. Input: candidates = [2,3,6,7], target = 7, Output: [[2,2,3],[7]]
2. Input: candidates = [2,3,5], target = 8, Output: [[2,2,2,2],[2,3,3],[3,5]]
3. Input: candidates = [2], target = 1, Output: []

Constraints:
- 1 <= candidates.length <= 30
- 2 <= candidates[i] <= 40
- All elements of candidates are distinct
- 1 <= target <= 40
"""


# Q1: Backtracking with recursive approach
def combinationSum_backtracking(candidates: list[int], target: int) -> list[list[int]]:
    """
    Time Complexity: O(N^(T/M)) where N is the number of candidates, T is the target, M is the min value
    Space Complexity: O(T/M) for recursion depth

    Approach: Use backtracking to explore all possible combinations. Since we can reuse numbers,
    we don't move the index forward after including a number.
    """
    result = []

    def backtrack(remaining, combination, start):
        # Base case: found a valid combination
        if remaining == 0:
            result.append(combination[:])
            return

        # Base case: remaining is negative
        if remaining < 0:
            return

        # Try each candidate starting from 'start'
        for i in range(start, len(candidates)):
            # Choose
            combination.append(candidates[i])

            # Explore with the same index (can reuse)
            backtrack(remaining - candidates[i], combination, i)

            # Unchoose
            combination.pop()

    backtrack(target, [], 0)
    return result


# Q2: Backtracking with in-place tracking
def combinationSum_inplace(candidates: list[int], target: int) -> list[list[int]]:
    """
    Time Complexity: O(N^(T/M))
    Space Complexity: O(T/M) for recursion depth

    Approach: Similar to Q1 but with slightly different implementation.
    """
    result = []

    def dfs(path, target, start):
        if target == 0:
            result.append(path)
            return

        if target < 0:
            return

        for i in range(start, len(candidates)):
            dfs(path + [candidates[i]], target - candidates[i], i)

    dfs([], target, 0)
    return result


# Q3: Sorted candidates optimization
def combinationSum_sorted(candidates: list[int], target: int) -> list[list[int]]:
    """
    Time Complexity: O(N^(T/M))
    Space Complexity: O(T/M) for recursion depth

    Approach: Sort candidates first to enable early termination.
    """
    candidates.sort()
    result = []

    def backtrack(remaining, combination, start):
        if remaining == 0:
            result.append(combination[:])
            return

        for i in range(start, len(candidates)):
            # Early termination: if candidate > remaining, no point checking further
            if candidates[i] > remaining:
                break

            combination.append(candidates[i])
            backtrack(remaining - candidates[i], combination, i)
            combination.pop()

    backtrack(target, [], 0)
    return result


# Q4: Iterative approach with queue
def combinationSum_iterative(candidates: list[int], target: int) -> list[list[int]]:
    """
    Time Complexity: O(N^(T/M))
    Space Complexity: O(N^(T/M)) for queue

    Approach: Use iterative approach with queue instead of recursion.
    """
    result = []
    queue = [(target, [], 0)]

    while queue:
        remaining, combination, start = queue.pop(0)

        if remaining == 0:
            result.append(combination)
            continue

        for i in range(start, len(candidates)):
            if candidates[i] <= remaining:
                queue.append((remaining - candidates[i], combination + [candidates[i]], i))

    return result


# Q5: DP with memoization
def combinationSum_dp(candidates: list[int], target: int) -> list[list[int]]:
    """
    Time Complexity: O(N^(T/M))
    Space Complexity: O(T) for memo + O(T/M) for recursion

    Approach: Use dynamic programming with memoization to cache results.
    """
    memo = {}

    def dp(remaining, start):
        if remaining == 0:
            return [[]]

        if remaining < 0:
            return []

        if (remaining, start) in memo:
            return memo[(remaining, start)]

        result = []

        for i in range(start, len(candidates)):
            if candidates[i] <= remaining:
                for sub_combination in dp(remaining - candidates[i], i):
                    result.append([candidates[i]] + sub_combination)

        memo[(remaining, start)] = result
        return result

    return dp(target, 0)


# Q6: Bottom-up DP
def combinationSum_bottom_up(candidates: list[int], target: int) -> list[list[int]]:
    """
    Time Complexity: O(target * N * L) where L is average length of combinations
    Space Complexity: O(target)

    Approach: Use bottom-up DP building from smaller targets.
    """
    dp = [[] for _ in range(target + 1)]
    dp[0] = [[]]

    for amount in range(1, target + 1):
        for candidate in candidates:
            if candidate <= amount:
                for combination in dp[amount - candidate]:
                    dp[amount].append(combination + [candidate])

    return dp[target]


# Q7: Generator-based approach
def combinationSum_generator(candidates: list[int], target: int) -> list[list[int]]:
    """
    Time Complexity: O(N^(T/M))
    Space Complexity: O(T/M) for recursion

    Approach: Use generator to yield combinations.
    """
    def generate(remaining, start):
        if remaining == 0:
            yield []
            return

        for i in range(start, len(candidates)):
            if candidates[i] <= remaining:
                for combination in generate(remaining - candidates[i], i):
                    yield [candidates[i]] + combination

    return list(generate(target, 0))


# Q8: Early termination with pruning
def combinationSum_pruning(candidates: list[int], target: int) -> list[list[int]]:
    """
    Time Complexity: O(N^(T/M))
    Space Complexity: O(T/M) for recursion

    Approach: Aggressive pruning of branches that can't lead to solution.
    """
    candidates.sort()
    result = []

    def backtrack(remaining, combination, start):
        if remaining == 0:
            result.append(combination[:])
            return

        if remaining < 0 or start >= len(candidates):
            return

        # Try including the current candidate multiple times
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break

            combination.append(candidates[i])
            backtrack(remaining - candidates[i], combination, i)
            combination.pop()

    backtrack(target, [], 0)
    return result


# Q9: With distinct tracking
def combinationSum_distinct(candidates: list[int], target: int) -> list[list[int]]:
    """
    Time Complexity: O(N^(T/M))
    Space Complexity: O(T/M) for recursion

    Approach: Track seen combinations to avoid duplicates.
    """
    result = []
    seen = set()

    def backtrack(remaining, combination, start):
        if remaining == 0:
            combo_tuple = tuple(sorted(combination))
            if combo_tuple not in seen:
                seen.add(combo_tuple)
                result.append(combination[:])
            return

        for i in range(start, len(candidates)):
            combination.append(candidates[i])
            backtrack(remaining - candidates[i], combination, i)
            combination.pop()

    backtrack(target, [], 0)
    return result


# Q10: Compact backtracking
def combinationSum_compact(candidates: list[int], target: int) -> list[list[int]]:
    """
    Time Complexity: O(N^(T/M))
    Space Complexity: O(T/M) for recursion

    Approach: Most compact implementation of backtracking.
    """
    result = []

    def backtrack(target, path, start):
        if target == 0:
            result.append(path)
        else:
            for i in range(start, len(candidates)):
                if candidates[i] <= target:
                    backtrack(target - candidates[i], path + [candidates[i]], i)

    backtrack(target, [], 0)
    return result


if __name__ == "__main__":
    test_cases = [
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ([2], 1, []),
        ([2, 3, 6, 7], 2, [[2]]),
        ([2, 3, 6, 7], 3, [[3]]),
        ([2, 3, 6, 7], 6, [[2, 2, 2], [3, 3], [6]]),
        ([1], 1, [[1]]),
        ([1, 2, 3], 5, [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 3], [1, 2, 2], [2, 3]]),
    ]

    functions = [
        combinationSum_backtracking,
        combinationSum_inplace,
        combinationSum_sorted,
        combinationSum_iterative,
        combinationSum_dp,
        combinationSum_bottom_up,
        combinationSum_generator,
        combinationSum_pruning,
        combinationSum_distinct,
        combinationSum_compact,
    ]

    for i, func in enumerate(functions, 1):
        print(f"\nQ{i}: {func.__name__}")
        print("-" * 70)
        all_passed = True
        for candidates, target, expected in test_cases:
            result = func(candidates[:], target)
            # Sort both for comparison since order doesn't matter
            result_sorted = sorted([sorted(r) for r in result])
            expected_sorted = sorted([sorted(e) for e in expected])
            passed = result_sorted == expected_sorted
            all_passed = all_passed and passed
            status = "✓" if passed else "✗"
            print(f"  {status} combinationSum({candidates}, {target})")
            if not passed:
                print(f"      Expected: {expected_sorted}")
                print(f"      Got: {result_sorted}")

        if all_passed:
            print(f"  All tests passed!")
