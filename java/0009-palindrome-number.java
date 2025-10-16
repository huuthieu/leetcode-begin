/**
 * LeetCode Problem 0009: Palindrome Number
 *
 * Problem:
 * Given an integer x, return true if x is a palindrome, and false otherwise.
 *
 * A palindrome is a number that reads the same forwards and backwards.
 * Negative numbers are NOT palindromes.
 * Numbers ending with 0 are only palindromes if the entire number is just 0.
 *
 * Examples:
 * - 121 → true (reads the same forwards and backwards)
 * - -121 → false (negative numbers are not palindromes)
 * - 10 → false (ends with 0 but is not 0)
 * - 0 → true (single digit)
 * - 1001 → true (reads the same forwards and backwards)
 *
 * Constraints:
 * - -2^31 <= x <= 2^31 - 1
 * - Try not to use extra space (O(1) space complexity)
 */

public class PalindromeNumber {

    // Q1: What is the brute force approach?
    // A1: Convert the number to a string and check if it equals its reverse.
    // Time Complexity: O(log n) - number of digits
    // Space Complexity: O(log n) - string storage
    /**
     * Brute force approach using string conversion.
     * Simple but uses extra space for string storage.
     */
    public static boolean isPalindromeString(int x) {
        if (x < 0) {
            return false;
        }

        String s = String.valueOf(x);
        String reversed = new StringBuilder(s).reverse().toString();
        return s.equals(reversed);
    }

    // Q2: How can we solve this without converting to string?
    // A2: Reverse the number mathematically and compare with original.
    // Time Complexity: O(log n)
    // Space Complexity: O(1)
    /**
     * Mathematical approach: reverse the entire number.
     * No string conversion needed, using only integer operations.
     */
    public static boolean isPalindromeReverse(int x) {
        if (x < 0) {
            return false;
        }

        int original = x;
        long reversedNum = 0;

        while (x > 0) {
            int digit = x % 10;
            reversedNum = reversedNum * 10 + digit;
            x /= 10;
        }

        return original == reversedNum;
    }

    // Q3: Can we optimize further by reversing only half the number?
    // A3: Yes! We can reverse only the second half and compare.
    // This prevents potential overflow and is more efficient.
    // Time Complexity: O(log n)
    // Space Complexity: O(1)
    /**
     * Optimized approach: reverse only the second half of the number.
     * More efficient and elegant than reversing the entire number.
     *
     * Idea: We keep reversing the second half until it becomes
     * >= the first half. Then we can compare.
     */
    public static boolean isPalindromeHalfReverse(int x) {
        // Negative numbers are not palindromes
        if (x < 0) {
            return false;
        }

        // Single digit numbers are palindromes
        if (x < 10) {
            return true;
        }

        // Numbers ending with 0 (except 0 itself) are not palindromes
        if (x % 10 == 0) {
            return false;
        }

        int reversedHalf = 0;

        // Reverse second half until it's >= first half
        while (x > reversedHalf) {
            reversedHalf = reversedHalf * 10 + x % 10;
            x /= 10;
        }

        // For even length: x == reversedHalf
        // For odd length: x == reversedHalf / 10 (middle digit ignored)
        return x == reversedHalf || x == reversedHalf / 10;
    }

    // Q4: What are the edge cases we need to handle?
    // A4: Negative numbers, trailing zeros, single digits, and potential overflow.
    /**
     * Test various edge cases.
     */
    public static void testEdgeCases() {
        int[][] testCases = {
            {121, 1},      // true
            {-121, 0},     // false
            {10, 0},       // false
            {0, 1},        // true
            {1, 1},        // true
            {1001, 1},     // true
            {1221, 1},     // true
            {12321, 1},    // true
            {100, 0},      // false
            {2147483647, 0} // false - INT_MAX
        };

        for (int[] testCase : testCases) {
            int num = testCase[0];
            int expected = testCase[1];
            boolean result = isPalindromeHalfReverse(num);
            String status = (result == (expected == 1)) ? "✓" : "✗";
            System.out.printf("%s isPalindrome(%d) = %b (expected %s)%n",
                status, num, result, expected == 1 ? "true" : "false");
        }
    }

