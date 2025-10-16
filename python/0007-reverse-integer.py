"""
LeetCode 0007: Reverse Integer

Problem Statement:
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1],
then return 0.

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0

Constraints:
- -2^31 <= x <= 2^31 - 1
- -2,147,483,648 <= x <= 2,147,483,647
"""


class ReverseInteger:
    """Solution for LeetCode 0007: Reverse Integer"""

    INT_MIN = -2147483648  # -2^31
    INT_MAX = 2147483647   # 2^31 - 1

    # Q1: What's the brute force approach to reverse an integer?
    # A1: Convert to string, reverse, convert back. Time: O(log n), Space: O(log n)
    def reverse_string(self, x: int) -> int:
        """
        Algorithm:
        1. Handle negative numbers by extracting sign
        2. Convert to string and reverse
        3. Parse back to integer
        4. Check for overflow
        """
        is_negative = x < 0
        digits = str(abs(x))
        reversed_digits = digits[::-1]

        try:
            result = int(reversed_digits)
            if is_negative:
                result = -result

            # Check for 32-bit integer overflow
            if result < self.INT_MIN or result > self.INT_MAX:
                return 0

            return result
        except ValueError:
            return 0

    # Q2: How can we reverse an integer mathematically without string conversion?
    # A2: Extract digits one by one using modulo. Time: O(log n), Space: O(1)
    def reverse_mathematical(self, x: int) -> int:
        """
        Algorithm:
        1. Extract last digit: digit = x % 10
        2. Remove last digit: x = x // 10
        3. Build reversed number: result = result * 10 + digit
        4. Check for overflow before each operation
        """
        result = 0

        while x != 0:
            # Handle negative numbers - Python's modulo behaves differently
            digit = x % 10
            x //= 10

            # Check for overflow before multiplication
            if result > self.INT_MAX // 10:
                return 0
            if result == self.INT_MAX // 10 and digit > 7:
                return 0

            # Check for underflow before multiplication
            if result < self.INT_MIN // 10:
                return 0
            if result == self.INT_MIN // 10 and digit < -8:
                return 0

            result = result * 10 + digit

        return result

    # Q3: Can we simplify the mathematical approach using Python's flexibility?
    # A3: Python allows easier handling of large integers, use bounds checking. Time: O(log n), Space: O(1)
    def reverse_optimized(self, x: int) -> int:
        """
        Algorithm:
        1. Use Python's integer flexibility
        2. Perform calculation without premature bounds checking
        3. Check final result against 32-bit bounds
        """
        result = 0

        # Work with positive value, track sign separately
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x > 0:
            digit = x % 10
            result = result * 10 + digit
            x //= 10

        result *= sign

        # Return 0 if overflow
        if result < self.INT_MIN or result > self.INT_MAX:
            return 0

        return result

    # Q4: What are the edge cases we need to handle?
    """
    A4: Edge cases:

    1. Zero: 0 -> 0
    2. Single digit: 5 -> 5, -5 -> -5
    3. Trailing zeros: 120 -> 21, 100 -> 1
    4. Negative numbers: -123 -> -321
    5. Overflow positive: 1534236469 -> 0
    6. Overflow negative: -2147483648 -> 0
    7. Boundary values: MAX_INT (2147483647), MIN_INT (-2147483648)
    """

    # Q5: How to validate overflow systematically?
    # A5: Check before each multiplication operation. Time: O(log n), Space: O(1)
    def reverse_validated(self, x: int) -> int:
        """
        Pre-check strategy:
        - Before: result * 10 + digit
        - Check: is result > MAX_INT/10?
        - Check: is result == MAX_INT/10 and digit > 7?

        Similar logic for MIN_INT with digit < -8
        """
        result = 0

        while x != 0:
            digit = x % 10

            # Pre-overflow check for positive overflow
            if result > self.INT_MAX // 10:
                return 0
            if result == self.INT_MAX // 10 and digit > 7:
                return 0

            # Pre-overflow check for negative overflow
            if result < self.INT_MIN // 10:
                return 0
            if result == self.INT_MIN // 10 and digit < -8:
                return 0

            result = result * 10 + digit
            x //= 10

        return result

    # Q6: What's the pattern for handling negative numbers in Python?
    """
    A6: Pattern analysis in Python:

    1. Modulo behavior:
       - Python: (-123) % 10 = 7 (always returns positive for positive divisor)
       - This differs from C/Java: (-123) % 10 = -3

    2. Floor division:
       - Python: (-123) // 10 = -13 (always floors toward negative infinity)
       - C/Java: (-123) / 10 = -12 (truncates toward zero)

    3. Handling:
       - Extract sign first
       - Work with absolute value
       - Apply sign at the end
       - This is cleaner and avoids language-specific modulo issues

    4. Example with sign extraction:
       - Input: -123
       - Sign: -1, x: 123
       - Reverse: 321
       - Result: -321 ✓
    """

    # Q7: How to compare approaches?
    """
    A7: Complexity comparison:

    1. String-based approach:
       - Pros: Simple, easy to understand, handles sign automatically
       - Cons: Extra space for string, slower due to conversions
       - Time: O(log n), Space: O(log n)

    2. Mathematical approach (with pre-check):
       - Pros: O(1) space, no string conversion
       - Cons: Complex overflow logic due to language quirks
       - Time: O(log n), Space: O(1)

    3. Optimized approach (sign extraction):
       - Pros: Cleaner code, handles Python's quirks well
       - Cons: Still O(1) space but with explicit sign handling
       - Time: O(log n), Space: O(1)

    Best for interview: Optimized approach - Pythonic and clear logic
    """

    # Q8: Can we use Python's built-in features more effectively?
    # A8: Yes, but for learning purposes, manual approaches are better
    def reverse_pythonic(self, x: int) -> int:
        """
        Using Python's str and slicing capabilities
        More readable but still O(log n) time
        """
        sign = -1 if x < 0 else 1
        result = int(str(abs(x))[::-1])
        result *= sign

        if result < self.INT_MIN or result > self.INT_MAX:
            return 0

        return result

    # Q9: How to test edge cases thoroughly?
    # A9: Comprehensive test suite with all edge cases
    def test_reverse(self, method_name: str = "optimized") -> bool:
        """
        Comprehensive test suite
        """
        test_cases = [
            # (input, expected_output)
            (123, 321),
            (-123, -321),
            (120, 21),
            (0, 0),
            (5, 5),
            (-5, -5),
            (100, 1),
            (1000, 1),
            (1200, 21),
            (Integer.MAX_VALUE, 0),       # 2147483647 -> overflow
            (Integer.MIN_VALUE, 0),       # -2147483648 -> overflow
            (1534236469, 0),              # overflow
            (-2147483648, 0),             # overflow
            (1, 1),
            (10, 1),
            (-1, -1),
        ]

        passed = 0
        failed = 0

        print(f"Testing {method_name} approach:")
        for input_val, expected in test_cases:
            result = self.reverse_optimized(input_val)
            status = "PASS" if result == expected else "FAIL"
            if status == "PASS":
                passed += 1
                print(f"  {status}: reverse({input_val}) = {result}")
            else:
                failed += 1
                print(f"  {status}: reverse({input_val}) = {result} (expected {expected})")

        print(f"\nResults: {passed} passed, {failed} failed")
        return failed == 0

    # Q10: What are common mistakes and pitfalls?
    """
    A10: Common mistakes:

    1. Forgetting to handle overflow:
       - Must check before result * 10 + digit
       - Easy to assume input fits in int

    2. Incorrect overflow check:
       - Must check: result > MAX_INT // 10
       - AND result == MAX_INT // 10 and digit > 7
       - Just one check is insufficient

    3. Sign handling error:
       - Python's % and // behave differently than C/Java
       - Better to extract sign first

    4. Off-by-one in boundary:
       - MAX_INT = 2147483647, last digit is 7
       - MIN_INT = -2147483648, last digit is -8
       - Easy to use wrong boundary value

    5. Not testing edge cases:
       - Must test MAX_INT, MIN_INT, 0, single digit
       - Must test values that cause overflow

    6. Python-specific issue:
       - Python's integers don't overflow naturally
       - Must manually check against 32-bit bounds
    """

    # Q11: How to optimize for different constraints?
    """
    A11: If constraints were different:

    1. If allowed to return long/bigint: No overflow check needed
    2. If allowed negative overflow: Don't check for MIN_INT case
    3. If input is always positive: Skip sign extraction
    4. If very large inputs: String-based approach anyway
    5. If performance critical: Pre-check might be slightly faster
    """

    # Q12: Real-world applications?
    """
    A12: Applications:

    1. Number theory algorithms: Palindrome checking
    2. Cryptography: Number manipulations
    3. Data validation: Reverse checking
    4. Competitive programming: Core algorithm
    5. Interview preparation: Tests integer overflow understanding
    6. Number formatting: Digit manipulation
    """


