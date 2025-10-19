"""
LeetCode 198: House Robber

Problem:
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, represented by a non-negative integer.
You cannot rob two adjacent houses (security system).
Return the maximum amount of money you can rob.

Example:
nums = [1,2,3,1] => 4 (rob house 1 (money=1) and house 3 (money=3))
nums = [2,7,9,3] => 9 (rob house 1 (money=2), house 3 (money=9) and house 4 (money=3))
nums = [5,3,4,11,2] => 16 (rob house 1 (5), 3 (4), 5 (2) = 5+4+2=11, or rob 4 (11) + 1 (5) = 16)

Time Complexity: O(n)
Space Complexity: O(n) - with DP array or O(1) - optimized
"""


# Approach 1: Dynamic Programming - Tabulation
def rob_DP(nums):
    """
    dp[i] = max money robbed up to house i
    dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    Explanation:
    - Either rob current house + max from 2 steps back
    - Or skip current house and take max from 1 step back
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[-1]


# Approach 2: Space-Optimized DP
def rob_Optimized(nums):
    """
    We only need the last two values
    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2 = nums[0]  # max money robbed up to house i-2
    prev1 = max(nums[0], nums[1])  # max money robbed up to house i-1

    for i in range(2, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = current

    return prev1


# Approach 3: Memoization (Top-Down DP)
def rob_Memo(nums):
    memo = {}

    def dp(index):
        if index < 0:
            return 0
        if index == 0:
            return nums[0]
        if index in memo:
            return memo[index]

        # Either rob current or skip it
        memo[index] = max(dp(index - 1), dp(index - 2) + nums[index])
        return memo[index]

    return dp(len(nums) - 1)


# Approach 4: Reverse Iteration (Alternative)
def rob_Reverse(nums):
    """
    Instead of forward DP, we can iterate backwards
    """
    if not nums:
        return 0

    a, b = 0, 0
    for num in reversed(nums):
        a, b = max(a + num, b), a

    return b


# Test Cases
def test_rob():
    test_cases = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3], 9),
        ([5, 3, 4, 11, 2], 16),
        ([1], 1),
        ([5], 5),
        ([2, 1], 2),
        ([5, 3,4, 11, 2], 16),
        ([1, 3, 1, 3, 100], 103),
    ]

    for nums, expected in test_cases:
        result_dp = rob_DP(nums)
        result_opt = rob_Optimized(nums)
        result_memo = rob_Memo(nums)
        result_rev = rob_Reverse(nums)

        assert result_dp == expected, f"DP failed for {nums}"
        assert result_opt == expected, f"Optimized failed for {nums}"
        assert result_memo == expected, f"Memo failed for {nums}"
        assert result_rev == expected, f"Reverse failed for {nums}"

        print(f"nums={nums} => {expected} ✓")


if __name__ == "__main__":
    test_rob()
    print("\nAll tests passed!")

    # Example usage
    print(f"\nHouse Robber Example: {rob_Optimized([2, 7, 9, 3])}")
