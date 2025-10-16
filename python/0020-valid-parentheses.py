"""
LeetCode Problem 0020: Valid Parentheses

Problem:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Examples:
1. Input: s = "()", Output: True
2. Input: s = "()[]{}", Output: True
3. Input: s = "(]", Output: False
4. Input: s = "([)]", Output: False
5. Input: s = "{[]}", Output: True

Constraints:
- 1 <= s.length <= 10^4
- s[i] is a parenthesis: '(', ')', '{', '}', '[', ']'
"""

# Q1: Stack-based approach (optimal)
def isValid_stack(s: str) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    Approach: Use a stack to track opening brackets. For each closing bracket,
    check if it matches the top of the stack.
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:  # Closing bracket
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:  # Opening bracket
            stack.append(char)

    return len(stack) == 0


# Q2: Dictionary mapping approach
def isValid_dict(s: str) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    Approach: Similar to Q1 but with explicit dictionary mapping.
    """
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in pairs:  # Opening bracket
            stack.append(char)
        else:  # Closing bracket
            if not stack or pairs[stack.pop()] != char:
                return False

    return len(stack) == 0


# Q3: Using length check first
def isValid_length_check(s: str) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    Approach: Quick check for even length, then use stack.
    """
    if len(s) % 2 != 0:
        return False

    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            stack.append(char)

    return len(stack) == 0


# Q4: Using list as stack
def isValid_list_stack(s: str) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    Approach: Use list operations for stack management.
    """
    stack = []
    matches = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in matches:
            stack.append(char)
        elif stack and matches[stack[-1]] == char:
            stack.pop()
        else:
            return False

    return not stack


# Q5: Character count optimization
def isValid_count(s: str) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    Approach: Count each type of bracket first.
    """
    if len(s) % 2 != 0:
        return False

    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)

    return not stack


# Q6: Recursive approach
def isValid_recursive(s: str) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(n) for recursion stack

    Approach: Recursively remove matching pairs.
    """
    if len(s) == 0:
        return True

    if len(s) % 2 != 0:
        return False

    pairs = ['()', '[]', '{}']

    for pair in pairs:
        if pair in s:
            return isValid_recursive(s.replace(pair, ''))

    return False


# Q7: Using deque
def isValid_deque(s: str) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    Approach: Use deque for potentially faster operations.
    """
    from collections import deque

    if len(s) % 2 != 0:
        return False

    stack = deque()
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)

    return len(stack) == 0


# Q8: With early termination
def isValid_early_exit(s: str) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    Approach: Return early if invalid state is detected.
    """
    if len(s) % 2 != 0:
        return False

    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            if not stack:
                return False
            if stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            stack.append(char)

    return len(stack) == 0


# Q9: Using string replacement (less efficient)
def isValid_replace(s: str) -> bool:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(n)

    Approach: Repeatedly remove valid pairs (less efficient).
    """
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()', '').replace('[]', '').replace('{}', '')

    return s == ''


# Q10: Compact implementation
def isValid_compact(s: str) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    Approach: Compact and readable implementation.
    """
    stack = []
    closes = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in closes:
            if stack and stack[-1] == closes[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return not stack


if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
        (")", False),
        ("((", False),
        ("))", False),
        ("({[]})", True),
        ("({[}])", False),
        ("[", False),
        ("]", False),
        ("[]", True),
        ("{}", True),
        ("({})", True),
        ("([{}])", True),
        ("(([{}]))", True),
        ("(([{}]])", False),
    ]

    functions = [
        isValid_stack,
        isValid_dict,
        isValid_length_check,
        isValid_list_stack,
        isValid_count,
        isValid_recursive,
        isValid_deque,
        isValid_early_exit,
        isValid_replace,
        isValid_compact,
    ]

    for i, func in enumerate(functions, 1):
        print(f"\nQ{i}: {func.__name__}")
        print("-" * 70)
        all_passed = True
        for s, expected in test_cases:
            result = func(s)
            passed = result == expected
            all_passed = all_passed and passed
            status = "✓" if passed else "✗"
            print(f"  {status} isValid('{s}') = {result} (expected: {expected})")

        if all_passed:
            print(f"  All tests passed!")