class Integer:
    """Helper class for boundary constants"""
    MAX_VALUE = 2147483647
    MIN_VALUE = -2147483648


def main():
    """Main method for testing"""
    solution = ReverseInteger()

    print("=" * 60)
    print("LeetCode 0007: Reverse Integer")
    print("=" * 60)

    # Example 1
    x1 = 123
    print("\nExample 1:")
    print(f"Input: x = {x1}")
    print(f"Output (String):      {solution.reverse_string(x1)}")
    print(f"Output (Math):        {solution.reverse_mathematical(x1)}")
    print(f"Output (Optimized):   {solution.reverse_optimized(x1)}")
    print(f"Output (Validated):   {solution.reverse_validated(x1)}")
    print(f"Output (Pythonic):    {solution.reverse_pythonic(x1)}")

    # Example 2
    x2 = -123
    print("\n" + "-" * 60)
    print("Example 2:")
    print(f"Input: x = {x2}")
    print(f"Output (String):      {solution.reverse_string(x2)}")
    print(f"Output (Math):        {solution.reverse_mathematical(x2)}")
    print(f"Output (Optimized):   {solution.reverse_optimized(x2)}")
    print(f"Output (Validated):   {solution.reverse_validated(x2)}")
    print(f"Output (Pythonic):    {solution.reverse_pythonic(x2)}")

    # Example 3
    x3 = 120
    print("\n" + "-" * 60)
    print("Example 3:")
    print(f"Input: x = {x3}")
    print(f"Output (String):      {solution.reverse_string(x3)}")
    print(f"Output (Math):        {solution.reverse_mathematical(x3)}")
    print(f"Output (Optimized):   {solution.reverse_optimized(x3)}")
    print(f"Output (Validated):   {solution.reverse_validated(x3)}")
    print(f"Output (Pythonic):    {solution.reverse_pythonic(x3)}")

    # Example 4 - Overflow case
    x4 = 1534236469
    print("\n" + "-" * 60)
    print("Example 4 (Overflow):")
    print(f"Input: x = {x4}")
    print(f"Output (String):      {solution.reverse_string(x4)}")
    print(f"Output (Math):        {solution.reverse_mathematical(x4)}")
    print(f"Output (Optimized):   {solution.reverse_optimized(x4)}")
    print(f"Output (Validated):   {solution.reverse_validated(x4)}")
    print(f"Output (Pythonic):    {solution.reverse_pythonic(x4)}")

    # Boundary cases
    print("\n" + "-" * 60)
    print("Boundary Cases:")
    print(f"MAX_INT: {Integer.MAX_VALUE} -> {solution.reverse_optimized(Integer.MAX_VALUE)}")
    print(f"MIN_INT: {Integer.MIN_VALUE} -> {solution.reverse_optimized(Integer.MIN_VALUE)}")

    # Comprehensive testing
    print("\n" + "=" * 60)
    print("Running Comprehensive Tests:")
    print("=" * 60 + "\n")
    solution.test_reverse("Optimized")

    # Performance comparison
    print("\n" + "=" * 60)
    print("Performance Comparison:")
    print("=" * 60)

    import time

    test_numbers = [123, -123, 120, 1000, 1534236469, Integer.MAX_VALUE]
    iterations = 100000

    for num in test_numbers:
        start_time = time.time()
        for _ in range(iterations):
            solution.reverse_string(num)
        string_time = (time.time() - start_time) * 1000

        start_time = time.time()
        for _ in range(iterations):
            solution.reverse_mathematical(num)
        math_time = (time.time() - start_time) * 1000

        start_time = time.time()
        for _ in range(iterations):
            solution.reverse_optimized(num)
        optimized_time = (time.time() - start_time) * 1000

        start_time = time.time()
        for _ in range(iterations):
            solution.reverse_pythonic(num)
        pythonic_time = (time.time() - start_time) * 1000

        print(f"\nInput: {num} ({iterations} iterations)")
        print(f"  String approach:       {string_time:.2f} ms")
        print(f"  Mathematical approach: {math_time:.2f} ms")
        print(f"  Optimized approach:    {optimized_time:.2f} ms")
        print(f"  Pythonic approach:     {pythonic_time:.2f} ms")


if __name__ == "__main__":
    main()
