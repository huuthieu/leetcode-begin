"""
LeetCode 0003: Longest Substring Without Repeating Characters

Problem Statement:
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.
"""

# Practice Questions and Answers

# Q1: What's the brute force approach and its time complexity?
# A1: Check all substrings and verify each is unique. Time: O(n^3), Space: O(min(n,m))
def length_of_longest_substring_brute_force(s):
    def has_unique_chars(substring):
        return len(substring) == len(set(substring))

    max_length = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if has_unique_chars(s[i:j]):
                max_length = max(max_length, j - i)
    return max_length

# Q2: How can we optimize using the sliding window technique with a set?
# A2: Use two pointers and expand/shrink window. Time: O(2n) = O(n), Space: O(min(n,m))
def length_of_longest_substring_set(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Remove characters from left until no duplicate
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

# Q3: Can we optimize further with a hash map to avoid shrinking one by one?
# A3: Store character indices and jump left pointer. Time: O(n), Space: O(min(n,m))
def length_of_longest_substring_optimized(s):
    char_index = {}
    max_length = 0
    left = 0

    for right in range(len(s)):
        # If character is in window, jump left pointer
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1

        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length

# Q4: What if we need to return the actual substring instead of just length?
# A4: Keep track of the start and end indices of the longest substring
def longest_substring_without_repeating(s):
    char_index = {}
    max_length = 0
    max_start = 0
    left = 0

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1

        char_index[s[right]] = right

        if right - left + 1 > max_length:
            max_length = right - left + 1
            max_start = left

    return s[max_start:max_start + max_length]

# Q5: How would you handle the case with limited character set (e.g., only lowercase letters)?
# A5: Use array instead of hash map for O(1) access with fixed space
def length_of_longest_substring_array(s):
    # Assuming ASCII charset (128 characters)
    char_index = [-1] * 128
    max_length = 0
    left = 0

    for right in range(len(s)):
        char_code = ord(s[right])
        if char_index[char_code] >= left:
            left = char_index[char_code] + 1

        char_index[char_code] = right
        max_length = max(max_length, right - left + 1)

    return max_length

# Q6: What if we need to find all substrings with maximum length?
# A6: Store all substrings that match the maximum length
def all_longest_substrings(s):
    char_index = {}
    max_length = 0
    results = []
    left = 0

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1

        char_index[s[right]] = right
        current_length = right - left + 1

        if current_length > max_length:
            max_length = current_length
            results = [s[left:right + 1]]
        elif current_length == max_length:
            results.append(s[left:right + 1])

    return results

# Q7: What about edge cases we should consider?
# A7: Empty string, single character, all same characters, all unique characters
def length_of_longest_substring_with_validation(s):
    if not s:
        return 0
    if len(s) == 1:
        return 1

    char_index = {}
    max_length = 0
    left = 0

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1

        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length

# Q8: What's the space-time tradeoff analysis?
"""
A8:
Brute Force: O(n^3) time, O(min(n,m)) space
Sliding Window (Set): O(2n) time, O(min(n,m)) space
Sliding Window (HashMap): O(n) time, O(min(n,m)) space
Array-based (fixed charset): O(n) time, O(1) space (fixed 128 or 256)

Where n is string length and m is charset size.
The optimized hash map approach is generally preferred.
"""

# Q9: How would you solve this problem using recursion?
# A9: Recursive approach (less efficient but demonstrates the concept)
def length_of_longest_substring_recursive(s, start=0, seen=None):
    if seen is None:
        seen = set()

    if start >= len(s):
        return 0

    if s[start] in seen:
        return 0

    # Include current character
    seen.add(s[start])
    include = 1 + length_of_longest_substring_recursive(s, start + 1, seen.copy())

    # Exclude current character and start fresh
    exclude = length_of_longest_substring_recursive(s, start + 1, set())

    return max(include, exclude)

# Q10: What variations of this problem exist?
"""
A10: Common variations include:
- Longest substring with at most K distinct characters
- Longest substring with at most 2 distinct characters
- Longest repeating character replacement
- Minimum window substring
- Longest substring with same letters after replacement
- Permutation in string
- Find all anagrams in string
"""

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("a", 1),
        ("abcdef", 6),
        ("au", 2),
        ("dvdf", 3),
        ("tmmzuxt", 5)
    ]

    for s, expected in test_cases:
        result = length_of_longest_substring_optimized(s)
        print(f"Input: s = '{s}'")
        print(f"Output: {result}, Expected: {expected}")
        print(f"Correct: {result == expected}")
        print()
