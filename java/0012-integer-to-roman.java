import java.util.*;

/**
 * LeetCode Problem 0012: Integer to Roman
 *
 * Problem:
 * Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
 *
 * Symbol       Value
 * I             1
 * V             5
 * X             10
 * L             50
 * C             100
 * D             500
 * M             1000
 *
 * Given an integer, convert it to a roman numeral. You may assume the input is always between 1 and 3999.
 *
 * Examples:
 * 1. Input: 3, Output: "III"
 * 2. Input: 58, Output: "LVIII" (50 + 5 + 3 = LVIII)
 * 3. Input: 1994, Output: "MCMXCIV" (1000 + 900 + 90 + 4 = MCMXCIV)
 *
 * Constraints:
 * - 1 <= num <= 3999
 */

public class IntegerToRoman {

    // Q1: Greedy approach using value-symbol pairs in descending order
    public static String intToRomanGreedy(int num) {
        /**
         * Time Complexity: O(1) - maximum iterations is bounded (num can be at most 3999)
         * Space Complexity: O(1) - output string is at most 12 characters
         *
         * Approach: Start from largest values and greedily build the roman numeral string.
         */
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

        StringBuilder result = new StringBuilder();
        for (int i = 0; i < values.length; i++) {
            int count = num / values[i];
            if (count > 0) {
                for (int j = 0; j < count; j++) {
                    result.append(symbols[i]);
                }
                num -= values[i] * count;
            }
        }
        return result.toString();
    }

    // Q2: Using HashMap for value-symbol mapping
    public static String intToRomanHashMap(int num) {
        /**
         * Time Complexity: O(1)
         * Space Complexity: O(1)
         *
         * Using LinkedHashMap to preserve insertion order of value-symbol pairs.
         */
        LinkedHashMap<Integer, String> valToSym = new LinkedHashMap<>();
        valToSym.put(1000, "M");
        valToSym.put(900, "CM");
        valToSym.put(500, "D");
        valToSym.put(400, "CD");
        valToSym.put(100, "C");
        valToSym.put(90, "XC");
        valToSym.put(50, "L");
        valToSym.put(40, "XL");
        valToSym.put(10, "X");
        valToSym.put(9, "IX");
        valToSym.put(5, "V");
        valToSym.put(4, "IV");
        valToSym.put(1, "I");

        StringBuilder result = new StringBuilder();
        for (Map.Entry<Integer, String> entry : valToSym.entrySet()) {
            int value = entry.getKey();
            String symbol = entry.getValue();
            while (num >= value) {
                result.append(symbol);
                num -= value;
            }
        }
        return result.toString();
    }

    // Q3: Using while loop with single loop
    public static String intToRomanSingleLoop(int num) {
        /**
         * Time Complexity: O(1)
         * Space Complexity: O(1)
         *
         * Single loop with pointer advancement for cleaner code.
         */
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

        StringBuilder result = new StringBuilder();
        int index = 0;

        while (num > 0) {
            if (num >= values[index]) {
                result.append(symbols[index]);
                num -= values[index];
            } else {
                index++;
            }
        }
        return result.toString();
    }

    // Q4: Using repeat method for cleaner append
    public static String intToRomanRepeat(int num) {
        /**
         * Time Complexity: O(1)
         * Space Complexity: O(1)
         *
         * Use String.repeat() for multiple appends (Java 11+).
         */
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

        StringBuilder result = new StringBuilder();
        for (int i = 0; i < values.length; i++) {
            int count = num / values[i];
            if (count > 0) {
                result.append(symbols[i].repeat(count));
                num -= values[i] * count;
            }
        }
        return result.toString();
    }

    // Q5: Using arrays of digit mappings for each place value
    public static String intToRomanGrouped(int num) {
        /**
         * Time Complexity: O(1)
         * Space Complexity: O(1)
         *
         * Group the values by place value (thousands, hundreds, tens, ones).
         */
        String[] thousands = {"", "M", "MM", "MMM"};
        String[] hundreds = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        String[] tens = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        String[] ones = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};

