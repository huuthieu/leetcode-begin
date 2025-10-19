"""
LeetCode Problem 0028: Find the Index of the First Occurrence in a String

Problem:
Given two strings needle and haystack, return the index of the first occurrence
of needle in haystack, or -1 if needle is not part of haystack.

Examples:
1. Input: haystack = "sadbutsad", needle = "sad", Output: 0
2. Input: haystack = "leetcode", needle = "leeto", Output: -1
3. Input: haystack = "a", needle = "a", Output: 0

Constraints:
- 1 <= haystack.length, needle.length <= 10^4
- haystack and needle consist of only lowercase English characters
"""

from typing import List


# Q1: Built-in string method (optimal for practical use)
def strStr_builtin(haystack: str, needle: str) -> int:
    """
    Time Complexity: O(n*m) worst case, O(n+m) average case
    Space Complexity: O(1)

    Approach: Use Python's built-in find() method.
    """
    return haystack.find(needle)


# Q2: Simple brute force approach
def strStr_brute_force(haystack: str, needle: str) -> int:
    """
    Time Complexity: O(n*m)
    Space Complexity: O(1)

    Approach: Check each position in haystack for matching needle.
    """
    if len(needle) == 0:
        return 0
    if len(needle) > len(haystack):
        return -1

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i

    return -1


# Q3: Character-by-character comparison
def strStr_char_compare(haystack: str, needle: str) -> int:
    """
    Time Complexity: O(n*m)
    Space Complexity: O(1)

    Approach: Compare characters one by one.
    """
    if len(needle) == 0:
        return 0

    for i in range(len(haystack) - len(needle) + 1):
        match = True
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                match = False
                break
        if match:
            return i

    return -1


# Q4: KMP (Knuth-Morris-Pratt) Algorithm (optimal)
def strStr_kmp(haystack: str, needle: str) -> int:
    """
    Time Complexity: O(n + m)
    Space Complexity: O(m)

    Approach: KMP algorithm using prefix function for linear time search.
    """
    if len(needle) == 0:
        return 0
    if len(needle) > len(haystack):
        return -1

    def build_prefix(s):
        prefix = [0] * len(s)
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = prefix[j - 1]
            if s[i] == s[j]:
                j += 1
            prefix[i] = j
        return prefix

    prefix = build_prefix(needle)
    j = 0

    for i in range(len(haystack)):
        while j > 0 and haystack[i] != needle[j]:
            j = prefix[j - 1]
        if haystack[i] == needle[j]:
            j += 1
        if j == len(needle):
            return i - len(needle) + 1

    return -1


# Q5: Boyer-Moore Algorithm
def strStr_boyer_moore(haystack: str, needle: str) -> int:
    """
    Time Complexity: O(n/m) best case, O(n*m) worst case
    Space Complexity: O(k) where k is alphabet size

    Approach: Boyer-Moore algorithm with bad character rule.
    """
    if len(needle) == 0:
        return 0
    if len(needle) > len(haystack):
        return -1

    def bad_char_table(s):
        table = {}
        for i, char in enumerate(s):
            table[char] = i
        return table

    bad_char = bad_char_table(needle)
    i = len(needle) - 1
    h_idx = len(needle) - 1

    while h_idx < len(haystack):
        if needle[i] == haystack[h_idx]:
            if i == 0:
                return h_idx
            i -= 1
            h_idx -= 1
        else:
            h_idx += len(needle) - min(i, bad_char.get(haystack[h_idx], -1) + 1)
            i = len(needle) - 1

    return -1


# Q6: Rolling hash approach (Rabin-Karp)
def strStr_rabin_karp(haystack: str, needle: str) -> int:
    """
    Time Complexity: O(n + m) average case
    Space Complexity: O(1)

    Approach: Use rolling hash to compare substrings.
    """
    if len(needle) == 0:
        return 0
    if len(needle) > len(haystack):
        return -1

    needle_hash = hash(needle)
    window_hash = hash(haystack[:len(needle)])

    if needle_hash == window_hash and haystack[:len(needle)] == needle:
        return 0

    for i in range(1, len(haystack) - len(needle) + 1):
        window = haystack[i:i + len(needle)]
        if hash(window) == needle_hash and window == needle:
            return i

    return -1


# Q7: Two-pointer sliding window
def strStr_two_pointer(haystack: str, needle: str) -> int:
    """
    Time Complexity: O(n*m)
    Space Complexity: O(1)

    Approach: Sliding window with two pointers.
    """
    if len(needle) == 0:
        return 0
    if len(needle) > len(haystack):
        return -1

    for start in range(len(haystack) - len(needle) + 1):
        for j in range(len(needle)):
            if haystack[start + j] != needle[j]:
                break
        else:
            return start

    return -1


# Q8: Using startswith method
def strStr_startswith(haystack: str, needle: str) -> int:
    """
    Time Complexity: O(n*m)
    Space Complexity: O(1)

    Approach: Use startswith() method for comparison.
    """
    if len(needle) == 0:
        return 0

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:].startswith(needle):
            return i

    return -1


if __name__ == "__main__":
    test_cases = [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("a", "a", 0),
        ("ab", "ba", -1),
        ("aab", "aab", 0),
        ("aaaa", "aa", 0),
        ("mississippi", "issip", 4),
        ("hello", "ll", 2),
        ("abc", "", 0),
        ("aabaaab", "aabaaa", 0),
    ]

    functions = [
        strStr_builtin,
        strStr_brute_force,
        strStr_char_compare,
        strStr_kmp,
        strStr_boyer_moore,
        strStr_rabin_karp,
        strStr_two_pointer,
        strStr_startswith,
    ]

    for i, func in enumerate(functions, 1):
        print(f"\nQ{i}: {func.__name__}")
        print("-" * 70)
        all_passed = True
        for haystack, needle, expected in test_cases:
            try:
                result = func(haystack, needle)
                passed = result == expected
                all_passed = all_passed and passed
                status = "✓" if passed else "✗"
                print(f"  {status} strStr('{haystack}', '{needle}') = {result} (expected: {expected})")
            except Exception as e:
                print(f"  ✗ strStr('{haystack}', '{needle}') raised {type(e).__name__}: {e}")
                all_passed = False

        if all_passed:
            print(f"  All tests passed!")
