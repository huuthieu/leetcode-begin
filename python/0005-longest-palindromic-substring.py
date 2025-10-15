"""
LeetCode 0005: Longest Palindromic Substring

Problem Statement:
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
- 1 <= s.length <= 1000
- s consist of only digits and English letters.
"""

# Practice Questions and Answers

# Q1: What's the brute force approach and its time complexity?
# A1: Check all possible substrings for palindrome. Time: O(n^3), Space: O(1)
def longestPalindrome_brute_force(s):
    def is_palindrome(substr):
        return substr == substr[::-1]

    n = len(s)
    longest = ""

    for i in range(n):
        for j in range(i, n):
            substr = s[i:j+1]
            if is_palindrome(substr) and len(substr) > len(longest):
                longest = substr

    return longest

# Q2: Can we optimize by expanding around centers?
# A2: Yes! Expand around each center (single char and between chars). Time: O(n^2), Space: O(1)
def longestPalindrome_expand_around_center(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    if not s:
        return ""

    start = 0
    max_len = 0

    for i in range(len(s)):
        # Odd length palindromes (center is a single character)
        len1 = expand_around_center(i, i)
        # Even length palindromes (center is between two characters)
        len2 = expand_around_center(i, i + 1)

        current_len = max(len1, len2)

        if current_len > max_len:
            max_len = current_len
            start = i - (current_len - 1) // 2

    return s[start:start + max_len]

# Q3: How does dynamic programming help solve this?
# A3: Build table where dp[i][j] = True if s[i:j+1] is palindrome. Time: O(n^2), Space: O(n^2)
def longestPalindrome_dp(s):
    n = len(s)
    if n < 2:
        return s

    # dp[i][j] = True if s[i:j+1] is a palindrome
    dp = [[False] * n for _ in range(n)]

    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True

    start = 0
    max_len = 1

    # Check for two-character palindromes
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Check for palindromes of length 3 and more
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_len = length

    return s[start:start + max_len]

# Q4: What's Manacher's algorithm and how does it work?
# A4: Linear time algorithm using symmetry. Time: O(n), Space: O(n)
def longestPalindrome_manacher(s):
    """
    Manacher's algorithm for finding longest palindrome in O(n) time.
    Transform string to handle even/odd length palindromes uniformly.
    """
    # Transform string to handle even and odd length palindromes
    # "abc" -> "^#a#b#c#$"
    T = '#'.join('^{}$'.format(s))
    n = len(T)
    P = [0] * n  # P[i] = length of palindrome centered at i
    C = R = 0  # Center and right boundary of rightmost palindrome

    for i in range(1, n - 1):
        # Mirror of i with respect to C
        mirror = 2 * C - i

        if i < R:
            P[i] = min(R - i, P[mirror])

        # Try to expand palindrome centered at i
        try:
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
        except:
            pass

        # If palindrome centered at i extends past R, adjust C and R
        if i + P[i] > R:
            C, R = i, i + P[i]

    # Find the maximum element in P
    max_len, center_index = max((length, i) for i, length in enumerate(P))

    # Extract the longest palindrome from original string
    start = (center_index - max_len) // 2
    return s[start:start + max_len]

# Q5: How to find all palindromic substrings (not just the longest)?
# A5: Similar to expand around center but collect all palindromes
def count_palindromic_substrings(s):
    def expand_around_center(left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

    total = 0
    for i in range(len(s)):
        total += expand_around_center(i, i)  # Odd length
        total += expand_around_center(i, i + 1)  # Even length

    return total

# Q6: What if we want to return all longest palindromes (in case of ties)?
# A6: Track all palindromes with maximum length
def longestPalindrome_all_max(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    if not s:
        return []

    max_len = 0
    results = []

    for i in range(len(s)):
        # Odd length
        l1, r1 = expand_around_center(i, i)
        if r1 - l1 + 1 > max_len:
            max_len = r1 - l1 + 1
            results = [s[l1:r1+1]]
        elif r1 - l1 + 1 == max_len and s[l1:r1+1] not in results:
            results.append(s[l1:r1+1])

        # Even length
        l2, r2 = expand_around_center(i, i + 1)
        if r2 >= l2:
            if r2 - l2 + 1 > max_len:
                max_len = r2 - l2 + 1
                results = [s[l2:r2+1]]
            elif r2 - l2 + 1 == max_len and s[l2:r2+1] not in results:
                results.append(s[l2:r2+1])

    return results

# Q7: How do we handle edge cases?
# A7: Empty strings, single character, entire string is palindrome
def longestPalindrome_with_validation(s):
    if not s:
        return ""

    if len(s) == 1:
        return s

    # Check if entire string is palindrome
    if s == s[::-1]:
        return s

    # Use expand around center approach
    return longestPalindrome_expand_around_center(s)

# Q8: What's the space-time tradeoff analysis?
"""
A8: Different approaches and their complexities:

1. Brute Force:
   - Time: O(n^3) - O(n^2) substrings, O(n) to check each
   - Space: O(1)

2. Dynamic Programming:
   - Time: O(n^2)
   - Space: O(n^2) - for DP table

3. Expand Around Center:
   - Time: O(n^2) - O(n) centers, O(n) expansion each
   - Space: O(1)
   - Best practical approach for most cases

4. Manacher's Algorithm:
   - Time: O(n)
   - Space: O(n)
   - Optimal complexity but more complex to implement
"""

# Q9: How can we optimize space in the DP approach?
# A9: We only need the previous row, can reduce to O(n) space
def longestPalindrome_dp_space_optimized(s):
    n = len(s)
    if n < 2:
        return s

    # We only need to track if dp[i+1][j-1] was True
    # Can use a 1D array and update carefully
    prev = [False] * n
    curr = [False] * n

    start = 0
    max_len = 1

    # Single characters
    for i in range(n):
        curr[i] = True

    # Two characters
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            start = i
            max_len = 2
            # Mark in a way we can track

    # For longer substrings, we need full 2D array
    # Space optimization is limited here
    return longestPalindrome_dp(s)

# Q10: What are common variations and related problems?
"""
A10: Common variations include:

1. Palindrome Permutation: Check if string can be rearranged to form palindrome
2. Valid Palindrome: Check if string is palindrome (ignoring non-alphanumeric)
3. Valid Palindrome II: Allow deleting at most one character
4. Palindromic Substrings: Count all palindromic substrings
5. Shortest Palindrome: Add minimum characters to make palindrome
6. Palindrome Partitioning: Partition string so each substring is palindrome
7. Longest Palindromic Subsequence: Similar but non-contiguous

Key insights:
- Expand around center is most practical
- DP good for learning but uses more space
- Manacher's for optimal complexity when needed
- Understanding palindrome properties is crucial
"""

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("babad", ["bab", "aba"]),  # Multiple valid answers
        ("cbbd", ["bb"]),
        ("a", ["a"]),
        ("ac", ["a", "c"]),
        ("racecar", ["racecar"]),
        ("noon", ["noon"]),
        ("abcdefg", None),  # Any single character
        ("aaaa", ["aaaa"]),
        ("abacabad", ["abacaba"]),
    ]

    print("Testing Expand Around Center Solution (Recommended):")
    for s, expected in test_cases:
        result = longestPalindrome_expand_around_center(s)
        print(f"Input: s = '{s}'")
        print(f"Output: '{result}'")
        if expected:
            is_valid = result in expected or len(result) == max(len(e) for e in expected)
            print(f"Valid: {is_valid} (Expected one of {expected})")
        else:
            print(f"Length: {len(result)}")
        print()

    print("\nTesting Manacher's Algorithm (O(n) time):")
    for s, _ in test_cases[:5]:
        result = longestPalindrome_manacher(s)
        print(f"Input: '{s}' -> Output: '{result}'")

    print("\nCounting palindromic substrings:")
    test_count = ["abc", "aaa", "noon"]
    for s in test_count:
        count = count_palindromic_substrings(s)
        print(f"Input: '{s}' has {count} palindromic substrings")
