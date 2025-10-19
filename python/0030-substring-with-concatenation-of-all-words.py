"""
LeetCode Problem 0030: Substring with Concatenation of All Words

Problem:
You are given a string s and an array of strings words of the same length.
Return all starting indices of substring(s) in s that is a concatenation of
each word in words exactly once, in any order, and without overlapping.

Examples:
1. Input: s = "barfoothefoobarman", words = ["foo","bar"], Output: [0,9]
2. Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"], Output: []
3. Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"], Output: [6,9,12]

Constraints:
- 1 <= s.length <= 10^4
- 1 <= words.length <= 5000
- 1 <= words[i].length <= 30
- s and words[i] consist of lowercase English letters
"""

from typing import List
from collections import Counter, defaultdict


# Q1: Sliding window with hash map (optimal)
def findSubstring_sliding_window(s: str, words: List[str]) -> List[int]:
    """
    Time Complexity: O(n*m) where n is length of s, m is total length of words
    Space Complexity: O(m)

    Approach: Use sliding window of size (word_length * num_words).
    """
    if not s or not words:
        return []

    word_len = len(words[0])
    num_words = len(words)
    window_size = word_len * num_words
    word_count = Counter(words)
    result = []

    for i in range(len(s) - window_size + 1):
        window = s[i:i + window_size]
        window_words = []

        for j in range(0, window_size, word_len):
            window_words.append(window[j:j + word_len])

        if Counter(window_words) == word_count:
            result.append(i)

    return result


# Q2: Optimized sliding window with rolling hash
def findSubstring_rolling(s: str, words: List[str]) -> List[int]:
    """
    Time Complexity: O(n*m)
    Space Complexity: O(m)

    Approach: Use rolling window approach with early break optimization.
    """
    if not s or not words:
        return []

    word_len = len(words[0])
    num_words = len(words)
    window_size = word_len * num_words
    word_count = Counter(words)
    result = []

    for i in range(len(s) - window_size + 1):
        seen = defaultdict(int)
        valid = True

        for j in range(num_words):
            word = s[i + j * word_len:i + (j + 1) * word_len]
            if word not in word_count:
                valid = False
                break
            seen[word] += 1
            if seen[word] > word_count[word]:
                valid = False
                break

        if valid and seen == word_count:
            result.append(i)

    return result


# Q3: Two-pointer sliding window
def findSubstring_two_pointer(s: str, words: List[str]) -> List[int]:
    """
    Time Complexity: O(n*m)
    Space Complexity: O(m)

    Approach: Use two pointers for sliding window.
    """
    if not s or not words:
        return []

    word_len = len(words[0])
    num_words = len(words)
    window_size = word_len * num_words
    word_count = Counter(words)
    result = []

    for start in range(len(s) - window_size + 1):
        window_count = defaultdict(int)

        for i in range(start, start + window_size, word_len):
            word = s[i:i + word_len]
            window_count[word] += 1

        if window_count == word_count:
            result.append(start)

    return result


# Q4: Optimized with early termination
def findSubstring_early_term(s: str, words: List[str]) -> List[int]:
    """
    Time Complexity: O(n*m)
    Space Complexity: O(m)

    Approach: Early termination when word not found.
    """
    if not s or not words:
        return []

    word_len = len(words[0])
    num_words = len(words)
    window_size = word_len * num_words
    word_count = Counter(words)
    result = []

    for i in range(len(s) - window_size + 1):
        window = s[i:i + window_size]
        current_count = defaultdict(int)
        valid = True

        for j in range(0, window_size, word_len):
            word = window[j:j + word_len]
            if word not in word_count:
                valid = False
                break
            current_count[word] += 1

        if valid and current_count == word_count:
            result.append(i)

    return result


# Q5: Dictionary approach
def findSubstring_dict(s: str, words: List[str]) -> List[int]:
    """
    Time Complexity: O(n*m)
    Space Complexity: O(m)

    Approach: Use dictionary for word tracking.
    """
    if not s or not words:
        return []

    word_len = len(words[0])
    num_words = len(words)
    window_size = word_len * num_words
    word_dict = {}

    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1

    result = []

    for i in range(len(s) - window_size + 1):
        temp_dict = {}

        for j in range(num_words):
            word = s[i + j * word_len:i + (j + 1) * word_len]
            temp_dict[word] = temp_dict.get(word, 0) + 1

        if temp_dict == word_dict:
            result.append(i)

    return result


# Q6: Set-based approach for unique words
def findSubstring_set(s: str, words: List[str]) -> List[int]:
    """
    Time Complexity: O(n*m)
    Space Complexity: O(m)

    Approach: Use set and counter for fast lookup.
    """
    if not s or not words:
        return []

    word_len = len(words[0])
    num_words = len(words)
    window_size = word_len * num_words
    word_set = set(words)
    word_count = Counter(words)
    result = []

    for i in range(len(s) - window_size + 1):
        window = s[i:i + window_size]
        window_count = Counter()

        for j in range(0, window_size, word_len):
            word = window[j:j + word_len]
            if word not in word_set:
                break
            window_count[word] += 1

        if window_count == word_count:
            result.append(i)

    return result


if __name__ == "__main__":
    test_cases = [
        ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
        ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]),
        ("a", ["a"], [0]),
        ("ab", ["a", "b"], [0]),
        ("aab", ["a", "b"], [0]),
    ]

    functions = [
        findSubstring_sliding_window,
        findSubstring_rolling,
        findSubstring_two_pointer,
        findSubstring_early_term,
        findSubstring_dict,
        findSubstring_set,
    ]

    for i, func in enumerate(functions, 1):
        print(f"\nQ{i}: {func.__name__}")
        print("-" * 70)
        all_passed = True
        for s, words, expected in test_cases:
            result = func(s, words)
            passed = sorted(result) == sorted(expected)
            all_passed = all_passed and passed
            status = "✓" if passed else "✗"
            print(f"  {status} findSubstring('{s}', {words}) = {result}")

        if all_passed:
            print(f"  All tests passed!")
