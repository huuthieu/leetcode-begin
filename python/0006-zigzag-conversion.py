"""
LeetCode 0006: Zigzag Conversion

Problem Statement:
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

Constraints:
- 1 <= s.length <= 1000
- s consists of English letters (lower-case and upper-case), ',' and '.'.
- 1 <= numRows <= 1000
"""

# Practice Questions and Answers

# Q1: What's the brute force approach and how does the zigzag pattern work?
# A1: Simulate the zigzag by tracking rows and direction. Time: O(n), Space: O(n)
def convert_brute_force(s, numRows):
    """
    Simulate writing the string in zigzag pattern row by row.
    """
    if numRows == 1 or numRows >= len(s):
        return s

    # Create a list for each row
    rows = [[] for _ in range(numRows)]
    current_row = 0
    going_down = False

    # Place each character in the appropriate row
    for char in s:
        rows[current_row].append(char)

        # Change direction at top and bottom rows
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down

        # Move up or down
        current_row += 1 if going_down else -1

    # Concatenate all rows
    return ''.join(''.join(row) for row in rows)

# Q2: Can we find a mathematical pattern to directly compute character positions?
# A2: Yes! Characters in each row follow a pattern based on cycle length. Time: O(n), Space: O(n)
def convert_by_row_pattern(s, numRows):
    """
    Use mathematical pattern to determine which characters go in each row.

    Pattern analysis:
    - For numRows = 4, the cycle length is 2 * numRows - 2 = 6
    - Row 0: indices 0, 6, 12, 18... (every cycleLen)
    - Row 1: indices 1, 5, 7, 11, 13, 17... (zigzag pattern)
    - Row 2: indices 2, 4, 8, 10, 14, 16... (zigzag pattern)
    - Row 3: indices 3, 9, 15, 21... (every cycleLen)
    """
    if numRows == 1 or numRows >= len(s):
        return s

    result = []
    n = len(s)
    cycle_len = 2 * numRows - 2

    for row in range(numRows):
        for i in range(row, n, cycle_len):
            result.append(s[i])

            # For middle rows, add the zigzag character
            if row != 0 and row != numRows - 1:
                zigzag_index = i + cycle_len - 2 * row
                if zigzag_index < n:
                    result.append(s[zigzag_index])

    return ''.join(result)

# Q3: How do we optimize the simulation approach?
# A3: Use string concatenation instead of nested loops. Time: O(n), Space: O(n)
def convert_optimized_simulation(s, numRows):
    """
    Optimized simulation using string concatenation.
    """
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows
    current_row = 0
    going_down = False

    for char in s:
        rows[current_row] += char

        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down

        current_row += 1 if going_down else -1

    return ''.join(rows)

# Q4: What's the pattern for calculating the cycle length?
# A4: cycleLen = 2 * numRows - 2 (down and up movement minus overlap)
def explain_cycle_pattern(numRows):
    """
    Explain the cycle pattern:
    - Going down: numRows characters
    - Going up: (numRows - 2) characters (excluding top and bottom)
    - Total cycle: numRows + (numRows - 2) = 2 * numRows - 2
    """
    if numRows == 1:
        return 1
    return 2 * numRows - 2

# Q5: How to handle edge cases?
# A5: numRows = 1, string length < numRows, empty string
def convert_with_validation(s, numRows):
    """
    Handle all edge cases properly.
    """
    # Empty string
    if not s:
        return ""

    # Single row or string shorter than rows
    if numRows == 1 or numRows >= len(s):
        return s

    # Negative or zero rows
    if numRows <= 0:
        return ""

    return convert_optimized_simulation(s, numRows)

# Q6: Can we visualize the zigzag pattern?
# A6: Yes, create a 2D grid representation for debugging
def visualize_zigzag(s, numRows):
    """
    Create a visual representation of the zigzag pattern.
    Returns a list of strings representing each row.
    """
    if numRows == 1 or numRows >= len(s):
        return [s]

    # Calculate grid width
    cycle_len = 2 * numRows - 2
    num_cycles = (len(s) + cycle_len - 1) // cycle_len
    width = num_cycles * (numRows - 1)

    # Create grid
    grid = [[' ' for _ in range(width)] for _ in range(numRows)]

    col = 0
    row = 0
    going_down = True

    for char in s:
        grid[row][col] = char

        if going_down:
            if row == numRows - 1:
                going_down = False
                row -= 1
                col += 1
            else:
                row += 1
        else:
            if row == 0:
                going_down = True
                row += 1
            else:
                row -= 1
                col += 1

    return [''.join(row) for row in grid]

# Q7: What if we need to find the original string from zigzag?
# A7: This is the reverse problem - we'd need the pattern and original indices
def reverse_zigzag(zigzag_str, numRows):
    """
    This is non-trivial because we lose positional information.
    We would need to know the pattern to reverse it.
    """
    # This requires knowing both numRows and the pattern
    # The conversion is lossy in terms of position
    pass

# Q8: How does the pattern differ for first, middle, and last rows?
"""
A8: Pattern analysis by row:

First row (row 0):
- Only characters from main vertical columns
- Indices: 0, cycleLen, 2*cycleLen, 3*cycleLen, ...

Middle rows (0 < row < numRows-1):
- Characters from both vertical and diagonal parts
- Main indices: row, row + cycleLen, row + 2*cycleLen, ...
- Diagonal indices: cycleLen - row, 2*cycleLen - row, ...

Last row (row numRows-1):
- Only characters from bottom of vertical columns
- Indices: numRows-1, numRows-1 + cycleLen, ...
"""

