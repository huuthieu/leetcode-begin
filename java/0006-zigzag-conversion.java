/**
 * LeetCode 0006: Zigzag Conversion
 *
 * Problem Statement:
 * The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
 * (you may want to display this pattern in a fixed font for better legibility)
 *
 * P   A   H   N
 * A P L S I I G
 * Y   I   R
 *
 * And then read line by line: "PAHNAPLSIIGYIR"
 *
 * Write the code that will take a string and make this conversion given a number of rows:
 * string convert(string s, int numRows);
 *
 * Example 1:
 * Input: s = "PAYPALISHIRING", numRows = 3
 * Output: "PAHNAPLSIIGYIR"
 *
 * Example 2:
 * Input: s = "PAYPALISHIRING", numRows = 4
 * Output: "PINALSIGYAHRPI"
 * Explanation:
 * P     I    N
 * A   L S  I G
 * Y A   H R
 * P     I
 *
 * Example 3:
 * Input: s = "A", numRows = 1
 * Output: "A"
 *
 * Constraints:
 * - 1 <= s.length <= 1000
 * - s consists of English letters (lower-case and upper-case), ',' and '.'.
 * - 1 <= numRows <= 1000
 */

import java.util.ArrayList;
import java.util.List;

public class ZigzagConversion {

    // Q1: What's the brute force approach and how does the zigzag pattern work?
    // A1: Simulate the zigzag by tracking rows and direction. Time: O(n), Space: O(n)
    public String convert_bruteForce(String s, int numRows) {
        if (numRows == 1 || numRows >= s.length()) {
            return s;
        }

        // Create a list for each row
        List<StringBuilder> rows = new ArrayList<>();
        for (int i = 0; i < numRows; i++) {
            rows.add(new StringBuilder());
        }

        int currentRow = 0;
        boolean goingDown = false;

        // Place each character in the appropriate row
        for (char c : s.toCharArray()) {
            rows.get(currentRow).append(c);

            // Change direction at top and bottom rows
            if (currentRow == 0 || currentRow == numRows - 1) {
                goingDown = !goingDown;
            }

            // Move up or down
            currentRow += goingDown ? 1 : -1;
        }

        // Concatenate all rows
        StringBuilder result = new StringBuilder();
        for (StringBuilder row : rows) {
            result.append(row);
        }

        return result.toString();
    }

    // Q2: Can we find a mathematical pattern to directly compute character positions?
    // A2: Yes! Characters in each row follow a pattern based on cycle length. Time: O(n), Space: O(n)
    public String convert_byRowPattern(String s, int numRows) {
        /*
         * Pattern analysis:
         * - For numRows = 4, the cycle length is 2 * numRows - 2 = 6
         * - Row 0: indices 0, 6, 12, 18... (every cycleLen)
         * - Row 1: indices 1, 5, 7, 11, 13, 17... (zigzag pattern)
         * - Row 2: indices 2, 4, 8, 10, 14, 16... (zigzag pattern)
         * - Row 3: indices 3, 9, 15, 21... (every cycleLen)
         */
        if (numRows == 1 || numRows >= s.length()) {
            return s;
        }

        StringBuilder result = new StringBuilder();
        int n = s.length();
        int cycleLen = 2 * numRows - 2;

        for (int row = 0; row < numRows; row++) {
            for (int i = row; i < n; i += cycleLen) {
                result.append(s.charAt(i));

                // For middle rows, add the zigzag character
                if (row != 0 && row != numRows - 1) {
                    int zigzagIndex = i + cycleLen - 2 * row;
                    if (zigzagIndex < n) {
                        result.append(s.charAt(zigzagIndex));
                    }
                }
            }
        }

        return result.toString();
    }

    // Q3: How do we optimize the simulation approach?
    // A3: Use StringBuilder instead of List. Time: O(n), Space: O(n)
    public String convert_optimizedSimulation(String s, int numRows) {
        if (numRows == 1 || numRows >= s.length()) {
            return s;
        }

        StringBuilder[] rows = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) {
            rows[i] = new StringBuilder();
        }

        int currentRow = 0;
        boolean goingDown = false;

