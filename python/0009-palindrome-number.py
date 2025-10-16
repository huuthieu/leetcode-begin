"""
LeetCode Problem 0009: Palindrome Number

Problem:
Given an integer x, return true if x is a palindrome, and false otherwise.

A palindrome is a number that reads the same forwards and backwards.
Negative numbers are NOT palindromes.
Numbers ending with 0 are only palindromes if the entire number is just 0.

Examples:
- 121 → true (reads the same forwards and backwards)
- -121 → false (negative numbers are not palindromes)
- 10 → false (ends with 0 but is not 0)
- 0 → true (single digit)
- 1001 → true (reads the same forwards and backwards)

Constraints:
- -2^31 <= x <= 2^31 - 1
- Try not to use extra space (O(1) space complexity)
"""


# Q1: What is the brute force approach?
# A1: Convert the number to a string and check if it equals its reverse.
# Time Complexity: O(log n) - number of digits
# Space Complexity: O(log n) - string storage
def is_palindrome_string(x: int) -> bool:
    """
    Brute force approach using string conversion.
    Simple but uses extra space for string storage.
    """
    if x < 0:
        return False

    s = str(x)
    return s == s[::-1]


# Q2: How can we solve this without converting to string?
# A2: Reverse the number mathematically and compare with original.
# Time Complexity: O(log n)
# Space Complexity: O(1)
def is_palindrome_reverse(x: int) -> bool:
    """
    Mathematical approach: reverse the entire number.
    No string conversion needed, using only integer operations.
    """
    if x < 0:
        return False

    original = x
    reversed_num = 0

    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10

    return original == reversed_num


# Q3: Can we optimize further by reversing only half the number?
# A3: Yes! We can reverse only the second half and compare.
# This prevents potential overflow and is more efficient.
# Time Complexity: O(log n)
# Space Complexity: O(1)
def is_palindrome_half_reverse(x: int) -> bool:
    """
    Optimized approach: reverse only the second half of the number.
    More efficient and elegant than reversing the entire number.

    Idea: We keep reversing the second half until it becomes
    >= the first half. Then we can compare.
    """
    # Negative numbers are not palindromes
    if x < 0:
        return False

    # Single digit numbers are palindromes
    if x < 10:
        return True

    # Numbers ending with 0 (except 0 itself) are not palindromes
    if x % 10 == 0:
        return False

    reversed_half = 0

    # Reverse second half until it's >= first half
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    # For even length: x == reversed_half
    # For odd length: x == reversed_half // 10 (middle digit ignored)
    return x == reversed_half or x == reversed_half // 10


# Q4: What are the edge cases we need to handle?
# A4: Negative numbers, trailing zeros, single digits, and potential overflow.
def test_edge_cases():
    """Test various edge cases."""
    test_cases = [
        (121, True),
        (-121, False),
        (10, False),
        (0, True),
        (1, True),
        (1001, True),
        (1221, True),
        (12321, True),
        (100, False),
        (2147483647, False),  # INT_MAX
    ]

    for num, expected in test_cases:
        result = is_palindrome_half_reverse(num)
        status = "✓" if result == expected else "✗"
        print(f"{status} is_palindrome({num}) = {result} (expected {expected})")


# Q5: How would we solve this using a two-pointer approach on digits?
# A5: Extract digits into an array and use two pointers from both ends.
# Time Complexity: O(log n)
# Space Complexity: O(log n) - for storing digits
def is_palindrome_two_pointer(x: int) -> bool:
    """
    Two-pointer approach: extract digits and compare from both ends.
    Educational approach that clearly shows the palindrome check.
    """
    if x < 0:
        return False

    # Extract digits
    digits = []
    temp = x
    while temp > 0:
        digits.append(temp % 10)
        temp //= 10

    # Reverse to get correct order, then compare
    digits.reverse()
    left, right = 0, len(digits) - 1

    while left < right:
        if digits[left] != digits[right]:
            return False
        left += 1
        right -= 1

    return True