        return thousands[num / 1000] +
               hundreds[(num % 1000) / 100] +
               tens[(num % 100) / 10] +
               ones[num % 10];
    }

    // Q6: Using helper method for repeated symbol appending
    public static String intToRomanHelper(int num) {
        /**
         * Time Complexity: O(1)
         * Space Complexity: O(1)
         *
         * Extract symbol appending logic into a helper method.
         */
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

        StringBuilder result = new StringBuilder();
        for (int i = 0; i < values.length; i++) {
            result.append(repeatSymbol(symbols[i], num / values[i]));
            num %= values[i];
        }
        return result.toString();
    }

    private static String repeatSymbol(String symbol, int count) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < count; i++) {
            sb.append(symbol);
        }
        return sb.toString();
    }

    // Q7: Using array of Pair objects for cleaner iteration
    public static String intToRomanPair(int num) {
        /**
         * Time Complexity: O(1)
         * Space Complexity: O(1)
         *
         * Use a list of pairs for more organized data structure.
         */
        List<int[]> pairs = Arrays.asList(
            new int[]{1000, 'M'}, new int[]{900, 'C'}, new int[]{500, 'D'}, new int[]{400, 'C'},
            new int[]{100, 'C'}, new int[]{90, 'X'}, new int[]{50, 'L'}, new int[]{40, 'X'},
            new int[]{10, 'X'}, new int[]{9, 'I'}, new int[]{5, 'V'}, new int[]{4, 'I'}, new int[]{1, 'I'}
        );

        String[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

        StringBuilder result = new StringBuilder();
        for (int i = 0; i < values.length; i++) {
            while (num >= values[i]) {
                result.append(symbols[i]);
                num -= values[i];
            }
        }
        return result.toString();
    }

    // Q8: Using do-while with explicit index advancement
    public static String intToRomanDoWhile(int num) {
        /**
         * Time Complexity: O(1)
         * Space Complexity: O(1)
         *
         * Alternative loop structure using do-while.
         */
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

        StringBuilder result = new StringBuilder();
        int index = 0;

        do {
            if (num >= values[index]) {
                result.append(symbols[index]);
                num -= values[index];
            } else {
                index++;
            }
        } while (num > 0 && index < values.length);

        return result.toString();
    }

    // Q9: Using recursive approach
    public static String intToRomanRecursive(int num) {
        /**
         * Time Complexity: O(1)
         * Space Complexity: O(1) - recursion depth is bounded
         *
         * Convert by recursively handling the largest value first.
         */
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

        return intToRomanRecursiveHelper(num, 0, new StringBuilder(), values, symbols).toString();
    }

    private static StringBuilder intToRomanRecursiveHelper(int num, int index, StringBuilder result,
                                                           int[] values, String[] symbols) {
        if (num == 0 || index >= values.length) {
            return result;
        }

        if (num >= values[index]) {
            result.append(symbols[index]);
            return intToRomanRecursiveHelper(num - values[index], index, result, values, symbols);
        } else {
            return intToRomanRecursiveHelper(num, index + 1, result, values, symbols);
        }
    }

    // Q10: Optimized with early exit
    public static String intToRomanOptimized(int num) {
        /**
         * Time Complexity: O(1)
         * Space Complexity: O(1)
         *
         * Optimized version with early exit condition when num becomes 0.
         */
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

        StringBuilder result = new StringBuilder();

        for (int i = 0; i < values.length && num > 0; i++) {
            while (num >= values[i]) {
                result.append(symbols[i]);
                num -= values[i];
            }
        }

        return result.toString();
    }

    public static void main(String[] args) {
        int[][] testCases = {
            {3, 0},           // III
            {58, 1},          // LVIII
            {1994, 2},        // MCMXCIV
            {1, 3},           // I
            {9, 4},           // IX
            {27, 5},          // XXVII
            {49, 6},          // XLIX
            {3999, 7},        // MMMCMXCIX
            {444, 8},         // CDXLIV
            {2023, 9}         // MMXXIII
        };

        String[] expectedResults = {
            "III", "LVIII", "MCMXCIV", "I", "IX",
            "XXVII", "XLIX", "MMMCMXCIX", "CDXLIV", "MMXXIII"
        };

        java.lang.reflect.Method[] methods = IntegerToRoman.class.getDeclaredMethods();
        java.util.Arrays.sort(methods, (a, b) -> a.getName().compareTo(b.getName()));

        int questionNum = 1;
        for (java.lang.reflect.Method method : methods) {
            if (!method.getName().startsWith("intToRoman") ||
                method.getName().contains("Helper") ||
                method.getName().contains("Recursive")) {
                continue;
            }

            System.out.println("\nQ" + questionNum + ": " + method.getName());
            System.out.println("-".repeat(50));

            boolean allPassed = true;
            for (int i = 0; i < testCases.length; i++) {
                int num = testCases[i][0];
                String expected = expectedResults[i];

                try {
                    String result = (String) method.invoke(null, num);
                    boolean passed = result.equals(expected);
                    allPassed = allPassed && passed;
                    String status = passed ? "✓" : "✗";
                    System.out.println("  " + status + " intToRoman(" + num + ") = " + result +
                                     " (expected: " + expected + ")");
                } catch (Exception e) {
                    System.out.println("  ✗ Error testing " + method.getName());
                    allPassed = false;
                }
            }

            if (allPassed) {
                System.out.println("  All tests passed!");
            }
            questionNum++;
        }

        // Special testing for recursive method
        System.out.println("\nQ9: intToRomanRecursive");
        System.out.println("-".repeat(50));
        boolean recursivePassed = true;
        for (int i = 0; i < testCases.length; i++) {
            int num = testCases[i][0];
            String expected = expectedResults[i];
            String result = intToRomanRecursive(num);
            boolean passed = result.equals(expected);
            recursivePassed = recursivePassed && passed;
            String status = passed ? "✓" : "✗";
            System.out.println("  " + status + " intToRoman(" + num + ") = " + result +
                             " (expected: " + expected + ")");
        }
        if (recursivePassed) {
            System.out.println("  All tests passed!");
        }
    }
}
