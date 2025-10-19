"""
LeetCode 121: Best Time to Buy and Sell Stock

Problem:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and a different day
in the future to sell that stock. Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example:
prices = [7,1,5,3,6,4] => 5 (buy at 1, sell at 6)
prices = [7,6,4,3,2,1] => 0 (no transaction)
prices = [2,4,1] => 2 (buy at 2, sell at 4)

Time Complexity: O(n)
Space Complexity: O(1)
"""


# Approach 1: One Pass - Track Min Price and Max Profit
def maxProfit_OnePass(prices):
    """
    Keep track of minimum price seen so far and maximum profit.
    For each price, calculate profit if we sell at that price and update max profit.

    Intuition: We want to buy low and sell high.
    We iterate through prices and track:
    1. The minimum price seen so far (best buying opportunity)
    2. The maximum profit we can achieve
    """
    if not prices or len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        potential_profit = price - min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, price)

    return max_profit


# Approach 2: Simplified One Pass
def maxProfit_Simplified(prices):
    """
    Same logic but with different variable names and flow
    """
    max_profit = 0
    min_price = float("inf")

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


# Approach 3: Brute Force (Not Optimal - O(n^2))
def maxProfit_BruteForce(prices):
    """
    Check all possible buy-sell pairs
    Time: O(n^2), Space: O(1)
    """
    max_profit = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)

    return max_profit


# Approach 4: Two Pointer
def maxProfit_TwoPointer(prices):
    """
    Start with left pointer at min price and right pointer at current price
    Move right pointer forward, and if we find a price lower than left, move left
    """
    if len(prices) < 2:
        return 0

    left = 0  # Buy pointer
    right = 1  # Sell pointer
    max_profit = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            left = right  # Found lower price, move buy point

        right += 1

    return max_profit


# Test Cases
def test_maxProfit():
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 2, 1], 0),
        ([2, 4, 1], 2),
        ([1], 0),
        ([2, 1], 1),
        ([1, 2], 1),
        ([3, 2, 6, 5, 0, 3], 4),
        ([1, 1, 1, 1], 0),
        ([2, 1, 2, 0, 4, 4, 3], 4),
    ]

    for prices, expected in test_cases:
        result_onepass = maxProfit_OnePass(prices)
        result_simplified = maxProfit_Simplified(prices)
        result_brute = maxProfit_BruteForce(prices)
        result_twopointer = maxProfit_TwoPointer(prices)

        assert (
            result_onepass == expected
        ), f"OnePass failed for {prices}: got {result_onepass}, expected {expected}"
        assert (
            result_simplified == expected
        ), f"Simplified failed for {prices}: got {result_simplified}, expected {expected}"
        assert (
            result_brute == expected
        ), f"BruteForce failed for {prices}: got {result_brute}, expected {expected}"
        assert (
            result_twopointer == expected
        ), f"TwoPointer failed for {prices}: got {result_twopointer}, expected {expected}"

        print(f"prices={prices} => {expected} ✓")


if __name__ == "__main__":
    test_maxProfit()
    print("\nAll tests passed!")

    # Example usage
    print(f"\nBest Time to Buy and Sell Stock Example: {maxProfit_OnePass([7, 1, 5, 3, 6, 4])}")
