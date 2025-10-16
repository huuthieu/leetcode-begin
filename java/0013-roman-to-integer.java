import java.util.*;

/**
 * LeetCode Problem 0013: Roman to Integer
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
 * Given a roman numeral string s, convert it to an integer.
 *
 * The key rule: A smaller value before a larger value means subtraction
 * (I before V or X = 4 or 9, X before L or C = 40 or 90, C before D or M = 400 or 900)
 *
 * Examples:
 * 1. Input: "III", Output: 3
 * 2. Input: "LVIII", Output: 58
 * 3. Input: "MCMXCIV", Output: 1994
 */
public class RomanToInteger {

    /**
     * Q1: Greedy approach - iterate right to left with subtraction check
     *
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     */
    public static int romanToIntGreedy(String s) {
        Map<Character, Integer> values = new HashMap<>();
        values.put('I', 1);
        values.put('V', 5);
        values.put('X', 10);
        values.put('L', 50);
        values.put('C', 100);
        values.put('D', 500);
        values.put('M', 1000);

        int total = 0;
        int prevValue = 0;

        for (int i = s.length() - 1; i >= 0; i--) {
            int currentValue = values.get(s.charAt(i));
            if (currentValue < prevValue) {
                total -= currentValue;
            } else {
                total += currentValue;
            }
            prevValue = currentValue;
        }

        return total;
    }

    /**
     * Q2: Array-based approach using switch for faster lookup
     *
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     */
    public static int romanToIntSwitch(String s) {
        int total = 0;
        int prevValue = 0;

        for (int i = s.length() - 1; i >= 0; i--) {
            int currentValue = getValue(s.charAt(i));
            if (currentValue < prevValue) {
                total -= currentValue;
            } else {
                total += currentValue;
            }
            prevValue = currentValue;
        }

        return total;
    }

