/**
 * LeetCode 0007: Reverse Integer
 *
 * Problem Statement:
 * Given a signed 32-bit integer x, return x with its digits reversed.
 * If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1],
 * then return 0.
 *
 * Example 1:
 * Input: x = 123
 * Output: 321
 *
 * Example 2:
 * Input: x = -123
 * Output: -321
 *
 * Example 3:
 * Input: x = 120
 * Output: 21
 *
 * Example 4:
 * Input: x = 0
 * Output: 0
 *
 * Constraints:
 * - -2^31 <= x <= 2^31 - 1
 * - -2,147,483,648 <= x <= 2,147,483,647
 */

public class ReverseInteger {

    // Q1: What's the brute force approach to reverse an integer?
    // A1: Convert to string, reverse, convert back. Time: O(log n), Space: O(log n)
    public int reverse_toString(int x) {
        /*
         * Algorithm:
         * 1. Handle negative numbers by extracting sign
         * 2. Convert to string and reverse
         * 3. Parse back to integer
         * 4. Check for overflow
         */
        boolean isNegative = x < 0;
        String digits = String.valueOf(Math.abs(x));
        String reversed = new StringBuilder(digits).reverse().toString();

        try {
            long result = Long.parseLong(reversed);
            if (isNegative) {
                result = -result;
            }

            // Check for 32-bit integer overflow
            if (result < Integer.MIN_VALUE || result > Integer.MAX_VALUE) {
                return 0;
            }

            return (int) result;
        } catch (NumberFormatException e) {
            return 0;
        }
    }

    // Q2: How can we reverse an integer mathematically without string conversion?
    // A2: Extract digits one by one using modulo. Time: O(log n), Space: O(1)
    public int reverse_mathematical(int x) {
        /*
         * Algorithm:
         * 1. Extract last digit: digit = x % 10
         * 2. Remove last digit: x = x / 10
         * 3. Build reversed number: result = result * 10 + digit
         * 4. Check for overflow before each operation
         */
        int result = 0;

        while (x != 0) {
            int digit = x % 10;
            x /= 10;

            // Check for overflow before multiplication
            // If result > MAX_INT / 10, then result * 10 will overflow
            // If result == MAX_INT / 10 and digit > 7, then result * 10 + digit will overflow
            if (result > Integer.MAX_VALUE / 10 ||
                (result == Integer.MAX_VALUE / 10 && digit > 7)) {
                return 0;
            }

            // Check for underflow before multiplication
            // If result < MIN_INT / 10, then result * 10 will underflow
            // If result == MIN_INT / 10 and digit < -8, then result * 10 + digit will underflow
            if (result < Integer.MIN_VALUE / 10 ||
                (result == Integer.MIN_VALUE / 10 && digit < -8)) {
                return 0;
            }

            result = result * 10 + digit;
        }

        return result;
    }

    // Q3: Can we use Long to simplify overflow checking?
    // A3: Yes, use Long for calculation and check at the end. Time: O(log n), Space: O(1)
    public int reverse_withLong(int x) {
        /*
         * Algorithm:
         * 1. Use long to perform calculations (no overflow)
         * 2. Check if final result is within 32-bit range
         * 3. Return 0 if overflow, else return result as int
         */
        long result = 0;

        while (x != 0) {
            int digit = x % 10;
            x /= 10;
            result = result * 10 + digit;

            // Check bounds after each operation
            if (result < Integer.MIN_VALUE || result > Integer.MAX_VALUE) {
                return 0;
            }
        }

        return (int) result;
    }

    // Q4: What are the edge cases we need to handle?
    /**
     * A4: Edge cases:
     *
     * 1. Zero: 0 -> 0
     * 2. Single digit: 5 -> 5, -5 -> -5
     * 3. Trailing zeros: 120 -> 21, 100 -> 1
     * 4. Negative numbers: -123 -> -321
     * 5. Overflow positive: 1534236469 -> 0
     * 6. Overflow negative: -2147483648 -> 0
     * 7. Boundary values: MAX_INT (2147483647), MIN_INT (-2147483648)
     */

    // Q5: How to validate overflow systematically?
    // A5: Check before each multiplication operation. Time: O(log n), Space: O(1)
    public int reverse_validated(int x) {
        /*
         * Pre-check strategy:
         * - Before: result * 10 + digit
         * - Check: is result > MAX_INT/10?
         * - Check: is result == MAX_INT/10 and digit > 7?
         *
         * Similar logic for MIN_INT with digit < -8
         */
        int result = 0;
        int INT_MAX = 2147483647;  // 2^31 - 1
        int INT_MIN = -2147483648; // -2^31

        while (x != 0) {
            int digit = x % 10;

            // Pre-overflow check
            if (result > INT_MAX / 10) return 0;
            if (result == INT_MAX / 10 && digit > 7) return 0;
            if (result < INT_MIN / 10) return 0;
            if (result == INT_MIN / 10 && digit < -8) return 0;

            result = result * 10 + digit;
            x /= 10;
        }

        return result;
    }

