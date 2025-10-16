"""
LeetCode 0008: String to Integer (atoi)

Problem Statement:
Implement the myAtoi(string s) function, which converts a string to a signed 32-bit integer.

The algorithm for myAtoi(string s) is as follows:
1. Read in and ignore any leading whitespace.
2. Check if the next character is '-' or '+'. Read this character in if it is either. This determines the sign of the final result.
3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the result is 0.
5. If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then clamp the result so that it remains in the range.
6. Return the integer as the final result.

Example 1:
Input: s = "42"
Output: 42

Example 2:
Input: s = "   -42"
Output: -42

Example 3:
Input: s = "4193 with words"
Output: 4193

Constraints:
- 0 <= s.length <= 200
- s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
- -2^31 <= return value <= 2^31 - 1
"""


class StringToInteger:
    """Solution for LeetCode 0008: String to Integer (atoi)"""

    INT_MIN = -2147483648  # -2^31
    INT_MAX = 2147483647   # 2^31 - 1

    # Q1: What's the step-by-step approach to solve this problem?
    # A1: Parse string following the atoi algorithm. Time: O(n), Space: O(1)
    def my_atoi_manual(self, s: str) -> int:
        """
        Algorithm:
        1. Skip leading whitespace
        2. Check for sign (+/-)
        3. Read digits until non-digit or end
        4. Build number
        5. Clamp to 32-bit range
        """
        # Step 1: Skip leading whitespace
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1

        # If we reached the end, return 0
        if i == len(s):
            return 0

        # Step 2: Check for sign
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1

        # Step 3 & 4: Read digits and build number
        result = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])

            # Check for overflow before multiplication
            if result > self.INT_MAX // 10:
                return self.INT_MAX if sign == 1 else self.INT_MIN
            if result == self.INT_MAX // 10 and digit > 7:
                return self.INT_MAX if sign == 1 else self.INT_MIN

            result = result * 10 + digit
            i += 1

        # Apply sign
        result *= sign

        # Step 5: Clamp to 32-bit range
        if result < self.INT_MIN:
            return self.INT_MIN
        if result > self.INT_MAX:
            return self.INT_MAX

        return result

    # Q2: How can we simplify the overflow check?
    # A2: Use Python's integer flexibility, check at the end. Time: O(n), Space: O(1)
    def my_atoi_simplified(self, s: str) -> int:
        """
        Algorithm:
        1. Skip whitespace
        2. Parse sign
        3. Extract digits
        4. Clamp result
        """
        i = 0

        # Skip leading whitespace
        while i < len(s) and s[i] == ' ':
            i += 1

        # Parse sign
        sign = 1
        if i < len(s) and s[i] in ['+', '-']:
            if s[i] == '-':
                sign = -1
            i += 1

        # Extract digits
        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        # Clamp to 32-bit range
        if result < self.INT_MIN:
            return self.INT_MIN
        if result > self.INT_MAX:
            return self.INT_MAX

        return result

    # Q3: Can we use regex for pattern matching?
    # A3: Yes, but it's more complex. Time: O(n), Space: O(n) for regex pattern
    def my_atoi_regex(self, s: str) -> int:
        """
        Algorithm:
        1. Use regex to match the pattern
        2. Extract the number
        3. Clamp result
        """
        import re

        # Pattern: optional spaces, optional sign, one or more digits
        match = re.match(r'^\s*([+-]?\d+)', s)

        if not match:
            return 0

        result = int(match.group(1))

        # Clamp to 32-bit range
        if result < self.INT_MIN:
            return self.INT_MIN
        if result > self.INT_MAX:
            return self.INT_MAX

        return result

    # Q4: What are the edge cases we need to handle?
    """
    A4: Edge cases:

    1. Empty string: "" -> 0
    2. Only whitespace: "   " -> 0
    3. No digits: "+abc" -> 0
    4. Leading zeros: "00123" -> 123
    5. Sign followed by spaces: "+ 42" -> 0 (space after sign)
    6. Words after number: "4193 with words" -> 4193
    7. Only sign: "+" -> 0, "-" -> 0
    8. Overflow positive: "9999999999" -> 2147483647
    9. Overflow negative: "-9999999999" -> -2147483648
    10. Decimal point: "3.14159" -> 3
    11. Multiple signs: "++42" -> 0 (double sign)
    12. Space in middle: "1 2 3" -> 1
    """

    # Q5: How to handle whitespace correctly?
    """
    A5: Whitespace handling:

    1. Only leading whitespace is skipped
    2. Whitespace after sign stops parsing
    3. Example: "  +0 123" -> 0
    4. Example: "  -42 abc" -> -42
    5. Use isspace() for flexibility or check ' ' for strict ASCII space
    """

    # Q6: What about the sign character?
    """
    A6: Sign character rules:

    1. Only '+' or '-' is valid sign
    2. Must come after whitespace, before digits
    3. Multiple signs: "++42" -> 0 (treated as non-digit)
    4. Other characters: "*42" -> 0
    5. Sign between digits: "4-2" -> 4
    6. Only one sign is allowed
    """

    # Q7: How to detect overflow efficiently?
    """
    A7: Overflow detection strategies:

    1. Pre-check: Before result = result * 10 + digit
       - Check if result > INT_MAX // 10
       - Check if result == INT_MAX // 10 and digit > 7

    2. Post-check: After building result, compare with bounds
       - Simpler but might allow temporary overflow (not in Python)
       - Python: No native overflow, so post-check is safe

    3. For this problem: Post-check is cleaner in Python
    """

    # Q8: What's the difference between atoi and int()?
    """
    A8: Differences between atoi and int():

    1. atoi stops at first non-digit (after sign)
    2. int() raises ValueError on invalid input
    3. atoi returns 0 on error, int() raises exception
    4. atoi clamps to 32-bit, int() supports arbitrary precision
    5. atoi is more lenient (4193 with words -> 4193)
    6. int() is stricter (int("4193 with words") raises error)

    Example:
    - atoi("4193 with words") = 4193
    - int("4193 with words") -> ValueError
    """

    # Q9: Can we use state machine approach?
    # A9: Yes, state machine for cleaner parsing. Time: O(n), Space: O(1)
    def my_atoi_state_machine(self, s: str) -> int:
        """
        State machine approach:
        States: START, SIGN, NUMBER, END
        """
        state = "START"
        sign = 1
        result = 0

        for char in s:
            if state == "START":
                if char == ' ':
                    continue
                elif char in ['+', '-']:
                    sign = 1 if char == '+' else -1
                    state = "SIGN"
                elif char.isdigit():
                    result = int(char)
                    state = "NUMBER"
                else:
                    return 0
            elif state == "SIGN":
                if char.isdigit():
                    result = int(char)
                    state = "NUMBER"
                else:
                    return 0
            elif state == "NUMBER":
                if char.isdigit():
                    result = result * 10 + int(char)
                else:
                    break

        result *= sign

        # Clamp to 32-bit range
        if result < self.INT_MIN:
            return self.INT_MIN
        if result > self.INT_MAX:
            return self.INT_MAX

        return result

    # Q10: How to compare approaches?
    """
    A10: Complexity comparison:

    1. Manual parsing (Pre-check):
       - Pros: Efficient overflow handling
       - Cons: More complex overflow logic
       - Time: O(n), Space: O(1)

    2. Simplified parsing (Post-check):
       - Pros: Cleaner, easier to understand
       - Cons: Slightly less efficient for large numbers
       - Time: O(n), Space: O(1)

    3. Regex approach:
       - Pros: Concise, pattern is clear
       - Cons: Extra space for regex, overhead
       - Time: O(n), Space: O(n)

    4. State machine:
       - Pros: Very clear state transitions
       - Cons: More code, slightly more overhead
       - Time: O(n), Space: O(1)

    Best for interview: Simplified parsing - clear and concise
    """

    # Q11: What are common mistakes?
    """
    A11: Common mistakes:

    1. Not skipping leading whitespace
    2. Allowing multiple signs: "++42" should be 0
    3. Allowing space after sign: "+ 42" should be 0
    4. Not stopping at first non-digit
    5. Not handling overflow: 9999999999 should clamp
    6. Using int() directly which raises exceptions
    7. Forgetting that "3.14" should be 3
    8. Not testing edge cases thoroughly

    Testing checklist:
    - Empty string
    - Whitespace only
    - Leading zeros
    - Very large numbers
    - Negative numbers
    - Words after numbers
    - Invalid characters
    """

    # Q12: Real-world applications?
    """
    A12: Applications:

    1. String parsing: Converting string input to integers
    2. Configuration files: Parsing numeric values
    3. User input validation: Extracting numbers from input
    4. Data parsing: Reading formatted data
    5. Protocol parsing: Extracting numbers from messages
    6. Log parsing: Extracting numeric values from logs
    7. Scripting languages: Implementing atoi function
    """

    def test_my_atoi(self, method_name: str = "simplified") -> bool:
        """
        Comprehensive test suite
        """
        test_cases = [
            # (input, expected_output)
            ("42", 42),
            ("   -42", -42),
            ("4193 with words", 4193),
            ("words and 987", 0),
            ("-91283472332", -2147483648),
            ("0", 0),
            ("", 0),
            ("   ", 0),
            ("+123", 123),
            ("+-42", 0),
            ("00123", 123),
            ("3.14159", 3),
            ("+0 123", 0),
            ("9999999999", 2147483647),
            ("-9999999999", -2147483648),
            ("+", 0),
            ("-", 0),
            ("+ 42", 0),
            ("  +0 123", 0),
            ("1", 1),
            ("-1", -1),
            ("2147483647", 2147483647),
            ("-2147483648", -2147483648),
        ]

        passed = 0
        failed = 0

        method = {
            "manual": self.my_atoi_manual,
            "simplified": self.my_atoi_simplified,
            "regex": self.my_atoi_regex,
            "state_machine": self.my_atoi_state_machine,
        }.get(method_name, self.my_atoi_simplified)

        print(f"Testing {method_name} approach:")
        for input_val, expected in test_cases:
            result = method(input_val)
            status = "PASS" if result == expected else "FAIL"
            if status == "PASS":
                passed += 1
                print(f"  {status}: myAtoi(\"{input_val}\") = {result}")
            else:
                failed += 1
                print(f"  {status}: myAtoi(\"{input_val}\") = {result} (expected {expected})")

        print(f"\nResults: {passed} passed, {failed} failed")
        return failed == 0


