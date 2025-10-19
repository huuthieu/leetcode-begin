"""
LeetCode Problem 0022: Generate Parentheses

Problem:
Given n pairs of parentheses, write a function to generate all combinations
of well-formed parentheses.

Examples:
1. Input: n = 3, Output: ["((()))","(()())","(())()","()(())","()()()"]
2. Input: n = 1, Output: ["()"]
3. Input: n = 0, Output: [""]

Constraints:
- 1 <= n <= 8
"""

from typing import List


# Q1: Backtracking approach (optimal)
def generateParenthesis_backtrack(n: int) -> List[str]:
    """
    Time Complexity: O(4^n / sqrt(n))
    Space Complexity: O(n)

    Approach: Use backtracking to build valid parentheses combinations.
    At each step, add '(' if we haven't used all opens, add ')' if closes < opens.
    """
    result = []

    def backtrack(current, opens, closes):
        if len(current) == 2 * n:
            result.append(current)
            return

        if opens < n:
            backtrack(current + "(", opens + 1, closes)

        if closes < opens:
            backtrack(current + ")", opens, closes + 1)

    backtrack("", 0, 0)
    return result


# Q2: Dynamic programming approach
def generateParenthesis_dp(n: int) -> List[str]:
    """
    Time Complexity: O(4^n / sqrt(n))
    Space Complexity: O(n)

    Approach: Build up from smaller subproblems.
    For each i, combine valid sequences of length 2*i-2.
    """
    if n == 0:
        return [""]

    dp = [[] for _ in range(n + 1)]
    dp[0] = [""]

    for i in range(1, n + 1):
        for j in range(i):
            for left in dp[j]:
                for right in dp[i - 1 - j]:
                    dp[i].append("(" + left + ")" + right)

    return dp[n]


# Q3: Backtracking with pruning
def generateParenthesis_prune(n: int) -> List[str]:
    """
    Time Complexity: O(4^n / sqrt(n))
    Space Complexity: O(n)

    Approach: Backtracking with early pruning of invalid states.
    """
    result = []

    def backtrack(current, open_count, close_count):
        if open_count > n or close_count > open_count:
            return

        if open_count == n and close_count == n:
            result.append(current)
            return

        backtrack(current + "(", open_count + 1, close_count)
        backtrack(current + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return result


# Q4: Stack-based approach
def generateParenthesis_stack(n: int) -> List[str]:
    """
    Time Complexity: O(4^n / sqrt(n))
    Space Complexity: O(n)

    Approach: Use a stack to track state (current string, open count, close count).
    """
    result = []
    stack = [("", 0, 0)]

    while stack:
        current, opens, closes = stack.pop()

        if opens == n and closes == n:
            result.append(current)
            continue

        if opens < n:
            stack.append((current + "(", opens + 1, closes))

        if closes < opens:
            stack.append((current + ")", opens, closes + 1))

    return result


# Q5: Recursive with list append
def generateParenthesis_recursive(n: int) -> List[str]:
    """
    Time Complexity: O(4^n / sqrt(n))
    Space Complexity: O(n)

    Approach: Pure recursive approach building result.
    """
    def helper(opens, closes):
        if opens == 0 and closes == 0:
            return [""]

        result = []

        if opens > 0:
            for seq in helper(opens - 1, closes):
                result.append("(" + seq)

        if closes > opens:
            for seq in helper(opens, closes - 1):
                result.append(")" + seq)

        return result

    return helper(n, n)


if __name__ == "__main__":
    test_cases = [
        (1, ["()"]),
        (2, ["(())", "()()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    ]

    functions = [
        generateParenthesis_backtrack,
        generateParenthesis_dp,
        generateParenthesis_prune,
        generateParenthesis_stack,
        generateParenthesis_recursive,
    ]

    for i, func in enumerate(functions, 1):
        print(f"\nQ{i}: {func.__name__}")
        print("-" * 70)
        all_passed = True
        for n, expected in test_cases:
            result = sorted(func(n))
            expected_sorted = sorted(expected)
            passed = result == expected_sorted
            all_passed = all_passed and passed
            status = "✓" if passed else "✗"
            print(f"  {status} generateParenthesis({n}) = {result}")

        if all_passed:
            print(f"  All tests passed!")