    // Q6: What's the pattern for handling negative numbers?
    /**
     * A6: Pattern analysis:
     *
     * 1. Sign preservation:
     *    - Negative number: keep sign through calculation
     *    - x % 10 preserves sign in Java (-123 % 10 = -3)
     *    - x / 10 preserves sign in Java (-123 / 10 = -12)
     *
     * 2. Verification:
     *    - -123 % 10 = -3 ✓
     *    - -123 / 10 = -12 ✓
     *    - result = 0 * 10 + (-3) = -3
     *    - result = -3 * 10 + (-2) = -32
     *    - result = -32 * 10 + (-1) = -321 ✓
     *
     * 3. Overflow bounds for negative:
     *    - MIN_INT / 10 = -214748364
     *    - If result == -214748364 and digit < -8, overflow
     *    - -214748364 * 10 + (-8) = -2147483648 (valid)
     *    - -214748364 * 10 + (-9) = -2147483649 (overflow)
     */

    // Q7: How to compare approaches?
    /**
     * A7: Complexity comparison:
     *
     * 1. String-based approach:
     *    - Pros: Simple, easy to understand, handles sign automatically
     *    - Cons: Extra space for string, slower due to conversions
     *    - Time: O(log n), Space: O(log n)
     *
     * 2. Mathematical approach (pre-check):
     *    - Pros: O(1) space, no string conversion
     *    - Cons: Complex overflow logic, hard to understand
     *    - Time: O(log n), Space: O(1)
     *
     * 3. Long-based approach:
     *    - Pros: Simpler overflow check (one per digit)
     *    - Cons: Uses extra space for long
     *    - Time: O(log n), Space: O(1)
     *
     * Best for interview: Long-based approach - good balance of simplicity and efficiency
     */

    // Q8: Can we solve this digit by digit without modulo operator?
    // A8: Yes, but modulo/division is the standard approach and most efficient
    public int reverse_alternativeMethod(int x) {
        /*
         * Alternative: Convert to character array
         * More complex and less efficient than mathematical approach
         */
        if (x == 0) return 0;

        StringBuilder sb = new StringBuilder();
        boolean isNegative = x < 0;

        long num = Math.abs((long) x);
        while (num > 0) {
            sb.append(num % 10);
            num /= 10;
        }

        long result = Long.parseLong(sb.toString());
        if (isNegative) result = -result;

        if (result < Integer.MIN_VALUE || result > Integer.MAX_VALUE) {
            return 0;
        }

        return (int) result;
    }

    // Q9: How to test edge cases thoroughly?
    // A9: Comprehensive test suite with all edge cases
    public boolean testReverse(String methodName) {
        TestCase[] testCases = {
            // Basic cases
            new TestCase(123, 321),
            new TestCase(-123, -321),
            new TestCase(120, 21),
            new TestCase(0, 0),

            // Single digit
            new TestCase(5, 5),
            new TestCase(-5, -5),

            // Trailing zeros
            new TestCase(100, 1),
            new TestCase(1000, 0),
            new TestCase(1200, 21),

            // Boundary values
            new TestCase(Integer.MAX_VALUE, 0),      // 2147483647 -> overflow
            new TestCase(Integer.MIN_VALUE, 0),      // -2147483648 -> overflow
            new TestCase(1534236469, 0),             // overflow
            new TestCase(-2147483648, 0),            // overflow

            // Safe boundary cases
            new TestCase(1534236467, 7646324351L),  // doesn't fit but shows pattern
            new TestCase(2147483640, 0),            // overflow
            new TestCase(2147483600, 0),            // overflow

            // Normal cases
            new TestCase(1, 1),
            new TestCase(10, 1),
            new TestCase(1000, 1),
            new TestCase(-1, -1),
        };

        int passed = 0;
        int failed = 0;

        for (TestCase tc : testCases) {
            int result = reverse_withLong(tc.input);
            if (result == tc.expected) {
                passed++;
                System.out.println("PASS: reverse(" + tc.input + ") = " + result);
            } else {
                failed++;
                System.out.println("FAIL: reverse(" + tc.input + ") = " + result +
                                 " (expected " + tc.expected + ")");
            }
        }

        System.out.println("\nResults: " + passed + " passed, " + failed + " failed");
        return failed == 0;
    }

    // Q10: What are common mistakes and pitfalls?
    /**
     * A10: Common mistakes:
     *
     * 1. Forgetting to handle overflow:
     *    - Must check before result * 10 + digit
     *    - Easy to assume input fits in int
     *
     * 2. Incorrect overflow check:
     *    - Must check: result > MAX_INT / 10
     *    - AND result == MAX_INT / 10 && digit > 7
     *    - Just one check is insufficient
     *
     * 3. Sign handling error:
     *    - x % 10 and x / 10 work correctly for negatives in Java
     *    - Some languages (C++) handle differently
     *    - Always verify behavior in your language
     *
     * 4. Off-by-one in boundary:
     *    - MAX_INT = 2147483647, last digit is 7
     *    - MIN_INT = -2147483648, last digit is -8
     *    - Easy to use wrong boundary value
     *
     * 5. Using int for intermediate calculations:
     *    - result * 10 can overflow before assignment
     *    - Use long if possible
     *
     * 6. Not testing edge cases:
     *    - Must test MAX_INT, MIN_INT, 0, single digit
     *    - Must test values that cause overflow
     */

