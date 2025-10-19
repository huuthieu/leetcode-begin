"""
LeetCode 91: Decode Ways

Problem:
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1", 'B' -> "2", ..., 'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters
using the reverse of the mapping above (there may be multiple ways).

Given a string s containing only digits, return the number of ways to decode it.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero.

Constraints:
- 1 <= s.length <= 100
- s contains only digits and may contain leading zero(s).

Time Complexity: O(n)
Space Complexity: O(n) for DP array, O(1) for optimized version
"""


# Approach 1: Dynamic Programming (Bottom-Up)
def numDecodings_dp(s):
    """
    Use DP where dp[i] = number of ways to decode s[0:i]

    Base cases:
    - dp[0] = 1 (empty string has one way)
    - dp[1] = 1 if s[0] != '0', else 0

    Recurrence:
    - If s[i-1] != '0': dp[i] += dp[i-1] (single digit decode)
    - If 10 <= int(s[i-2:i]) <= 26: dp[i] += dp[i-2] (two digit decode)

    Time: O(n)
    Space: O(n)
    """
    if not s or s[0] == '0':
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # Empty string
    dp[1] = 1  # First character (already checked it's not '0')

    for i in range(2, n + 1):
        # Check one digit decode
        one_digit = int(s[i-1])
        if one_digit >= 1:
            dp[i] += dp[i-1]

        # Check two digit decode
        two_digits = int(s[i-2:i])
        if 10 <= two_digits <= 26:
            dp[i] += dp[i-2]

    return dp[n]


# Approach 2: Dynamic Programming (Space Optimized)
def numDecodings_optimized(s):
    """
    Optimize space to O(1) by only keeping track of last two values

    Time: O(n)
    Space: O(1)
    """
    if not s or s[0] == '0':
        return 0

    n = len(s)
    prev2 = 1  # dp[i-2]
    prev1 = 1  # dp[i-1]

    for i in range(2, n + 1):
        current = 0

        # Check one digit
        if int(s[i-1]) >= 1:
            current += prev1

        # Check two digits
        two_digits = int(s[i-2:i])
        if 10 <= two_digits <= 26:
            current += prev2

        prev2 = prev1
        prev1 = current

    return prev1


# Approach 3: Memoization (Top-Down DP)
def numDecodings_memo(s):
    """
    Use recursion with memoization

    Time: O(n)
    Space: O(n) for recursion stack and memo
    """
    if not s or s[0] == '0':
        return 0

    memo = {}

    def dfs(index):
        # Base case: reached end of string
        if index == len(s):
            return 1

        # If starts with '0', invalid
        if s[index] == '0':
            return 0

        # Check memo
        if index in memo:
            return memo[index]

        # Take one digit
        result = dfs(index + 1)

        # Take two digits if valid
        if index + 1 < len(s):
            two_digits = int(s[index:index+2])
            if 10 <= two_digits <= 26:
                result += dfs(index + 2)

        memo[index] = result
        return result

    return dfs(0)


# Approach 4: Recursive (No memoization - for comparison, TLE on large inputs)
def numDecodings_recursive(s):
    """
    Pure recursion without memoization

    Time: O(2^n) - exponential
    Space: O(n) for recursion stack

    Note: This will TLE on large inputs, shown for educational purposes
    """
    def decode(index):
        # Base case
        if index == len(s):
            return 1

        # Invalid: leading zero
        if s[index] == '0':
            return 0

        # Take one digit
        ways = decode(index + 1)

        # Take two digits if valid
        if index + 1 < len(s):
            two_digits = int(s[index:index+2])
            if 10 <= two_digits <= 26:
                ways += decode(index + 2)

        return ways

    if not s or s[0] == '0':
        return 0

    return decode(0)


# Follow-up: Decode with wildcard '*' (LeetCode 639)
def numDecodingsWithWildcard(s):
    """
    Same problem but '*' can represent 1-9

    This is much more complex. Here's a simplified version.
    """
    # This would require careful case handling for:
    # - Single '*': 9 ways (1-9)
    # - '1*': 9 ways (11-19)
    # - '2*': 6 ways (21-26)
    # - '*1'-'*6': 2 ways (11/21, 12/22, ..., 16/26)
    # - '*7'-'*9': 1 way (17, 18, 19)
    # - '**': 15 ways (11-19, 21-26)
    pass


