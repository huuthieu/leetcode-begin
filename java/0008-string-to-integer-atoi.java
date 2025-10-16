import java.util.Arrays;

/**
 * LeetCode 0008: String to Integer (atoi)
 *
 * Problem Statement:
 * Implement the myAtoi(String s) function, which converts a string to a signed 32-bit integer.
 *
 * The algorithm for myAtoi(String s) is as follows:
 * 1. Read in and ignore any leading whitespace.
 * 2. Check if the next character is '-' or '+'. Read this character in if it is either.
 * 3. Read in next the characters until the next non-digit character or the end of the input is reached.
 * 4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
 * 5. If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], clamp the result.
 * 6. Return the integer as the final result.
 *
 * Example 1:
 * Input: s = "42"
 * Output: 42
 *
 * Example 2:
 * Input: s = "   -42"
 * Output: -42
 *
 * Example 3:
 * Input: s = "4193 with words"
 * Output: 4193
 *
 * Constraints:
 * - 0 <= s.length() <= 200
 * - s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
 * - -2^31 <= return value <= 2^31 - 1
 */

public class StringToInteger {

    private static final int INT_MIN = -2147483648;  // -2^31
    private static final int INT_MAX = 2147483647;   // 2^31 - 1

    /**
     * Q1: What's the step-by-step approach to solve this problem?
     * A1: Parse string following the atoi algorithm. Time: O(n), Space: O(1)
     *
     * Algorithm:
     * 1. Skip leading whitespace
     * 2. Check for sign (+/-)
     * 3. Read digits until non-digit or end
     * 4. Build number with overflow check
     * 5. Return clamped result
     */
    public int myAtoiManual(String s) {
        // Step 1: Skip leading whitespace
        int i = 0;
        while (i < s.length() && s.charAt(i) == ' ') {
            i++;
        }

        // If we reached the end, return 0
        if (i == s.length()) {
            return 0;
        }

        // Step 2: Check for sign
        int sign = 1;
        if (s.charAt(i) == '+') {
            i++;
        } else if (s.charAt(i) == '-') {
            sign = -1;
            i++;
        }

        // Step 3 & 4: Read digits and build number with overflow check
        int result = 0;
        while (i < s.length() && Character.isDigit(s.charAt(i))) {
            int digit = s.charAt(i) - '0';

            // Check for overflow before multiplication
            if (result > INT_MAX / 10) {
                return sign == 1 ? INT_MAX : INT_MIN;
            }
            if (result == INT_MAX / 10 && digit > 7) {
                return sign == 1 ? INT_MAX : INT_MIN;
            }

            result = result * 10 + digit;
            i++;
        }

        return result * sign;
    }

    /**
     * Q2: How can we simplify the overflow check?
     * A2: Check after parsing, using long for intermediate result. Time: O(n), Space: O(1)
     *
     * Algorithm:
     * 1. Skip whitespace
     * 2. Parse sign
     * 3. Extract digits into long
     * 4. Clamp result to 32-bit range
     */
    public int myAtoiSimplified(String s) {
        // Skip leading whitespace
        int i = 0;
        while (i < s.length() && s.charAt(i) == ' ') {
            i++;
        }

        // Parse sign
        int sign = 1;
        if (i < s.length()) {
            if (s.charAt(i) == '+') {
                i++;
            } else if (s.charAt(i) == '-') {
                sign = -1;
                i++;
            }
        }

        // Extract digits using long to avoid overflow temporarily
        long result = 0;
        while (i < s.length() && Character.isDigit(s.charAt(i))) {
            result = result * 10 + (s.charAt(i) - '0');

            // Early termination if already out of bounds
            if (result > INT_MAX) {
                break;
            }
            i++;
        }

        result *= sign;

        // Clamp to 32-bit range
        if (result < INT_MIN) {
            return INT_MIN;
        }
        if (result > INT_MAX) {
            return INT_MAX;
        }

        return (int) result;
    }