    // Q11: How to optimize for different constraints?
    /**
     * A11: If constraints were different:
     *
     * 1. If allowed to return long: No overflow check needed
     * 2. If allowed negative overflow: Don't check for MIN_INT case
     * 3. If input is always positive: Skip negative handling
     * 4. If very large inputs: Use string-based approach anyway
     * 5. If performance critical: Pre-check might be slightly faster
     */

    // Q12: Real-world applications?
    /**
     * A12: Applications:
     *
     * 1. Number theory algorithms: Palindrome checking
     * 2. Cryptography: Number manipulations
     * 3. Data validation: Reverse checking
     * 4. Competitive programming: Core algorithm
     * 5. Interview preparation: Tests integer overflow understanding
     */

    // Helper class for test cases
    private static class TestCase {
        int input;
        long expected;

        TestCase(int input, long expected) {
            this.input = input;
            this.expected = expected;
        }
    }

    // Main method for testing
    public static void main(String[] args) {
        ReverseInteger solution = new ReverseInteger();

        System.out.println("=".repeat(60));
        System.out.println("LeetCode 0007: Reverse Integer");
        System.out.println("=".repeat(60));

        // Example 1
        int x1 = 123;
        System.out.println("\nExample 1:");
        System.out.println("Input: x = " + x1);
        System.out.println("Output (String):      " + solution.reverse_toString(x1));
        System.out.println("Output (Math):        " + solution.reverse_mathematical(x1));
        System.out.println("Output (Long):        " + solution.reverse_withLong(x1));
        System.out.println("Output (Validated):   " + solution.reverse_validated(x1));

        // Example 2
        int x2 = -123;
        System.out.println("\n" + "-".repeat(60));
        System.out.println("Example 2:");
        System.out.println("Input: x = " + x2);
        System.out.println("Output (String):      " + solution.reverse_toString(x2));
        System.out.println("Output (Math):        " + solution.reverse_mathematical(x2));
        System.out.println("Output (Long):        " + solution.reverse_withLong(x2));
        System.out.println("Output (Validated):   " + solution.reverse_validated(x2));

        // Example 3
        int x3 = 120;
        System.out.println("\n" + "-".repeat(60));
        System.out.println("Example 3:");
        System.out.println("Input: x = " + x3);
        System.out.println("Output (String):      " + solution.reverse_toString(x3));
        System.out.println("Output (Math):        " + solution.reverse_mathematical(x3));
        System.out.println("Output (Long):        " + solution.reverse_withLong(x3));
        System.out.println("Output (Validated):   " + solution.reverse_validated(x3));

        // Example 4 - Overflow case
        int x4 = 1534236469;
        System.out.println("\n" + "-".repeat(60));
        System.out.println("Example 4 (Overflow):");
        System.out.println("Input: x = " + x4);
        System.out.println("Output (String):      " + solution.reverse_toString(x4));
        System.out.println("Output (Math):        " + solution.reverse_mathematical(x4));
        System.out.println("Output (Long):        " + solution.reverse_withLong(x4));
        System.out.println("Output (Validated):   " + solution.reverse_validated(x4));

        // Boundary cases
        System.out.println("\n" + "-".repeat(60));
        System.out.println("Boundary Cases:");
        System.out.println("MAX_INT: " + Integer.MAX_VALUE +
                         " -> " + solution.reverse_withLong(Integer.MAX_VALUE));
        System.out.println("MIN_INT: " + Integer.MIN_VALUE +
                         " -> " + solution.reverse_withLong(Integer.MIN_VALUE));

        // Comprehensive testing
        System.out.println("\n" + "=".repeat(60));
        System.out.println("Running Comprehensive Tests:");
        System.out.println("=".repeat(60) + "\n");
        solution.testReverse("Long-based");

        // Performance comparison
        System.out.println("\n" + "=".repeat(60));
        System.out.println("Performance Comparison:");
        System.out.println("=".repeat(60));

        int[] testNumbers = {123, -123, 120, 1000, 1534236469, Integer.MAX_VALUE};
        int iterations = 1000000;

        for (int num : testNumbers) {
            long startTime = System.nanoTime();
            for (int i = 0; i < iterations; i++) {
                solution.reverse_toString(num);
            }
            long stringTime = System.nanoTime() - startTime;

            startTime = System.nanoTime();
            for (int i = 0; i < iterations; i++) {
                solution.reverse_mathematical(num);
            }
            long mathTime = System.nanoTime() - startTime;

            startTime = System.nanoTime();
            for (int i = 0; i < iterations; i++) {
                solution.reverse_withLong(num);
            }
            long longTime = System.nanoTime() - startTime;

            System.out.println("\nInput: " + num + " (" + iterations + " iterations)");
            System.out.println("  String approach:      " + (stringTime / 1_000_000) + " ms");
            System.out.println("  Mathematical approach: " + (mathTime / 1_000_000) + " ms");
            System.out.println("  Long approach:        " + (longTime / 1_000_000) + " ms");
        }
    }
}
