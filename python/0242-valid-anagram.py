"""
LeetCode 242: Valid Anagram

Problem:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example:
s = "anagram", t = "nagaram" => True
s = "rat", t = "car" => False
s = "a", t = "b" => False

Time Complexity: O(n log n) for sorting, O(n) for hash map
Space Complexity: O(1) for sorting (if we don't count output), O(k) for hash map (k = alphabet size)
"""

from collections import Counter


# Approach 1: Sorting
def isAnagram_Sorting(s: str, t: str) -> bool:
    """
    Two strings are anagrams if they have the same characters when sorted
    Time: O(n log n), Space: O(1) - not counting the space used by sorting
    """
    return sorted(s) == sorted(t)


# Approach 2: Hash Map / Dictionary
def isAnagram_HashMap(s: str, t: str) -> bool:
    """
    Count frequency of each character in both strings
    If frequencies match, they are anagrams
    Time: O(n), Space: O(k) where k is the alphabet size (26 for lowercase English)
    """
    if len(s) != len(t):
        return False

    char_count = {}

    # Count characters in s
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Subtract count from t
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False

    return True


# Approach 3: Counter from Collections
def isAnagram_Counter(s: str, t: str) -> bool:
    """
    Python's Counter is an elegant way to solve this
    Time: O(n), Space: O(k)
    """
    return Counter(s) == Counter(t)


# Approach 4: Two Hash Maps
def isAnagram_TwoMaps(s: str, t: str) -> bool:
    """
    Create frequency maps for both strings and compare
    """
    if len(s) != len(t):
        return False

    count_s = {}
    count_t = {}

    for i in range(len(s)):
        count_s[s[i]] = count_s.get(s[i], 0) + 1
        count_t[t[i]] = count_t.get(t[i], 0) + 1

    return count_s == count_t


# Approach 5: Array (Fixed size for lowercase English)
def isAnagram_Array(s: str, t: str) -> bool:
    """
    Use an array of size 26 for lowercase English letters
    Time: O(n), Space: O(1) - fixed size array
    """
    if len(s) != len(t):
        return False

    count = [0] * 26

    for i in range(len(s)):
        count[ord(s[i]) - ord("a")] += 1
        count[ord(t[i]) - ord("a")] -= 1

    return all(c == 0 for c in count)


# Test Cases
def test_isAnagram():
    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "b", False),
        ("ab", "ba", True),
        ("abc", "bca", True),
        ("", "", True),
        ("a", "a", True),
        ("listen", "silent", True),
        ("hello", "world", False),
    ]

    for s, t, expected in test_cases:
        assert isAnagram_Sorting(s, t) == expected, f"Sorting failed for {s}, {t}"
        assert isAnagram_HashMap(s, t) == expected, f"HashMap failed for {s}, {t}"
        assert isAnagram_Counter(s, t) == expected, f"Counter failed for {s}, {t}"
        assert isAnagram_TwoMaps(s, t) == expected, f"TwoMaps failed for {s}, {t}"
        assert isAnagram_Array(s, t) == expected, f"Array failed for {s}, {t}"

        print(f's="{s}", t="{t}" => {expected} ✓')


if __name__ == "__main__":
    test_isAnagram()
    print("\nAll tests passed!")

    # Example usage
    print(f'\nValid Anagram Example: {isAnagram_Counter("anagram", "nagaram")}')
