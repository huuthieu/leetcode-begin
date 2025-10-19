"""
LeetCode Problem 0029: Divide Two Integers

Problem:
Given two integers dividend and divisor, divide two integers without using
multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate towards zero, which means losing its
fractional part.

Examples:
1. Input: dividend = 10, divisor = 3, Output: 3
2. Input: dividend = 7, divisor = -3, Output: -2
3. Input: dividend = -2147483648, divisor = -1, Output: 2147483647

Constraints:
- -2^31 <= dividend, divisor <= 2^31 - 1
- divisor != 0
- Assume we are dealing with an environment that could only store integers
  within the 32-bit signed integer range: [-2^31, 2^31 - 1]
"""


# Q1: Bit manipulation approach (optimal)
def divide_bit_manipulation(dividend: int, divisor: int) -> int:
    """
    Time Complexity: O(log n)
    Space Complexity: O(log n)

    Approach: Use bit shift operations to build quotient.
    """
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    negative = (dividend < 0) ^ (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)

    quotient = 0
    current_dividend = 0

    for i in range(31, -1, -1):
        current_dividend = (current_dividend << 1) | ((dividend >> i) & 1)

        if current_dividend >= divisor:
            current_dividend -= divisor
            quotient |= (1 << i)

    return -quotient if negative else quotient


# Q2: Exponential search
def divide_exponential_search(dividend: int, divisor: int) -> int:
    """
    Time Complexity: O(log n)
    Space Complexity: O(log n)

    Approach: Use exponential search to find quotient.
    """
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    negative = (dividend < 0) ^ (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)

    if dividend < divisor:
        return 0

    quotient = 0
    power = 1

    while divisor * power <= dividend:
        power *= 2

    power //= 2

    while power >= 1:
        if divisor * power <= dividend:
            dividend -= divisor * power
            quotient += power
        power //= 2

    return -quotient if negative else quotient


# Q3: Double and subtract approach
def divide_double_subtract(dividend: int, divisor: int) -> int:
    """
    Time Complexity: O(log n)
    Space Complexity: O(1)

    Approach: Keep doubling divisor and subtracting.
    """
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    negative = (dividend < 0) ^ (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)

    quotient = 0

    while dividend >= divisor:
        temp_divisor = divisor
        power = 1

        while temp_divisor <= dividend:
            temp_divisor <<= 1
            power <<= 1

        temp_divisor >>= 1
        power >>= 1

        dividend -= temp_divisor
        quotient += power

    return -quotient if negative else quotient


# Q4: Bit shifting with accumulation
def divide_bit_shift(dividend: int, divisor: int) -> int:
    """
    Time Complexity: O(log n)
    Space Complexity: O(log n)

    Approach: Use bit shifting to accumulate quotient.
    """
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    negative = (dividend < 0) ^ (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)

    quotient = 0
    power_of_two = 1

    while (divisor << power_of_two) <= dividend:
        power_of_two += 1

    power_of_two -= 1

    for i in range(power_of_two, -1, -1):
        if (divisor << i) <= dividend:
            dividend -= (divisor << i)
            quotient += (1 << i)

    return -quotient if negative else quotient


# Q5: Recursive approach
def divide_recursive(dividend: int, divisor: int) -> int:
    """
    Time Complexity: O(log n)
    Space Complexity: O(log n)

    Approach: Recursively divide using subtraction.
    """
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    def helper(dividend, divisor):
        if dividend < divisor:
            return 0

        current = divisor
        quotient = 1

        while current <= dividend:
            temp = current
            current += temp
            quotient += quotient

        return quotient - 1 + helper(dividend - current // 2, divisor)

    negative = (dividend < 0) ^ (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)

    result = helper(dividend, divisor)
    return -result if negative else result


# Q6: Using logarithm approach
def divide_logarithm(dividend: int, divisor: int) -> int:
    """
    Time Complexity: O(log n)
    Space Complexity: O(1)

    Approach: Use logarithm properties (not suitable for interview).
    """
    import math

    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    negative = (dividend < 0) ^ (divisor < 0)
    result = int(math.exp(math.log(abs(dividend)) - math.log(abs(divisor))))

    return -result if negative else result


if __name__ == "__main__":
    test_cases = [
        (10, 3, 3),
        (7, -3, -2),
        (-2147483648, -1, 2147483647),
        (0, 1, 0),
        (1, 1, 1),
        (-1, 1, -1),
        (1, -1, -1),
        (2147483647, 1, 2147483647),
        (2147483647, 2, 1073741823),
        (100, 2, 50),
    ]

    functions = [
        divide_bit_manipulation,
        divide_exponential_search,
        divide_double_subtract,
        divide_bit_shift,
    ]

    for i, func in enumerate(functions, 1):
        print(f"\nQ{i}: {func.__name__}")
        print("-" * 70)
        all_passed = True
        for dividend, divisor, expected in test_cases:
            try:
                result = func(dividend, divisor)
                passed = result == expected
                all_passed = all_passed and passed
                status = "✓" if passed else "✗"
                print(f"  {status} divide({dividend}, {divisor}) = {result} (expected: {expected})")
            except Exception as e:
                print(f"  ✗ divide({dividend}, {divisor}) raised {type(e).__name__}: {e}")
                all_passed = False

        if all_passed:
            print(f"  All tests passed!")
