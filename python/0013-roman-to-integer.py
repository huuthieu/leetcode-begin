"""
LeetCode Problem 0013: Roman to Integer

Problem:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Given a roman numeral string s, convert it to an integer.

The key rule to remember: In Roman numerals, a smaller value before a larger value
means subtraction (I before V or X means 4 or 9, X before L or C means 40 or 90,
C before D or M means 400 or 900).

Examples:
1. Input: "III", Output: 3
2. Input: "LVIII", Output: 58 (50 + 5 + 3)
3. Input: "MCMXCIV", Output: 1994 (1000 + 900 + 90 + 4)

Constraints:
- 1 <= s.length <= 15
- s contains only the characters 'I', 'V', 'X', 'L', 'C', 'D', 'M'
- It is guaranteed that s is a valid roman numeral in the range [1, 3999]
"""

# Q1: Greedy approach - iterate right to left checking for subtraction cases
def roman_to_int_greedy(s: str) -> int:
    """
    Time Complexity: O(n) where n is the length of the string
    Space Complexity: O(1)

    Approach: Iterate from right to left. If a symbol has a smaller value than
    the next symbol, subtract it; otherwise, add it.
    """
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(s):
        current_value = values[char]
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value

    return total


# Q2: Right-to-left with comparison lookup
def roman_to_int_lookup(s: str) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Similar to Q1 but using a different iteration approach.
    """
    mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for i in range(len(s) - 1, -1, -1):
        if i < len(s) - 1 and mapping[s[i]] < mapping[s[i + 1]]:
            total -= mapping[s[i]]
        else:
            total += mapping[s[i]]

    return total


# Q3: Left-to-right approach with lookahead
def roman_to_int_lookahead(s: str) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Iterate from left to right and look ahead to check for subtraction cases.
    """
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    i = 0

    while i < len(s):
        if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
            total += values[s[i + 1]] - values[s[i]]
            i += 2
        else:
            total += values[s[i]]
            i += 1

    return total


# Q4: Dictionary with subtraction pairs
def roman_to_int_subtraction_pairs(s: str) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Store subtraction pairs explicitly to check during iteration.
    """
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    subtraction_pairs = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}

    total = 0
    i = 0

    while i < len(s):
        if i + 1 < len(s) and s[i:i+2] in subtraction_pairs:
            pair = s[i:i+2]
            if pair == 'IV':
                total += 4
            elif pair == 'IX':
                total += 9
            elif pair == 'XL':
                total += 40
            elif pair == 'XC':
                total += 90
            elif pair == 'CD':
                total += 400
            elif pair == 'CM':
                total += 900
            i += 2
        else:
            total += values[s[i]]
            i += 1

    return total


# Q5: Using list and pointers
def roman_to_int_pointers(s: str) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Maintain explicit pointers while traversing.
    """
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    i = 0
    n = len(s)

    while i < n:
        if i + 1 < n and roman_map[s[i]] < roman_map[s[i + 1]]:
            total += roman_map[s[i + 1]] - roman_map[s[i]]
            i += 2
        else:
            total += roman_map[s[i]]
            i += 1

    return total


# Q6: Accumulator pattern with lookahead
def roman_to_int_accumulator(s: str) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Use an accumulator that tracks previous value for comparison.
    """
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    chars = list(s)
    total = 0

    for i, char in enumerate(chars):
        current = values[char]
        if i + 1 < len(chars) and current < values[chars[i + 1]]:
            total -= current
        else:
            total += current

    return total


# Q7: Recursive approach with right traversal
def roman_to_int_recursive(s: str) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n) for recursion stack

    Convert recursively from right to left.
    """
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def helper(index, prev_value):
        if index < 0:
            return 0

        current_value = values[s[index]]
        if current_value < prev_value:
            return helper(index - 1, prev_value) - current_value
        else:
            return helper(index - 1, current_value) + current_value

    return helper(len(s) - 1, 0)


# Q8: Stack-based approach
def roman_to_int_stack(s: str) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n) for the stack

    Use a stack to process Roman numerals.
    """
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    stack = []

    for char in s:
        current = values[char]
        if stack and stack[-1] < current:
            stack.append(current - stack.pop())
        else:
            stack.append(current)

    return sum(stack)


# Q9: Map with subtraction value pairs
def roman_to_int_value_map(s: str) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Create a mapping that includes both individual values and subtraction cases.
    """
    value_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
        'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
    }

    total = 0
    i = 0

    while i < len(s):
        if i + 1 < len(s) and s[i:i+2] in value_map:
            two_char = s[i:i+2]
            if two_char in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
                total += value_map[two_char]
                i += 2
                continue

        total += value_map[s[i]]
        i += 1

    return total


# Q10: Reverse iteration with efficient lookup
def roman_to_int_efficient(s: str) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Most efficient implementation using reverse iteration.
    """
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for char in reversed(s):
        current_value = values[char]
        total += current_value if current_value >= prev_value else -current_value
        prev_value = max(prev_value, current_value)

    return total


if __name__ == "__main__":
    test_cases = [
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("I", 1),
        ("IX", 9),
        ("IV", 4),
        ("MMXXIII", 2023),
        ("MMMCMXCIX", 3999),
        ("XLII", 42),
        ("CDXLIV", 444),
    ]

    functions = [
        roman_to_int_greedy,
        roman_to_int_lookup,
        roman_to_int_lookahead,
        roman_to_int_subtraction_pairs,
        roman_to_int_pointers,
        roman_to_int_accumulator,
        roman_to_int_recursive,
        roman_to_int_stack,
        roman_to_int_value_map,
        roman_to_int_efficient,
    ]

    for i, func in enumerate(functions, 1):
        print(f"\nQ{i}: {func.__name__}")
        print("-" * 50)
        all_passed = True
        for s, expected in test_cases:
            result = func(s)
            passed = result == expected
            all_passed = all_passed and passed
            status = "✓" if passed else "✗"
            print(f"  {status} roman_to_int('{s}') = {result} (expected: {expected})")

        if all_passed:
            print(f"  All tests passed!")
