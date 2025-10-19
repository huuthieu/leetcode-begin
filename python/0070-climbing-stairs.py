"""
LeetCode 70: Climbing Stairs

Problem:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example:
n = 2 => 2 ways (1+1, 2)
n = 3 => 3 ways (1+1+1, 1+2, 2+1)
n = 4 => 5 ways (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2)
n = 5 => 8 ways

Time Complexity: O(n)
Space Complexity: O(n) - with memoization or O(1) - optimized with two variables
"""


# Approach 1: Dynamic Programming - Tabulation
def climbStairs_DP(n: int) -> int:
    """
    Classic DP approach: dp[i] = dp[i-1] + dp[i-2]
    Why? To reach step i, you can come from step i-1 (1 step) or step i-2 (2 steps)
    """
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Approach 2: Space-Optimized DP
def climbStairs_Optimized(n: int) -> int:
    """
    We only need the last two values, so we can use O(1) space
    """
    if n <= 2:
        return n

    prev2, prev1 = 1, 2

    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1


# Approach 3: Memoization (Top-Down DP)
def climbStairs_Memo(n: int) -> int:
    memo = {}

    def dp(n):
        if n <= 2:
            return n
        if n in memo:
            return memo[n]

        memo[n] = dp(n - 1) + dp(n - 2)
        return memo[n]

    return dp(n)


# Approach 4: Fibonacci Pattern (Mathematical)
def climbStairs_Fibonacci(n: int) -> int:
    """
    This is actually Fibonacci sequence!
    f(1) = 1, f(2) = 2, f(3) = 3, f(4) = 5, f(5) = 8...
    Can be solved using matrix exponentiation for very large n
    """
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
    return a


# Test Cases
def test_climbStairs():
    test_cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (6, 13),
        (10, 89),
    ]

    for n, expected in test_cases:
        assert climbStairs_DP(n) == expected, f"DP failed for n={n}"
        assert climbStairs_Optimized(n) == expected, f"Optimized failed for n={n}"
        assert climbStairs_Memo(n) == expected, f"Memo failed for n={n}"
        assert climbStairs_Fibonacci(n) == expected, f"Fibonacci failed for n={n}"
        print(f"n={n}: {expected} ways ✓")


if __name__ == "__main__":
    test_climbStairs()
    print("\nAll tests passed!")

    # Example usage
    print(f"\nFor n=45: {climbStairs_Optimized(45)} ways")