# Test Cases
def test_decode_ways():
    print("Testing Decode Ways:\n")

    test_cases = [
        ("12", 2, "Can decode as AB or L"),
        ("226", 3, "Can decode as BZ, VF, or BBF"),
        ("06", 0, "Leading zero invalid"),
        ("0", 0, "Single zero"),
        ("10", 1, "Exactly 10 - only J"),
        ("27", 1, "27 > 26, must be 2,7"),
        ("11106", 2, "Multiple valid decodings"),
        ("1", 1, "Single digit"),
        ("2101", 1, "Has zeros in middle"),
        ("230", 0, "Ends with invalid '30'"),
        ("1201234", 3, "Complex case"),
        ("111111", 13, "Many 1s = fibonacci-like"),
    ]

    for s, expected, description in test_cases:
        result1 = numDecodings_dp(s)
        result2 = numDecodings_optimized(s)
        result3 = numDecodings_memo(s)

        assert result1 == expected, f"DP failed for {description}: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimized failed for {description}: got {result2}, expected {expected}"
        assert result3 == expected, f"Memo failed for {description}: got {result3}, expected {expected}"

        # Only test recursive on small inputs to avoid timeout
        if len(s) <= 10:
            result4 = numDecodings_recursive(s)
            assert result4 == expected, f"Recursive failed for {description}"

        print(f"[PASS] {description}")
        print(f"       s = '{s}', ways = {expected}\n")


# Practice Questions
def practice_questions():
    """
    Q1: Why is this a DP problem?
    A1: It has optimal substructure (ways to decode s[0:i] depends on s[0:i-1] and s[0:i-2])
        and overlapping subproblems (same substrings decoded multiple times in recursion).

    Q2: Why does leading zero make a string invalid?
    A2: There's no mapping for '0'. 'A' starts at '1', so any standalone '0' or
        leading '0' in a two-digit number can't be decoded.

    Q3: What's the relationship to Fibonacci?
    A3: For strings without '0' and where all two-digit combinations are valid
        (like "1111"), the recurrence dp[i] = dp[i-1] + dp[i-2] is exactly Fibonacci!

    Q4: How to handle the '0' cases?
    A4: '0' can only appear as second digit in '10' or '20'. Any other '0'
        (leading, '30', '40', etc.) makes the string undecodable.

    Q5: Why check 10 <= two_digits <= 26?
    A5: Valid two-digit mappings are 10-26 (J-Z). Numbers < 10 have leading zero,
        and numbers > 26 don't have a letter mapping.

    Q6: What's the space-optimized version doing?
    A6: Since dp[i] only depends on dp[i-1] and dp[i-2], we only need to store
        these two values, reducing space from O(n) to O(1).

    Q7: Can this be solved greedily?
    A7: No. At each position, we need to consider both options (one-digit and
        two-digit decode), and both might lead to valid solutions. We need DP
        to count all possibilities.

    Q8: What if we allow mappings beyond 26?
    A8: The problem would be simpler - every digit sequence would be valid.
        Just need to handle '0' specially. Recurrence would be similar.

    Q9: Real-world applications?
    A9: - Cryptography (counting decoding possibilities)
        - DNA sequence analysis (counting valid interpretations)
        - Natural language processing (word segmentation)
        - Data compression (Huffman coding analysis)

    Q10: How does the wildcard version differ?
    A10: With '*' representing 1-9, we need to multiply by the number of
         possibilities. Must carefully handle:*, *digit, digit*, and **.
         Much more complex case analysis required.
    """
    pass


# Follow-up Problems
def follow_up_problems():
    """
    1. LeetCode 639: Decode Ways II - With wildcard '*'
       Solution: DP with careful case handling for all * combinations

    2. Count decodings with exactly K segments
       Solution: 2D DP, dp[i][k] = ways to decode s[0:i] using k segments

    3. Minimum segments to decode string
       Solution: DP, dp[i] = min segments to decode s[0:i]

    4. Decode with weighted mappings (each letter has different cost)
       Solution: DP tracking minimum cost

    5. Decode with forbidden patterns
       Solution: DP with validation at each step

    6. Circular decoding (last digit can connect to first)
       Solution: DP with special handling for wrap-around

    7. Maximum value decoding
       Solution: DP maximizing the numerical value of decoded string
    """
    pass


if __name__ == "__main__":
    test_decode_ways()
    print("="*50)
    print("All tests passed!")
    print("="*50)

    # Uncomment to see practice questions
    # help(practice_questions)
    # help(follow_up_problems)