def convert_detailed_explanation(s, numRows):
    """
    Implementation with detailed comments explaining the pattern.
    """
    if numRows == 1 or numRows >= len(s):
        return s

    result = []
    n = len(s)
    cycle_len = 2 * numRows - 2

    for row in range(numRows):
        # Start with the first character in this row
        idx = row

        while idx < n:
            # Add the main vertical column character
            result.append(s[idx])

            # For middle rows, add the diagonal character
            if row != 0 and row != numRows - 1:
                diagonal_idx = idx + cycle_len - 2 * row
                if diagonal_idx < n:
                    result.append(s[diagonal_idx])

            # Move to next cycle
            idx += cycle_len

    return ''.join(result)

# Q9: What are the space-time complexity tradeoffs?
"""
A9: Complexity Analysis:

1. Simulation Approach:
   - Time: O(n) - visit each character once
   - Space: O(n) - store rows
   - Pros: Easy to understand and implement
   - Cons: Requires tracking direction and state

2. Mathematical Pattern Approach:
   - Time: O(n) - visit each character once
   - Space: O(n) - store result
   - Pros: Direct calculation, no state tracking
   - Cons: Pattern logic is less intuitive

Both approaches are O(n) time and space, so choice depends on:
- Code readability (simulation is clearer)
- Implementation complexity (pattern is more mathematical)
"""

# Q10: How to test and verify the solution?
def test_convert(convert_func):
    """
    Comprehensive test cases for zigzag conversion.
    """
    test_cases = [
        # (input_string, numRows, expected_output)
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
        ("AB", 1, "AB"),
        ("ABC", 2, "ACB"),
        ("ABCD", 2, "ACBD"),
        ("ABCDE", 3, "AEBDC"),
        ("", 1, ""),
        ("A", 5, "A"),
    ]

    passed = 0
    failed = 0

    for s, numRows, expected in test_cases:
        result = convert_func(s, numRows)
        if result == expected:
            passed += 1
            status = "PASS"
        else:
            failed += 1
            status = "FAIL"
        print(f"{status}: convert('{s}', {numRows}) = '{result}' (expected '{expected}')")

    print(f"\nResults: {passed} passed, {failed} failed")
    return failed == 0

# Q11: What are common mistakes and pitfalls?
"""
A11: Common mistakes:

1. Off-by-one errors in cycle calculation
   - Cycle length is 2*numRows - 2, not 2*numRows

2. Not handling edge cases:
   - numRows = 1 (no zigzag, return original)
   - String length < numRows (return original)
   - Empty string

3. Middle row calculation errors:
   - Diagonal index: i + cycleLen - 2*row
   - Easy to get the 2*row part wrong

4. Boundary checking:
   - Always verify indices are < len(s)

5. First/last row special handling:
   - They don't have diagonal characters
   - Need to skip zigzag addition

6. Direction change timing:
   - Change at row 0 and row numRows-1
   - Not at row 1 and row numRows-2
"""

# Q12: How to extend this to other patterns?
def convert_reverse_zigzag(s, numRows):
    """
    What if we want to go up first, then down?
    Similar logic but start going_down = True at row 0.
    """
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows
    current_row = numRows - 1  # Start from bottom
    going_up = True

    for char in s:
        rows[current_row] += char

        if current_row == 0 or current_row == numRows - 1:
            going_up = not going_up

        current_row += -1 if going_up else 1

    return ''.join(rows)

if __name__ == "__main__":
    print("=" * 60)
    print("LeetCode 0006: Zigzag Conversion")
    print("=" * 60)

    # Test example
    s1 = "PAYPALISHIRING"
    numRows1 = 3

    print(f"\nExample 1:")
    print(f"Input: s = '{s1}', numRows = {numRows1}")
    print(f"\nVisualization:")
    visual = visualize_zigzag(s1, numRows1)
    for row in visual:
        print(row)
    print(f"\nOutput (Simulation): '{convert_brute_force(s1, numRows1)}'")
    print(f"Output (Pattern):    '{convert_by_row_pattern(s1, numRows1)}'")

    # Example 2
    numRows2 = 4
    print(f"\n{'-'*60}")
    print(f"Example 2:")
    print(f"Input: s = '{s1}', numRows = {numRows2}")
    print(f"\nVisualization:")
    visual = visualize_zigzag(s1, numRows2)
    for row in visual:
        print(row)
    print(f"\nOutput (Simulation): '{convert_brute_force(s1, numRows2)}'")
    print(f"Output (Pattern):    '{convert_by_row_pattern(s1, numRows2)}'")

    # Pattern explanation
    print(f"\n{'-'*60}")
    print("Pattern Explanation for numRows = 4:")
    print(f"Cycle length: {explain_cycle_pattern(4)}")
    print("\nRow 0: indices 0, 6, 12, 18, ...")
    print("Row 1: indices 1, 5, 7, 11, 13, 17, ...")
    print("Row 2: indices 2, 4, 8, 10, 14, 16, ...")
    print("Row 3: indices 3, 9, 15, 21, ...")

    # Comprehensive testing
    print(f"\n{'='*60}")
    print("Running Comprehensive Tests:")
    print('='*60)
    print("\nTesting Simulation Approach:")
    test_convert(convert_brute_force)

    print("\nTesting Pattern Approach:")
    test_convert(convert_by_row_pattern)

    print("\nTesting Optimized Simulation:")
    test_convert(convert_optimized_simulation)

    # Edge cases
    print(f"\n{'='*60}")
    print("Edge Cases:")
    print('='*60)
    edge_cases = [
        ("A", 1),
        ("AB", 1),
        ("ABCDEF", 10),
        ("", 3),
    ]

    for s, numRows in edge_cases:
        result = convert_with_validation(s, numRows)
        print(f"convert('{s}', {numRows}) = '{result}'")