        for (char c : s.toCharArray()) {
            rows[currentRow].append(c);

            if (currentRow == 0 || currentRow == numRows - 1) {
                goingDown = !goingDown;
            }

            currentRow += goingDown ? 1 : -1;
        }

        StringBuilder result = new StringBuilder();
        for (StringBuilder row : rows) {
            result.append(row);
        }

        return result.toString();
    }

    // Q4: What's the pattern for calculating the cycle length?
    // A4: cycleLen = 2 * numRows - 2 (down and up movement minus overlap)
    public int calculateCycleLength(int numRows) {
        /*
         * Explain the cycle pattern:
         * - Going down: numRows characters
         * - Going up: (numRows - 2) characters (excluding top and bottom)
         * - Total cycle: numRows + (numRows - 2) = 2 * numRows - 2
         */
        if (numRows == 1) {
            return 1;
        }
        return 2 * numRows - 2;
    }

    // Q5: How to handle edge cases?
    // A5: numRows = 1, string length < numRows, empty string
    public String convert_withValidation(String s, int numRows) {
        // Empty or null string
        if (s == null || s.isEmpty()) {
            return "";
        }

        // Single row or string shorter than rows
        if (numRows == 1 || numRows >= s.length()) {
            return s;
        }

        // Negative or zero rows
        if (numRows <= 0) {
            return "";
        }

        return convert_optimizedSimulation(s, numRows);
    }

    // Q6: Can we visualize the zigzag pattern?
    // A6: Yes, create a 2D grid representation for debugging
    public String[] visualizeZigzag(String s, int numRows) {
        if (numRows == 1 || numRows >= s.length()) {
            return new String[]{s};
        }

        // Calculate grid width
        int cycleLen = 2 * numRows - 2;
        int numCycles = (s.length() + cycleLen - 1) / cycleLen;
        int width = numCycles * (numRows - 1);

        // Create grid
        char[][] grid = new char[numRows][width];
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < width; j++) {
                grid[i][j] = ' ';
            }
        }

        int col = 0;
        int row = 0;
        boolean goingDown = true;

        for (char c : s.toCharArray()) {
            grid[row][col] = c;

            if (goingDown) {
                if (row == numRows - 1) {
                    goingDown = false;
                    row--;
                    col++;
                } else {
                    row++;
                }
            } else {
                if (row == 0) {
                    goingDown = true;
                    row++;
                } else {
                    row--;
                    col++;
                }
            }
        }

        String[] result = new String[numRows];
        for (int i = 0; i < numRows; i++) {
            result[i] = new String(grid[i]);
        }

        return result;
    }

    // Q7: How does the pattern differ for first, middle, and last rows?
    /**
     * A7: Pattern analysis by row:
     *
     * First row (row 0):
     * - Only characters from main vertical columns
     * - Indices: 0, cycleLen, 2*cycleLen, 3*cycleLen, ...
     *
     * Middle rows (0 < row < numRows-1):
     * - Characters from both vertical and diagonal parts
     * - Main indices: row, row + cycleLen, row + 2*cycleLen, ...
     * - Diagonal indices: cycleLen - row, 2*cycleLen - row, ...
     *
     * Last row (row numRows-1):
     * - Only characters from bottom of vertical columns
     * - Indices: numRows-1, numRows-1 + cycleLen, ...
     */
    public String convert_detailedExplanation(String s, int numRows) {
        if (numRows == 1 || numRows >= s.length()) {
            return s;
        }

        StringBuilder result = new StringBuilder();
        int n = s.length();
        int cycleLen = 2 * numRows - 2;

        for (int row = 0; row < numRows; row++) {
            // Start with the first character in this row
            int idx = row;

            while (idx < n) {
                // Add the main vertical column character
                result.append(s.charAt(idx));

                // For middle rows, add the diagonal character
                if (row != 0 && row != numRows - 1) {
                    int diagonalIdx = idx + cycleLen - 2 * row;
                    if (diagonalIdx < n) {
                        result.append(s.charAt(diagonalIdx));
                    }
                }

                // Move to next cycle
                idx += cycleLen;
            }
        }

        return result.toString();
    }

    // Q8: What are the space-time complexity tradeoffs?
    /**
     * A8: Complexity Analysis:
     *
     * 1. Simulation Approach:
     *    - Time: O(n) - visit each character once
     *    - Space: O(n) - store rows
     *    - Pros: Easy to understand and implement
     *    - Cons: Requires tracking direction and state
     *
     * 2. Mathematical Pattern Approach:
     *    - Time: O(n) - visit each character once
     *    - Space: O(n) - store result
     *    - Pros: Direct calculation, no state tracking
     *    - Cons: Pattern logic is less intuitive
     *
     * Both approaches are O(n) time and space, so choice depends on:
     * - Code readability (simulation is clearer)
     * - Implementation complexity (pattern is more mathematical)
     */

    // Q9: How to implement with index calculation optimization?
    // A9: Pre-calculate indices for better performance
    public String convert_indexCalculation(String s, int numRows) {
        if (numRows == 1 || numRows >= s.length()) {
            return s;
        }

        char[] result = new char[s.length()];
        int index = 0;
        int n = s.length();
        int cycleLen = 2 * numRows - 2;

        for (int row = 0; row < numRows; row++) {
            for (int i = row; i < n; i += cycleLen) {
                result[index++] = s.charAt(i);

                if (row != 0 && row != numRows - 1) {
                    int zigzagIdx = i + cycleLen - 2 * row;
                    if (zigzagIdx < n) {
                        result[index++] = s.charAt(zigzagIdx);
                    }
                }
            }
        }

        return new String(result, 0, index);
    }

    // Q10: What are common mistakes and pitfalls?
    /**
     * A10: Common mistakes:
     *
     * 1. Off-by-one errors in cycle calculation
     *    - Cycle length is 2*numRows - 2, not 2*numRows
     *
     * 2. Not handling edge cases:
     *    - numRows = 1 (no zigzag, return original)
     *    - String length < numRows (return original)
     *    - Empty string
     *
     * 3. Middle row calculation errors:
     *    - Diagonal index: i + cycleLen - 2*row
     *    - Easy to get the 2*row part wrong
     *
     * 4. Boundary checking:
     *    - Always verify indices are < s.length()
     *
     * 5. First/last row special handling:
     *    - They don't have diagonal characters
     *    - Need to skip zigzag addition
     *
     * 6. Direction change timing:
     *    - Change at row 0 and row numRows-1
     *    - Not at row 1 and row numRows-2
     */

    // Q11: How to extend this to other patterns?
    // A11: What if we want to go up first, then down?
    public String convert_reverseZigzag(String s, int numRows) {
        if (numRows == 1 || numRows >= s.length()) {
            return s;
        }

        StringBuilder[] rows = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) {
            rows[i] = new StringBuilder();
        }

        int currentRow = numRows - 1;  // Start from bottom
        boolean goingUp = true;

        for (char c : s.toCharArray()) {
            rows[currentRow].append(c);

            if (currentRow == 0 || currentRow == numRows - 1) {
                goingUp = !goingUp;
            }

            currentRow += goingUp ? -1 : 1;
        }

        StringBuilder result = new StringBuilder();
        for (StringBuilder row : rows) {
            result.append(row);
        }

        return result.toString();
    }

    // Q12: How to test and verify the solution?
    // A12: Comprehensive test cases
    public boolean testConvert(String methodName) {
        TestCase[] testCases = {
            new TestCase("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
            new TestCase("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
            new TestCase("A", 1, "A"),
            new TestCase("AB", 1, "AB"),
            new TestCase("ABC", 2, "ACB"),
            new TestCase("ABCD", 2, "ACBD"),
            new TestCase("ABCDE", 3, "AEBDC"),
            new TestCase("", 1, ""),
            new TestCase("A", 5, "A"),
        };

        int passed = 0;
        int failed = 0;

        for (TestCase tc : testCases) {
            String result = convert_byRowPattern(tc.s, tc.numRows);
            if (result.equals(tc.expected)) {
                passed++;
                System.out.println("PASS: convert(\"" + tc.s + "\", " + tc.numRows +
                                 ") = \"" + result + "\"");
            } else {
                failed++;
                System.out.println("FAIL: convert(\"" + tc.s + "\", " + tc.numRows +
                                 ") = \"" + result + "\" (expected \"" + tc.expected + "\")");
            }
        }

        System.out.println("\nResults: " + passed + " passed, " + failed + " failed");
        return failed == 0;
    }

    // Helper class for test cases
    private static class TestCase {
        String s;
        int numRows;
        String expected;

        TestCase(String s, int numRows, String expected) {
            this.s = s;
            this.numRows = numRows;
            this.expected = expected;
        }
    }

    // Main method for testing
    public static void main(String[] args) {
        ZigzagConversion solution = new ZigzagConversion();

        System.out.println("=".repeat(60));
        System.out.println("LeetCode 0006: Zigzag Conversion");
        System.out.println("=".repeat(60));

        // Test example 1
        String s1 = "PAYPALISHIRING";
        int numRows1 = 3;

        System.out.println("\nExample 1:");
        System.out.println("Input: s = \"" + s1 + "\", numRows = " + numRows1);
        System.out.println("\nVisualization:");
        String[] visual = solution.visualizeZigzag(s1, numRows1);
        for (String row : visual) {
            System.out.println(row);
        }
        System.out.println("\nOutput (Simulation): \"" +
                         solution.convert_bruteForce(s1, numRows1) + "\"");
        System.out.println("Output (Pattern):    \"" +
                         solution.convert_byRowPattern(s1, numRows1) + "\"");

        // Example 2
        int numRows2 = 4;
        System.out.println("\n" + "-".repeat(60));
        System.out.println("Example 2:");
        System.out.println("Input: s = \"" + s1 + "\", numRows = " + numRows2);
        System.out.println("\nVisualization:");
        visual = solution.visualizeZigzag(s1, numRows2);
        for (String row : visual) {
            System.out.println(row);
        }
        System.out.println("\nOutput (Simulation): \"" +
                         solution.convert_bruteForce(s1, numRows2) + "\"");
        System.out.println("Output (Pattern):    \"" +
                         solution.convert_byRowPattern(s1, numRows2) + "\"");

        // Pattern explanation
        System.out.println("\n" + "-".repeat(60));
        System.out.println("Pattern Explanation for numRows = 4:");
        System.out.println("Cycle length: " + solution.calculateCycleLength(4));
        System.out.println("\nRow 0: indices 0, 6, 12, 18, ...");
        System.out.println("Row 1: indices 1, 5, 7, 11, 13, 17, ...");
        System.out.println("Row 2: indices 2, 4, 8, 10, 14, 16, ...");
        System.out.println("Row 3: indices 3, 9, 15, 21, ...");

        // Comprehensive testing
        System.out.println("\n" + "=".repeat(60));
        System.out.println("Running Comprehensive Tests:");
        System.out.println("=".repeat(60));
        System.out.println("\nTesting Pattern Approach:");
        solution.testConvert("Pattern");

        // Edge cases
        System.out.println("\n" + "=".repeat(60));
        System.out.println("Edge Cases:");
        System.out.println("=".repeat(60));

        String[][] edgeCases = {
            {"A", "1"},
            {"AB", "1"},
            {"ABCDEF", "10"},
            {"", "3"}
        };

        for (String[] testCase : edgeCases) {
            String s = testCase[0];
            int numRows = Integer.parseInt(testCase[1]);
            String result = solution.convert_withValidation(s, numRows);
            System.out.println("convert(\"" + s + "\", " + numRows + ") = \"" + result + "\"");
        }

        // Performance comparison
        System.out.println("\n" + "=".repeat(60));
        System.out.println("Performance Comparison:");
        System.out.println("=".repeat(60));

        String largeString = "A".repeat(1000);
        int rows = 10;

        long startTime = System.nanoTime();
        solution.convert_bruteForce(largeString, rows);
        long simulationTime = System.nanoTime() - startTime;

        startTime = System.nanoTime();
        solution.convert_byRowPattern(largeString, rows);
        long patternTime = System.nanoTime() - startTime;

        System.out.println("String length: " + largeString.length() + ", numRows: " + rows);
        System.out.println("Simulation approach: " + simulationTime / 1000 + " microseconds");
        System.out.println("Pattern approach:    " + patternTime / 1000 + " microseconds");
    }
}