    /**
     * Q3: Can we use a state machine approach?
     * A3: Yes, state machine for cleaner parsing. Time: O(n), Space: O(1)
     *
     * States: START, SIGN, NUMBER, END
     */
    public int myAtoiStateMachine(String s) {
        String state = "START";
        int sign = 1;
        long result = 0;

        for (char c : s.toCharArray()) {
            if (state.equals("START")) {
                if (c == ' ') {
                    continue;
                } else if (c == '+') {
                    state = "SIGN";
                } else if (c == '-') {
                    sign = -1;
                    state = "SIGN";
                } else if (Character.isDigit(c)) {
                    result = c - '0';
                    state = "NUMBER";
                } else {
                    return 0;
                }
            } else if (state.equals("SIGN")) {
                if (Character.isDigit(c)) {
                    result = c - '0';
                    state = "NUMBER";
                } else {
                    return 0;
                }
            } else if (state.equals("NUMBER")) {
                if (Character.isDigit(c)) {
                    result = result * 10 + (c - '0');
                } else {
                    break;
                }
            }
        }

        result *= sign;

        // Clamp to 32-bit range
        if (result < INT_MIN) {
            return INT_MIN;
        }
        if (result > INT_MAX) {
            return INT_MAX;
        }

        return (int) result;
    }

    /**
     * Q4: What are the edge cases we need to handle?
     *
     * A4: Edge cases:
     * 1. Empty string: "" -> 0
     * 2. Only whitespace: "   " -> 0
     * 3. No digits: "+abc" -> 0
     * 4. Leading zeros: "00123" -> 123
     * 5. Sign followed by spaces: "+ 42" -> 0 (space after sign)
     * 6. Words after number: "4193 with words" -> 4193
     * 7. Only sign: "+" -> 0, "-" -> 0
     * 8. Overflow positive: "9999999999" -> 2147483647
     * 9. Overflow negative: "-9999999999" -> -2147483648
     * 10. Decimal point: "3.14159" -> 3
     */

    /**
     * Q5: How to handle overflow detection efficiently?
     *
     * A5: Overflow detection strategies:
     * 1. Pre-check: Before result = result * 10 + digit
     *    - Check if result > INT_MAX / 10
     *    - Check if result == INT_MAX / 10 && digit > 7
     * 2. Post-check: After parsing, compare with bounds
     * 3. Use long: Parse into long, then clamp (simpler in Java)
     */

    /**
     * Q6: Difference between atoi and Integer.parseInt()?
     *
     * A6: Differences:
     * 1. atoi stops at first non-digit (after sign)
     * 2. Integer.parseInt() throws NumberFormatException on invalid input
     * 3. atoi returns 0 on error, parseInt throws exception
     * 4. atoi is more lenient ("4193 with words" -> 4193)
     * 5. parseInt is stricter (throws exception)
     */

    /**
     * Q7: How to test edge cases thoroughly?
     *
     * A7: Testing approach:
     * 1. Create comprehensive test suite with all edge cases
     * 2. Test empty strings, whitespace, signs
     * 3. Test overflow cases
     * 4. Test boundary values
     * 5. Test mixed content (digits with words)
     */

    public boolean testMyAtoi(String methodName) {
        String[][] testCases = {
            {"42", "42"},
            {"   -42", "-42"},
            {"4193 with words", "4193"},
            {"words and 987", "0"},
            {"-91283472332", String.valueOf(INT_MIN)},
            {"0", "0"},
            {"", "0"},
            {"   ", "0"},
            {"+123", "123"},
            {"+-42", "0"},
            {"00123", "123"},
            {"3.14159", "3"},
            {"+0 123", "0"},
            {"9999999999", String.valueOf(INT_MAX)},
            {"-9999999999", String.valueOf(INT_MIN)},
            {"+", "0"},
            {"-", "0"},
            {"+ 42", "0"},
            {"  +0 123", "0"},
            {"1", "1"},
            {"-1", "-1"},
            {"2147483647", "2147483647"},
            {"-2147483648", "-2147483648"},
        };

        int passed = 0;
        int failed = 0;

        System.out.println("Testing " + methodName + " approach:");
        for (String[] testCase : testCases) {
            String input = testCase[0];
            int expected = Integer.parseInt(testCase[1]);

            int result;
            switch (methodName) {
                case "manual":
                    result = myAtoiManual(input);
                    break;
                case "state_machine":
                    result = myAtoiStateMachine(input);
                    break;
                default:
                    result = myAtoiSimplified(input);
                    break;
            }

            if (result == expected) {
                passed++;
                System.out.println("  PASS: myAtoi(\"" + input + "\") = " + result);
            } else {
                failed++;
                System.out.println("  FAIL: myAtoi(\"" + input + "\") = " + result + " (expected " + expected + ")");
            }
        }

        System.out.println("\nResults: " + passed + " passed, " + failed + " failed");
        return failed == 0;
    }