# Q6: What if we compare with the reversed number directly?
# A6: This is similar to Q2 but emphasizes the comparison approach.
def is_palindrome_direct_comparison(x: int) -> bool:
    """
    Direct comparison: create a fully reversed number and compare.
    Clear and straightforward approach.
    """
    if x < 0:
        return False

    # Handle leading zeros
    if x != 0 and x % 10 == 0:
        return False

    reversed_num = 0
    while x > 0:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10

    return x == reversed_num


# Q7: How can we handle potential overflow concerns?
# A7: By reversing only half the number, we avoid overflow issues.
def is_palindrome_no_overflow(x: int) -> bool:
    """
    Handles overflow by never creating a fully reversed number
    that exceeds the range of input numbers.

    This is the same as the half-reverse approach (Q3),
    which naturally prevents overflow.
    """
    if x < 0 or (x != 0 and x % 10 == 0):
        return False

    if x < 10:
        return True

    reversed_half = 0

    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    return x == reversed_half or x == reversed_half // 10


# Q8: What is the space-time tradeoff analysis?
# A8: Comparing different approaches:
# - String approach: Easy to understand, uses O(n) space
# - Full reverse: Uses O(1) space, slight risk of overflow
# - Half reverse: Best of both - O(1) space, no overflow risk
def comparison_analysis():
    """
    Analyze different approaches:

    Approach 1 - String Conversion:
      Pros: Easy to understand and implement
      Cons: Uses extra space O(log n), slower due to string operations

    Approach 2 - Full Reverse:
      Pros: Uses O(1) space, purely mathematical
      Cons: Potential overflow in other languages

    Approach 3 - Half Reverse (BEST):
      Pros: O(1) space, no overflow risk, most efficient
      Cons: Slightly more complex logic to understand
    """
    pass


# Q9: How do string comparison and mathematical approaches compare?
# A9: Both work, but mathematical approach is more elegant for numbers.
def string_vs_mathematical_comparison():
    """
    String Approach:
    - Intuitive: palindrome = string equals reversed string
    - Pythonic: uses string slicing
    - Downside: creates string objects

    Mathematical Approach:
    - More efficient: works directly with digits
    - Language-agnostic: doesn't rely on string manipulation
    - More elegant for pure number problems

    For interviews, prefer mathematical when possible.
    """
    pass


# Q10: What are variations of this problem?
# A10: String palindromes, checking only alphanumeric, ignoring case, etc.
def is_palindrome_string_version(s: str) -> bool:
    """
    Variation: Check if a string is a palindrome,
    ignoring non-alphanumeric characters and case.
    """
    filtered = ''.join(c.lower() for c in s if c.isalnum())
    return filtered == filtered[::-1]


def is_palindrome_only_digits(s: str) -> bool:
    """
    Variation: Check if a digit string is a palindrome.
    """
    return s == s[::-1]


def is_palindrome_custom(s: str, filter_func) -> bool:
    """
    Generic variation: Apply custom filter before palindrome check.
    """
    filtered = ''.join(c for c in s if filter_func(c))
    return filtered == filtered[::-1]


if __name__ == "__main__":
    print("=" * 60)
    print("LeetCode 0009: Palindrome Number")
    print("=" * 60)

    print("\n--- Edge Case Testing ---")
    test_edge_cases()

    print("\n--- Comparing Different Approaches ---")
    test_nums = [121, -121, 10, 0, 1221, 12321]

    for num in test_nums:
        r1 = is_palindrome_string(num)
        r2 = is_palindrome_reverse(num)
        r3 = is_palindrome_half_reverse(num)
        r4 = is_palindrome_two_pointer(num)

        match = "✓" if (r1 == r2 == r3 == r4) else "✗"
        print(f"{match} {num}: String={r1}, Reverse={r2}, HalfReverse={r3}, TwoPointer={r4}")

    print("\n--- String Palindrome Variations ---")
    test_strings = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
        "0P",
    ]

    for test_str in test_strings:
        result = is_palindrome_string_version(test_str)
        print(f"'{test_str}' → {result}")
