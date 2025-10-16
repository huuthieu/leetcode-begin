"""
LeetCode 0010: Regular Expression Matching

Problem Statement:
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
- '.' Matches any single character.
- '*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a"
Output: false

Example 3:
Input: s = "aa", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input: s = "ab", p = ".*"
Output: true

Example 5:
Input: s = "aab", p = "c*a*b"
Output: true

Constraints:
- 1 <= s.length <= 20
- 1 <= p.length <= 30
- s contains only lowercase English letters.
- p contains only lowercase English letters, '.', and '*'.
- For each appearance of the character '*', there will be a previous character in the pattern.
"""

# Practice Questions and Answers

# Q1: What's the brute force approach?
# A1: Try all possible matches recursively. Time: O(2^(m+n)), Space: O(m+n)
def is_match_brute_force(s, p):
    if not p:
        return not s

    # Check if first character matches
    first_match = bool(s) and (p[0] == s[0] or p[0] == '.')

    # If pattern has at least 2 characters and second is '*'
    if len(p) >= 2 and p[1] == '*':
        # Either match zero occurrences or one and recurse
        return (is_match_brute_force(s, p[2:]) or
                (first_match and is_match_brute_force(s[1:], p)))
    else:
        # Move both pointers if first character matches
        return first_match and is_match_brute_force(s[1:], p[1:])

# Q2: How can we optimize with memoization?
# A2: Cache results for (s_index, p_index) pairs. Time: O(m*n), Space: O(m*n)
def is_match_memo(s, p):
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        # Base case: if pattern is empty
        if j == len(p):
            result = i == len(s)
        else:
            # Check if first character matches
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # If next character is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Either skip the current pattern (match zero) or match current char
                result = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # Normal character matching
                result = first_match and dp(i + 1, j + 1)

        memo[(i, j)] = result
        return result

    return dp(0, 0)

# Q3: How can we solve this with bottom-up dynamic programming?
# A3: Build a table where dp[i][j] means s[0:i] matches p[0:j]. Time: O(m*n), Space: O(m*n)
def is_match_dp(s, p):
    m, n = len(s), len(p)
    # dp[i][j] represents if s[0:i] matches p[0:j]
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Empty string matches empty pattern
    dp[0][0] = True

    # Handle patterns like a*, a*b*, a*b*c* which can match empty string
    for j in range(2, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # '*' can match zero occurrences (take from dp[i][j-2])
                # or one or more occurrences (take from dp[i-1][j])
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (p[j - 2] == s[i - 1] or p[j - 2] == '.'))
            else:
                # Regular character or '.'
                dp[i][j] = dp[i - 1][j - 1] and (p[j - 1] == s[i - 1] or p[j - 1] == '.')

    return dp[m][n]

# Q4: Can we optimize the space complexity?
# A4: Yes, use two 1D arrays instead of 2D. Time: O(m*n), Space: O(n)
def is_match_space_optimized(s, p):
    m, n = len(s), len(p)
    prev = [False] * (n + 1)
    curr = [False] * (n + 1)

    # Empty string matches empty pattern
    prev[0] = True

    # Handle patterns like a*, a*b*
    for j in range(2, n + 1):
        if p[j - 1] == '*':
            prev[j] = prev[j - 2]

    # Fill the table
    for i in range(1, m + 1):
        curr[0] = False  # s[0:i] can never match empty pattern

        for j in range(1, n + 1):
            if p[j - 1] == '*':
                curr[j] = curr[j - 2] or (prev[j] and (p[j - 2] == s[i - 1] or p[j - 2] == '.'))
            else:
                curr[j] = prev[j - 1] and (p[j - 1] == s[i - 1] or p[j - 1] == '.')

        prev, curr = curr, prev

    return prev[n]

# Q5: What if we need to match partial strings?
# A5: Modify DP to check if pattern matches any substring
def is_match_partial(s, p):
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    dp[0][0] = True

    for j in range(2, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (p[j - 2] == s[i - 1] or p[j - 2] == '.'))
            else:
                dp[i][j] = dp[i - 1][j - 1] and (p[j - 1] == s[i - 1] or p[j - 1] == '.')

    # Check if pattern matches any substring
    return any(dp[i][n] for i in range(m + 1))

# Q6: How do we handle edge cases?
# A6: Empty string, empty pattern, only '*', only '.'
def is_match_with_validation(s, p):
    if not p:
        return not s
    return is_match_dp(s, p)

# Q7: What's the time and space complexity analysis?
"""
A7:
Brute Force: Time O(2^(m+n)), Space O(m+n) - exponential, impractical
Memoization: Time O(m*n), Space O(m*n) - each state computed once
DP (2D): Time O(m*n), Space O(m*n) - same as memoization
DP (1D): Time O(m*n), Space O(n) - optimized space
"""

# Q8: How would you trace through an example?
"""
A8: For s = "aab", p = "c*a*b"
dp[0][0] = True (empty matches empty)
dp[0][1] = False (c can't match empty)
dp[0][2] = True (c* can match empty - zero c's)
dp[0][3] = False
dp[0][4] = True (c*a* can match empty - zero c's and zero a's)
dp[0][5] = False
...
Then fill row by row checking character matches and '*' patterns
Final answer: dp[3][5] = True
"""

# Q9: What are common variations of this problem?
"""
A9:
- Wildcard Matching (with ? and *)
- Simplified regex (only specific patterns)
- Match with groups
- Match with backreferences
- Pattern matching in multiple strings
"""

# Q10: How would you implement without using built-in regex?
"""
A10: This solution already doesn't use built-in regex.
It manually implements a regex engine using dynamic programming.
This is often asked to test if candidates understand DP and pattern matching.
"""

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("", "", True),
        ("a", ".", True),
        ("ab", ".*.*.*.*.* ", False),
        ("aaa", "a*a*a*a*a*b", False),
        ("aaaa", "***a", False),
    ]

    print("Testing all approaches:")
    for s, p, expected in test_cases:
        dp_result = is_match_dp(s, p)
        memo_result = is_match_memo(s, p)
        space_opt_result = is_match_space_optimized(s, p)

        print(f"s = '{s}', p = '{p}'")
        print(f"Expected: {expected}, DP: {dp_result}, Memo: {memo_result}, Space Opt: {space_opt_result}")
        assert dp_result == expected, f"DP failed for {s}, {p}"
        assert memo_result == expected, f"Memo failed for {s}, {p}"
        assert space_opt_result == expected, f"Space opt failed for {s}, {p}"
        print("✓ Passed\n")