    // Q5: How would we solve this using a two-pointer approach on digits?
    // A5: Extract digits into an array and use two pointers from both ends.
    // Time Complexity: O(log n)
    // Space Complexity: O(log n) - for storing digits
    /**
     * Two-pointer approach: extract digits and compare from both ends.
     * Educational approach that clearly shows the palindrome check.
     */
    public static boolean isPalindromeTwoPointer(int x) {
        if (x < 0) {
            return false;
        }

        // Extract digits
        java.util.List<Integer> digits = new java.util.ArrayList<>();
        int temp = x;
        while (temp > 0) {
            digits.add(temp % 10);
            temp /= 10;
        }

        // Reverse to get correct order
        java.util.Collections.reverse(digits);

        // Compare from both ends
        int left = 0, right = digits.size() - 1;
        while (left < right) {
            if (!digits.get(left).equals(digits.get(right))) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }

    // Q6: What if we compare with the reversed number directly?
    // A6: This is similar to Q2 but emphasizes the comparison approach.
    /**
     * Direct comparison: create a fully reversed number and compare.
     * Clear and straightforward approach.
     */
    public static boolean isPalindromeDirectComparison(int x) {
        if (x < 0) {
            return false;
        }

        // Handle trailing zeros
        if (x != 0 && x % 10 == 0) {
            return false;
        }

        long reversedNum = 0;
        int original = x;

        while (x > 0) {
            reversedNum = reversedNum * 10 + x % 10;
            x /= 10;
        }

        return original == reversedNum;
    }

    // Q7: How can we handle potential overflow concerns?
    // A7: By reversing only half the number, we avoid overflow issues.
    /**
     * Handles overflow by never creating a fully reversed number
     * that exceeds the range of input numbers.
     *
     * This is the same as the half-reverse approach (Q3),
     * which naturally prevents overflow.
     */
    public static boolean isPalindromeNoOverflow(int x) {
        if (x < 0 || (x != 0 && x % 10 == 0)) {
            return false;
        }

        if (x < 10) {
            return true;
        }

        int reversedHalf = 0;

        while (x > reversedHalf) {
            reversedHalf = reversedHalf * 10 + x % 10;
            x /= 10;
        }

        return x == reversedHalf || x == reversedHalf / 10;
    }

    // Q8: What is the space-time tradeoff analysis?
    // A8: Comparing different approaches:
    /**
     * Space-Time Tradeoff Analysis:
     *
     * Approach 1 - String Conversion:
     *   Pros: Easy to understand and implement
     *   Cons: Uses extra space O(log n), slower due to string operations
     *
     * Approach 2 - Full Reverse:
     *   Pros: Uses O(1) space, purely mathematical
     *   Cons: Potential overflow when multiplying
     *
     * Approach 3 - Half Reverse (BEST):
     *   Pros: O(1) space, no overflow risk, most efficient
     *   Cons: Slightly more complex logic to understand
     */
    public static void spaceTimeTradeoffAnalysis() {
        System.out.println("See method documentation for analysis.");
    }

    // Q9: How do string comparison and mathematical approaches compare?
    // A9: Both work, but mathematical approach is more elegant for numbers.
    /**
     * String vs Mathematical Comparison:
     *
     * String Approach:
     * - Intuitive: palindrome = string equals reversed string
     * - Uses StringBuilder for efficient reversal
     * - Downside: creates string objects
     *
     * Mathematical Approach:
     * - More efficient: works directly with digits
     * - Language-agnostic: doesn't rely on string manipulation
     * - More elegant for pure number problems
     *
     * For interviews, prefer mathematical when possible.
     */
    public static void stringVsMathematicalComparison() {
        System.out.println("See method documentation for comparison.");
    }

    // Q10: What are variations of this problem?
    // A10: String palindromes, checking only alphanumeric, ignoring case, etc.
    /**
     * Variation: Check if a string is a palindrome,
     * ignoring non-alphanumeric characters and case.
     */
    public static boolean isPalindromeString(String s) {
        StringBuilder filtered = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                filtered.append(Character.toLowerCase(c));
            }
        }

        String str = filtered.toString();
        return str.equals(new StringBuilder(str).reverse().toString());
    }

    /**
     * Variation: Check if a digit string is a palindrome.
     */
    public static boolean isPalindromeDigitString(String s) {
        return s.equals(new StringBuilder(s).reverse().toString());
    }

    /**
     * Generic variation: Apply custom filter before palindrome check.
     */
    public static boolean isPalindromeCustom(String s, java.util.function.Predicate<Character> filterFunc) {
        StringBuilder filtered = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (filterFunc.test(c)) {
                filtered.append(c);
            }
        }

        String str = filtered.toString();
        return str.equals(new StringBuilder(str).reverse().toString());
    }

    /**
     * Main method: Run all tests and demonstrations.
     */
    public static void main(String[] args) {
        System.out.println("=" .repeat(60));
        System.out.println("LeetCode 0009: Palindrome Number");
        System.out.println("=" .repeat(60));

        System.out.println("\n--- Edge Case Testing ---");
        testEdgeCases();

        System.out.println("\n--- Comparing Different Approaches ---");
        int[] testNums = {121, -121, 10, 0, 1221, 12321};

        for (int num : testNums) {
            boolean r1 = isPalindromeString(num);
            boolean r2 = isPalindromeReverse(num);
            boolean r3 = isPalindromeHalfReverse(num);
            boolean r4 = isPalindromeTwoPointer(num);

            String match = (r1 == r2 && r2 == r3 && r3 == r4) ? "✓" : "✗";
            System.out.printf("%s %d: String=%b, Reverse=%b, HalfReverse=%b, TwoPointer=%b%n",
                match, num, r1, r2, r3, r4);
        }

        System.out.println("\n--- String Palindrome Variations ---");
        String[] testStrings = {
            "A man, a plan, a canal: Panama",
            "race a car",
            " ",
            "0P"
        };

        for (String testStr : testStrings) {
            boolean result = isPalindromeString(testStr);
            System.out.printf("'%s' → %b%n", testStr, result);
        }
    }
}
