"""
LeetCode Problem 0014: Longest Common Prefix

Problem:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Examples:
1. Input: strs = ["flower","flow","flight"], Output: "fl"
2. Input: strs = ["dog","racecar","car"], Output: ""
3. Input: strs = ["ab"], Output: "ab"
4. Input: strs = ["a"], Output: "a"

Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters
"""

# Q1: Horizontal scanning - compare first string with all others
def longestCommonPrefix_horizontal(strs: list[str]) -> str:
    """
    Time Complexity: O(n * m) where n is number of strings, m is min length
    Space Complexity: O(1)

    Approach: Start with first string as prefix, then trim it char by char
    until it matches prefix of all strings.
    """
    if not strs:
        return ""

    prefix = strs[0]

    for i in range(1, len(strs)):
        while not strs[i].startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix


# Q2: Vertical scanning - compare characters column by column
def longestCommonPrefix_vertical(strs: list[str]) -> str:
    """
    Time Complexity: O(n * m) where n is number of strings, m is min length
    Space Complexity: O(1)

    Approach: Compare character by character at each position across all strings.
    """
    if not strs:
        return ""

    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]

    return strs[0]


# Q3: Divide and conquer
def longestCommonPrefix_divide_conquer(strs: list[str]) -> str:
    """
    Time Complexity: O(n * m)
    Space Complexity: O(m) for recursion stack

    Approach: Divide array in half, find LCP of each half, then merge results.
    """
    if not strs:
        return ""

    def lcp(strs, left, right):
        if left == right:
            return strs[left]

        mid = (left + right) // 2
        lcp_left = lcp(strs, left, mid)
        lcp_right = lcp(strs, mid + 1, right)

        return common(lcp_left, lcp_right)

    def common(left, right):
        min_len = min(len(left), len(right))
        for i in range(min_len):
            if left[i] != right[i]:
                return left[:i]
        return left[:min_len]

    return lcp(strs, 0, len(strs) - 1)


# Q4: Binary search on length
def longestCommonPrefix_binary_search(strs: list[str]) -> str:
    """
    Time Complexity: O(n * m * log(m)) where n is number of strings, m is min length
    Space Complexity: O(1)

    Approach: Binary search on the length of the prefix.
    """
    if not strs:
        return ""

    def is_common_prefix(length):
        prefix = strs[0][:length]
        for i in range(1, len(strs)):
            if not strs[i].startswith(prefix):
                return False
        return True

    left, right = 0, min(len(s) for s in strs)

    while left < right:
        mid = (left + right + 1) // 2
        if is_common_prefix(mid):
            left = mid
        else:
            right = mid - 1

    return strs[0][:left]


# Q5: Trie-based approach
def longestCommonPrefix_trie(strs: list[str]) -> str:
    """
    Time Complexity: O(n * m) to build trie, O(m) to find LCP
    Space Complexity: O(n * m) for trie storage

    Approach: Build a trie of all strings, then traverse down the trie
    while there's only one child at each node.
    """
    if not strs:
        return ""

    class TrieNode:
        def __init__(self):
            self.children = {}
            self.count = 0

    root = TrieNode()

    # Build trie
    for word in strs:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1

    # Find LCP
    result = ""
    node = root
    while node.children and len(node.children) == 1:
        char = list(node.children.keys())[0]
        if node.children[char].count == len(strs):
            result += char
            node = node.children[char]
        else:
            break

    return result


# Q6: Character-by-character with early termination
def longestCommonPrefix_char_by_char(strs: list[str]) -> str:
    """
    Time Complexity: O(n * m)
    Space Complexity: O(1)

    Approach: Check each position until a mismatch is found.
    """
    if not strs:
        return ""

    if len(strs) == 1:
        return strs[0]

    min_len = min(len(s) for s in strs)

    for i in range(min_len):
        char = strs[0][i]
        for s in strs[1:]:
            if s[i] != char:
                return strs[0][:i]

    return strs[0][:min_len]


# Q7: Using zip and set
def longestCommonPrefix_zip(strs: list[str]) -> str:
    """
    Time Complexity: O(n * m)
    Space Complexity: O(1)

    Approach: Use zip to group characters by position, check for consistency.
    """
    if not strs:
        return ""

    result = ""
    for chars in zip(*strs):
        if len(set(chars)) == 1:
            result += chars[0]
        else:
            break

    return result


# Q8: Recursive horizontal scanning
def longestCommonPrefix_recursive(strs: list[str]) -> str:
    """
    Time Complexity: O(n * m)
    Space Complexity: O(m) for recursion stack

    Approach: Recursively compare strings.
    """
    if not strs:
        return ""

    def helper(strs, index):
        if index >= len(strs[0]):
            return strs[0][:index]

        char = strs[0][index]
        for s in strs[1:]:
            if index >= len(s) or s[index] != char:
                return strs[0][:index]

        return helper(strs, index + 1)

    return helper(strs, 0)


# Q9: Generator-based approach
def longestCommonPrefix_generator(strs: list[str]) -> str:
    """
    Time Complexity: O(n * m)
    Space Complexity: O(1)

    Approach: Use generator to lazily evaluate prefixes.
    """
    if not strs:
        return ""

    def prefix_gen():
        for i in range(len(strs[0])):
            char = strs[0][i]
            if all(i < len(s) and s[i] == char for s in strs[1:]):
                yield char
            else:
                break

    return "".join(prefix_gen())


# Q10: Slicing with all() function
def longestCommonPrefix_slicing(strs: list[str]) -> str:
    """
    Time Complexity: O(n * m)
    Space Complexity: O(1)

    Approach: For each position, slice all strings and check consistency.
    """
    if not strs:
        return ""

    result = ""
    for i in range(len(strs[0])):
        chars = [s[i] if i < len(s) else None for s in strs]
        if len(set(chars)) == 1 and chars[0] is not None:
            result += chars[0]
        else:
            break

    return result


if __name__ == "__main__":
    test_cases = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["ab"], "ab"),
        (["a"], "a"),
        (["interspecies", "interstellar", "interstate"], "inters"),
        (["abc"], "abc"),
        (["abab", "aba", "abc"], "ab"),
        (["", "b"], ""),
        (["a", "a", "a", "a"], "a"),
        (["aca", "cba", "bda"], ""),
    ]

    functions = [
        longestCommonPrefix_horizontal,
        longestCommonPrefix_vertical,
        longestCommonPrefix_divide_conquer,
        longestCommonPrefix_binary_search,
        longestCommonPrefix_trie,
        longestCommonPrefix_char_by_char,
        longestCommonPrefix_zip,
        longestCommonPrefix_recursive,
        longestCommonPrefix_generator,
        longestCommonPrefix_slicing,
    ]

    for i, func in enumerate(functions, 1):
        print(f"\nQ{i}: {func.__name__}")
        print("-" * 60)
        all_passed = True
        for strs, expected in test_cases:
            result = func(strs)
            passed = result == expected
            all_passed = all_passed and passed
            status = "✓" if passed else "✗"
            print(f"  {status} longestCommonPrefix({strs}) = '{result}' (expected: '{expected}')")

        if all_passed:
            print(f"  All tests passed!")
