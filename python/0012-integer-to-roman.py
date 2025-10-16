"""
LeetCode Problem 0012: Integer to Roman

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

Given an integer, convert it to a roman numeral. You may assume the input is always between 1 and 3999.

Examples:
1. Input: 3, Output: "III"
2. Input: 58, Output: "LVIII" (50 + 5 + 3 = LVIII)
3. Input: 1994, Output: "MCMXCIV" (1000 + 900 + 90 + 4 = MCMXCIV)

Constraints:
- 1 <= num <= 3999
"""

# Q1: Greedy approach using value-symbol pairs in descending order
def int_to_roman_greedy(num: int) -> str:
    """
    Time Complexity: O(1) - maximum iterations is bounded (num can be at most 3999)
    Space Complexity: O(1) - output string is at most 12 characters

    Approach: Start from largest values and greedily build the roman numeral string.
    """
    values = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    result = ""
    for value, symbol in values:
        count = num // value
        if count:
            result += symbol * count
            num -= value * count

    return result


# Q2: Same approach with different data structure (dictionary)
def int_to_roman_dict(num: int) -> str:
    """
    Time Complexity: O(1)
    Space Complexity: O(1)

    Using a dictionary for value-symbol mapping with explicit ordering.
    """
    val_sym = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    result = []
    for value, symbol in val_sym:
        while num >= value:
            result.append(symbol)
            num -= value

    return ''.join(result)


# Q3: Recursive approach
def int_to_roman_recursive(num: int) -> str:
    """
    Time Complexity: O(1)
    Space Complexity: O(1) - recursion depth is bounded

    Convert by recursively handling the largest value first.
    """
    val_sym = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    def helper(n, index):
        if n == 0:
            return ""

        value, symbol = val_sym[index]
        if n >= value:
            return symbol + helper(n - value, index)
        else:
            return helper(n, index + 1)

    return helper(num, 0)


# Q4: Using divmod for cleaner code
def int_to_roman_divmod(num: int) -> str:
    """
    Time Complexity: O(1)
    Space Complexity: O(1)

    Use divmod to separate quotient and remainder in one operation.
    """
    values = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    result = ""
    for value, symbol in values:
        count, num = divmod(num, value)
        result += symbol * count

    return result


# Q5: Subtractive notation grouping
def int_to_roman_grouped(num: int) -> str:
    """
    Time Complexity: O(1)
    Space Complexity: O(1)

    Group the values by place value (thousands, hundreds, tens, ones).
    """
    thousands = ['', 'M', 'MM', 'MMM']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCC', 'CM']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXX', 'XC']
    ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

    return (thousands[num // 1000] +
            hundreds[(num % 1000) // 100] +
            tens[(num % 100) // 10] +
            ones[num % 10])


# Q6: Iterative with list building
def int_to_roman_list(num: int) -> str:
    """
    Time Complexity: O(1)
    Space Complexity: O(1)

    Build result list and join at the end for efficiency.
    """
    val_sym = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    result = []
    for value, symbol in val_sym:
        count = num // value
        result.extend([symbol] * count)
        num %= value

    return ''.join(result)


# Q7: Generator approach
def int_to_roman_generator(num: int) -> str:
    """
    Time Complexity: O(1)
    Space Complexity: O(1)

    Use a generator for efficient symbol production.
    """
    val_sym = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    def gen_symbols():
        for value, symbol in val_sym:
            for _ in range(num // value):
                yield symbol
            num_ref[0] -= (num // value) * value

    num_ref = [num]
    return ''.join(gen_symbols())


# Q8: While loop with explicit pointer
def int_to_roman_pointer(num: int) -> str:
    """
    Time Complexity: O(1)
    Space Complexity: O(1)

    Maintain a pointer to current position in value-symbol pairs.
    """
    val_sym = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    result = ""
    i = 0
    while num > 0 and i < len(val_sym):
        value, symbol = val_sym[i]
        if num >= value:
            result += symbol
            num -= value
        else:
            i += 1

    return result


# Q9: Two-pointer approach
def int_to_roman_two_pointer(num: int) -> str:
    """
    Time Complexity: O(1)
    Space Complexity: O(1)

    Use two pointers - one for tracking value-symbol pair, one for string building.
    """
    val_sym = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    result = []
    index = 0

    while num > 0:
        if num >= val_sym[index][0]:
            result.append(val_sym[index][1])
            num -= val_sym[index][0]
        else:
            index += 1

    return ''.join(result)


# Q10: Hardcoded strings for each digit position
def int_to_roman_hardcoded(num: int) -> str:
    """
    Time Complexity: O(1)
    Space Complexity: O(1)

    Pre-computed strings for all possible digit combinations.
    """
    ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    thousands = ['', 'M', 'MM', 'MMM']

    return (thousands[num // 1000] +
            hundreds[(num % 1000) // 100] +
            tens[(num % 100) // 10] +
            ones[num % 10])


if __name__ == "__main__":
    test_cases = [
        (3, "III"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
        (1, "I"),
        (9, "IX"),
        (27, "XXVII"),
        (49, "XLIX"),
        (3999, "MMMCMXCIX"),
        (444, "CDXLIV"),
        (2023, "MMXXIII"),
    ]

    functions = [
        int_to_roman_greedy,
        int_to_roman_dict,
        int_to_roman_recursive,
        int_to_roman_divmod,
        int_to_roman_grouped,
        int_to_roman_list,
        int_to_roman_generator,
        int_to_roman_pointer,
        int_to_roman_two_pointer,
        int_to_roman_hardcoded,
    ]

    for i, func in enumerate(functions, 1):
        print(f"\nQ{i}: {func.__name__}")
        print("-" * 50)
        all_passed = True
        for num, expected in test_cases:
            result = func(num)
            passed = result == expected
            all_passed = all_passed and passed
            status = "✓" if passed else "✗"
            print(f"  {status} int_to_roman({num}) = {result} (expected: {expected})")

        if all_passed:
            print(f"  All tests passed!")