def main():
    """Main method for testing"""
    solution = StringToInteger()

    print("=" * 60)
    print("LeetCode 0008: String to Integer (atoi)")
    print("=" * 60)

    # Example 1
    s1 = "42"
    print("\nExample 1:")
    print(f"Input: s = \"{s1}\"")
    print(f"Output (Manual):        {solution.my_atoi_manual(s1)}")
    print(f"Output (Simplified):    {solution.my_atoi_simplified(s1)}")
    print(f"Output (Regex):         {solution.my_atoi_regex(s1)}")
    print(f"Output (State Machine): {solution.my_atoi_state_machine(s1)}")

    # Example 2
    s2 = "   -42"
    print("\n" + "-" * 60)
    print("Example 2:")
    print(f"Input: s = \"{s2}\"")
    print(f"Output (Manual):        {solution.my_atoi_manual(s2)}")
    print(f"Output (Simplified):    {solution.my_atoi_simplified(s2)}")
    print(f"Output (Regex):         {solution.my_atoi_regex(s2)}")
    print(f"Output (State Machine): {solution.my_atoi_state_machine(s2)}")

    # Example 3
    s3 = "4193 with words"
    print("\n" + "-" * 60)
    print("Example 3:")
    print(f"Input: s = \"{s3}\"")
    print(f"Output (Manual):        {solution.my_atoi_manual(s3)}")
    print(f"Output (Simplified):    {solution.my_atoi_simplified(s3)}")
    print(f"Output (Regex):         {solution.my_atoi_regex(s3)}")
    print(f"Output (State Machine): {solution.my_atoi_state_machine(s3)}")

    # Example 4 - Edge case
    s4 = "words and 987"
    print("\n" + "-" * 60)
    print("Example 4 (Invalid):")
    print(f"Input: s = \"{s4}\"")
    print(f"Output (Manual):        {solution.my_atoi_manual(s4)}")
    print(f"Output (Simplified):    {solution.my_atoi_simplified(s4)}")
    print(f"Output (Regex):         {solution.my_atoi_regex(s4)}")
    print(f"Output (State Machine): {solution.my_atoi_state_machine(s4)}")

    # Example 5 - Overflow
    s5 = "-91283472332"
    print("\n" + "-" * 60)
    print("Example 5 (Overflow):")
    print(f"Input: s = \"{s5}\"")
    print(f"Output (Manual):        {solution.my_atoi_manual(s5)}")
    print(f"Output (Simplified):    {solution.my_atoi_simplified(s5)}")
    print(f"Output (Regex):         {solution.my_atoi_regex(s5)}")
    print(f"Output (State Machine): {solution.my_atoi_state_machine(s5)}")

    # Comprehensive testing
    print("\n" + "=" * 60)
    print("Running Comprehensive Tests:")
    print("=" * 60 + "\n")
    solution.test_my_atoi("simplified")

    # Performance comparison
    print("\n" + "=" * 60)
    print("Performance Comparison:")
    print("=" * 60)

    import time

    test_strings = ["42", "   -42", "4193 with words", "words and 987", "-91283472332"]
    iterations = 100000

    for s in test_strings:
        start_time = time.time()
        for _ in range(iterations):
            solution.my_atoi_manual(s)
        manual_time = (time.time() - start_time) * 1000

        start_time = time.time()
        for _ in range(iterations):
            solution.my_atoi_simplified(s)
        simplified_time = (time.time() - start_time) * 1000

        start_time = time.time()
        for _ in range(iterations):
            solution.my_atoi_regex(s)
        regex_time = (time.time() - start_time) * 1000

        start_time = time.time()
        for _ in range(iterations):
            solution.my_atoi_state_machine(s)
        state_machine_time = (time.time() - start_time) * 1000

        print(f"\nInput: \"{s}\" ({iterations} iterations)")
        print(f"  Manual approach:         {manual_time:.2f} ms")
        print(f"  Simplified approach:     {simplified_time:.2f} ms")
        print(f"  Regex approach:          {regex_time:.2f} ms")
        print(f"  State Machine approach:  {state_machine_time:.2f} ms")


if __name__ == "__main__":
    main()
