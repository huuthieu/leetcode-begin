"""
LeetCode 322: Coin Change

Problem:
You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example:
coins = [1,2,5], amount = 5 => 1 (5 = 5)
coins = [2], amount = 3 => -1
coins = [10], amount = 10 => 1
coins = [1,3,4], amount = 6 => 2 (6 = 3 + 3)

Time Complexity: O(amount * n) where n = len(coins)
Space Complexity: O(amount)
"""


# Approach 1: Dynamic Programming - Bottom-Up (Tabulation)
def coinChange_DP(coins, amount):
    """
    dp[i] = minimum coins needed to make amount i
    dp[i] = min(dp[i], dp[i - coin] + 1) for each coin

    Time: O(amount * n), Space: O(amount)
    """
    if amount == 0:
        return 0

    # Initialize with amount + 1 (impossible value)
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0  # 0 coins needed to make 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


# Approach 2: BFS - Shortest Path
def coinChange_BFS(coins, amount):
    """
    Treat this as shortest path problem.
    Each coin is a step, find minimum steps to reach amount.

    Time: O(amount * n), Space: O(amount)
    """
    from collections import deque

    if amount == 0:
        return 0

    queue = deque([(amount, 0)])  # (remaining amount, num_coins)
    visited = {amount}

    while queue:
        remaining, num_coins = queue.popleft()

        for coin in coins:
            new_amount = remaining - coin

            if new_amount == 0:
                return num_coins + 1

            if new_amount > 0 and new_amount not in visited:
                visited.add(new_amount)
                queue.append((new_amount, num_coins + 1))

    return -1


# Approach 3: Memoization - Top-Down (Recursion)
def coinChange_Memo(coins, amount):
    """
    Recursive solution with memoization

    Time: O(amount * n), Space: O(amount)
    """
    memo = {}

    def dp(remaining):
        if remaining == 0:
            return 0
        if remaining < 0:
            return -1
        if remaining in memo:
            return memo[remaining]

        min_coins = float("inf")

        for coin in coins:
            result = dp(remaining - coin)
            if result >= 0:
                min_coins = min(min_coins, result + 1)

        memo[remaining] = min_coins if min_coins != float("inf") else -1
        return memo[remaining]

    return dp(amount)


# Approach 4: DP with Coin Tracking
def coinChange_WithTracking(coins, amount):
    """
    Also track which coins are used (for reconstruction)
    """
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    parent = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin

    if dp[amount] == float("inf"):
        return -1

    # Reconstruct coins used
    coins_used = []
    current = amount
    while current > 0:
        coin = parent[current]
        coins_used.append(coin)
        current -= coin

    print(f"Coins used: {coins_used}")
    return dp[amount]


# Test Cases
def test_coinChange():
    test_cases = [
        ([1, 2, 5], 5, 1),
        ([2], 3, -1),
        ([10], 10, 1),
        ([1, 3, 4], 6, 2),
        ([3, 6, 9], 12, 2),
        ([2, 5, 10], 27, 4),
        ([], 0, 0),
        ([1], 0, 0),
        ([1], 1, 1),
    ]

    for coins, amount, expected in test_cases:
        result_dp = coinChange_DP(coins, amount)
        result_bfs = coinChange_BFS(coins, amount)
        result_memo = coinChange_Memo(coins, amount)

        assert (
            result_dp == expected
        ), f"DP failed: got {result_dp}, expected {expected}"
        assert (
            result_bfs == expected
        ), f"BFS failed: got {result_bfs}, expected {expected}"
        assert (
            result_memo == expected
        ), f"Memo failed: got {result_memo}, expected {expected}"

        print(f"coins={coins}, amount={amount} => {expected} ✓")


if __name__ == "__main__":
    test_coinChange()
    print("\nAll tests passed!")