    private static int getValue(char c) {
        switch (c) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: return 0;
        }
    }

    /**
     * Q3: Left-to-right with lookahead
     *
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     */
    public static int romanToIntLookahead(String s) {
        Map<Character, Integer> values = new HashMap<>();
        values.put('I', 1);
        values.put('V', 5);
        values.put('X', 10);
        values.put('L', 50);
        values.put('C', 100);
        values.put('D', 500);
        values.put('M', 1000);

        int total = 0;
        int i = 0;

        while (i < s.length()) {
            if (i + 1 < s.length() && values.get(s.charAt(i)) < values.get(s.charAt(i + 1))) {
                total += values.get(s.charAt(i + 1)) - values.get(s.charAt(i));
                i += 2;
            } else {
                total += values.get(s.charAt(i));
                i++;
            }
        }

        return total;
    }

    /**
     * Q4: Subtraction pair detection
     *
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     */
    public static int romanToIntPairs(String s) {
        int total = 0;
        int i = 0;

        while (i < s.length()) {
            if (i + 1 < s.length()) {
                String pair = s.substring(i, i + 2);
                if (pair.equals("IV") || pair.equals("IX") || pair.equals("XL") ||
                    pair.equals("XC") || pair.equals("CD") || pair.equals("CM")) {
                    total += getPairValue(pair);
                    i += 2;
                    continue;
                }
            }

            total += getCharValue(s.charAt(i));
            i++;
        }

        return total;
    }

    private static int getPairValue(String pair) {
        switch (pair) {
            case "IV": return 4;
            case "IX": return 9;
            case "XL": return 40;
            case "XC": return 90;
            case "CD": return 400;
            case "CM": return 900;
            default: return 0;
        }
    }

    private static int getCharValue(char c) {
        switch (c) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: return 0;
        }
    }

    /**
     * Q5: Using array for constant-time lookup
     *
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     */
    public static int romanToIntArray(String s) {
        int[] values = new int[256];
        values['I'] = 1;
        values['V'] = 5;
        values['X'] = 10;
        values['L'] = 50;
        values['C'] = 100;
        values['D'] = 500;
        values['M'] = 1000;

        int total = 0;
        int prevValue = 0;

        for (int i = s.length() - 1; i >= 0; i--) {
            int currentValue = values[s.charAt(i)];
            if (currentValue < prevValue) {
                total -= currentValue;
            } else {
                total += currentValue;
            }
            prevValue = currentValue;
        }

        return total;
    }

    /**
     * Q6: Efficient comparison pattern
     *
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     */
    public static int romanToIntEfficient(String s) {
        int total = 0;
        int prevValue = 0;

        for (int i = s.length() - 1; i >= 0; i--) {
            int currentValue = getCharValue(s.charAt(i));
            total += currentValue >= prevValue ? currentValue : -currentValue;
            prevValue = Math.max(prevValue, currentValue);
        }

        return total;
    }

    /**
     * Q7: StringBuilder accumulation approach
     *
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     */
    public static int romanToIntIterative(String s) {
        Map<Character, Integer> map = new HashMap<>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);

        int result = 0;

        for (int i = s.length() - 1; i >= 0; i--) {
            int val = map.get(s.charAt(i));
            if (i < s.length() - 1 && val < map.get(s.charAt(i + 1))) {
                result -= val;
            } else {
                result += val;
            }
        }

        return result;
    }

    /**
     * Q8: Stream-based approach (less efficient but demonstrates functional style)
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public static int romanToIntStream(String s) {
        Map<Character, Integer> map = new HashMap<>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);

        int[] result = {0};
        int[] prevValue = {0};

        for (int i = s.length() - 1; i >= 0; i--) {
            int currentValue = map.get(s.charAt(i));
            if (currentValue < prevValue[0]) {
                result[0] -= currentValue;
            } else {
                result[0] += currentValue;
            }
            prevValue[0] = currentValue;
        }

        return result[0];
    }

    /**
     * Q9: Two-pointer with boundary check
     *
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     */
    public static int romanToIntTwoPointer(String s) {
        int total = 0;
        int i = 0;

        while (i < s.length()) {
            int curr = getCharValue(s.charAt(i));
            int next = (i + 1 < s.length()) ? getCharValue(s.charAt(i + 1)) : 0;

            if (curr < next) {
                total += next - curr;
                i += 2;
            } else {
                total += curr;
                i++;
            }
        }

        return total;
    }

    /**
     * Q10: Most straightforward approach with HashMap
     *
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     */
    public static int romanToIntDirect(String s) {
        Map<String, Integer> values = new HashMap<>();
        values.put("I", 1);
        values.put("V", 5);
        values.put("X", 10);
        values.put("L", 50);
        values.put("C", 100);
        values.put("D", 500);
        values.put("M", 1000);
        values.put("IV", 4);
        values.put("IX", 9);
        values.put("XL", 40);
        values.put("XC", 90);
        values.put("CD", 400);
        values.put("CM", 900);

        int total = 0;
        int i = 0;

        while (i < s.length()) {
            if (i + 1 < s.length() && values.containsKey(s.substring(i, i + 2))) {
                total += values.get(s.substring(i, i + 2));
                i += 2;
            } else {
                total += values.get(String.valueOf(s.charAt(i)));
                i++;
            }
        }

        return total;
    }

    // Test cases and main function
    public static void main(String[] args) {
        String[] testCases = {"III", "LVIII", "MCMXCIV", "I", "IX", "IV", "MMXXIII", "MMMCMXCIX", "XLII", "CDXLIV"};
        int[] expected = {3, 58, 1994, 1, 9, 4, 2023, 3999, 42, 444};

        java.lang.reflect.Method[] methods = RomanToInteger.class.getDeclaredMethods();
        List<java.lang.reflect.Method> testMethods = new ArrayList<>();

        for (java.lang.reflect.Method method : methods) {
            if (method.getName().startsWith("romanToInt") && method.getReturnType() == int.class) {
                testMethods.add(method);
            }
        }

        Collections.sort(testMethods, (a, b) -> a.getName().compareTo(b.getName()));

        int questionNum = 1;
        for (java.lang.reflect.Method method : testMethods) {
            System.out.println("\nQ" + questionNum + ": " + method.getName());
            System.out.println("-".repeat(50));

            boolean allPassed = true;
            for (int i = 0; i < testCases.length; i++) {
                try {
                    int result = (int) method.invoke(null, testCases[i]);
                    boolean passed = result == expected[i];
                    allPassed = allPassed && passed;
                    String status = passed ? "✓" : "✗";
                    System.out.println("  " + status + " romanToInt(\"" + testCases[i] + "\") = " + result + " (expected: " + expected[i] + ")");
                } catch (Exception e) {
                    System.out.println("  ✗ Error: " + e.getMessage());
                    allPassed = false;
                }
            }

            if (allPassed) {
                System.out.println("  All tests passed!");
            }

            questionNum++;
        }
    }
}