    public static void main(String[] args) {
        StringToInteger solution = new StringToInteger();

        System.out.println("=".repeat(60));
        System.out.println("LeetCode 0008: String to Integer (atoi)");
        System.out.println("=".repeat(60));

        // Example 1
        String s1 = "42";
        System.out.println("\nExample 1:");
        System.out.println("Input: s = \"" + s1 + "\"");
        System.out.println("Output (Manual):        " + solution.myAtoiManual(s1));
        System.out.println("Output (Simplified):    " + solution.myAtoiSimplified(s1));
        System.out.println("Output (State Machine): " + solution.myAtoiStateMachine(s1));

        // Example 2
        String s2 = "   -42";
        System.out.println("\n" + "-".repeat(60));
        System.out.println("Example 2:");
        System.out.println("Input: s = \"" + s2 + "\"");
        System.out.println("Output (Manual):        " + solution.myAtoiManual(s2));
        System.out.println("Output (Simplified):    " + solution.myAtoiSimplified(s2));
        System.out.println("Output (State Machine): " + solution.myAtoiStateMachine(s2));

        // Example 3
        String s3 = "4193 with words";
        System.out.println("\n" + "-".repeat(60));
        System.out.println("Example 3:");
        System.out.println("Input: s = \"" + s3 + "\"");
        System.out.println("Output (Manual):        " + solution.myAtoiManual(s3));
        System.out.println("Output (Simplified):    " + solution.myAtoiSimplified(s3));
        System.out.println("Output (State Machine): " + solution.myAtoiStateMachine(s3));

        // Example 4 - Edge case
        String s4 = "words and 987";
        System.out.println("\n" + "-".repeat(60));
        System.out.println("Example 4 (Invalid):");
        System.out.println("Input: s = \"" + s4 + "\"");
        System.out.println("Output (Manual):        " + solution.myAtoiManual(s4));
        System.out.println("Output (Simplified):    " + solution.myAtoiSimplified(s4));
        System.out.println("Output (State Machine): " + solution.myAtoiStateMachine(s4));

        // Example 5 - Overflow
        String s5 = "-91283472332";
        System.out.println("\n" + "-".repeat(60));
        System.out.println("Example 5 (Overflow):");
        System.out.println("Input: s = \"" + s5 + "\"");
        System.out.println("Output (Manual):        " + solution.myAtoiManual(s5));
        System.out.println("Output (Simplified):    " + solution.myAtoiSimplified(s5));
        System.out.println("Output (State Machine): " + solution.myAtoiStateMachine(s5));

        // Comprehensive testing
        System.out.println("\n" + "=".repeat(60));
        System.out.println("Running Comprehensive Tests:");
        System.out.println("=".repeat(60) + "\n");
        solution.testMyAtoi("simplified");

        // Performance comparison
        System.out.println("\n" + "=".repeat(60));
        System.out.println("Performance Comparison:");
        System.out.println("=".repeat(60));

        String[] testStrings = {"42", "   -42", "4193 with words", "words and 987", "-91283472332"};
        int iterations = 100000;

        for (String s : testStrings) {
            long startTime = System.currentTimeMillis();
            for (int i = 0; i < iterations; i++) {
                solution.myAtoiManual(s);
            }
            long manualTime = System.currentTimeMillis() - startTime;

            startTime = System.currentTimeMillis();
            for (int i = 0; i < iterations; i++) {
                solution.myAtoiSimplified(s);
            }
            long simplifiedTime = System.currentTimeMillis() - startTime;

            startTime = System.currentTimeMillis();
            for (int i = 0; i < iterations; i++) {
                solution.myAtoiStateMachine(s);
            }
            long stateMachineTime = System.currentTimeMillis() - startTime;

            System.out.println("\nInput: \"" + s + "\" (" + iterations + " iterations)");
            System.out.println("  Manual approach:        " + manualTime + " ms");
            System.out.println("  Simplified approach:    " + simplifiedTime + " ms");
            System.out.println("  State Machine approach: " + stateMachineTime + " ms");
        }
    }
}
