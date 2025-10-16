import java.util.*;

/**
 * LeetCode Problem 0020: Valid Parentheses
 *
 * Problem:
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
 * determine if the input string is valid.
 *
 * An input string is valid if:
 * 1. Open brackets must be closed by the same type of brackets.
 * 2. Open brackets must be closed in the correct order.
 *
 * Examples:
 * 1. Input: s = "()", Output: true
 * 2. Input: s = "()[]{}", Output: true
 * 3. Input: s = "(]", Output: false
 */
public class ValidParentheses {

    /**
     * Q1: Stack-based approach (optimal)
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public static boolean isValidStack(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> mapping = new HashMap<>();
        mapping.put(')', '(');
        mapping.put('}', '{');
        mapping.put(']', '[');

        for (char c : s.toCharArray()) {
            if (mapping.containsKey(c)) {  // Closing bracket
                if (stack.isEmpty() || stack.pop() != mapping.get(c)) {
                    return false;
                }
            } else {  // Opening bracket
                stack.push(c);
            }
        }

        return stack.isEmpty();
    }

    /**
     * Q2: Using Deque
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public static boolean isValidDeque(String s) {
        Deque<Character> stack = new LinkedList<>();
        Map<Character, Character> mapping = new HashMap<>();
        mapping.put(')', '(');
        mapping.put('}', '{');
        mapping.put(']', '[');

        for (char c : s.toCharArray()) {
            if (mapping.containsKey(c)) {
                if (stack.isEmpty() || stack.pop() != mapping.get(c)) {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }

        return stack.isEmpty();
    }

    /**
     * Q3: With length check first
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public static boolean isValidLengthCheck(String s) {
        if (s.length() % 2 != 0) return false;

        Stack<Character> stack = new Stack<>();
        Map<Character, Character> mapping = new HashMap<>();
        mapping.put(')', '(');
        mapping.put('}', '{');
        mapping.put(']', '[');

        for (char c : s.toCharArray()) {
            if (mapping.containsKey(c)) {
                if (stack.isEmpty() || stack.pop() != mapping.get(c)) {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }

        return stack.isEmpty();
    }

    /**
     * Q4: Using array instead of Stack
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public static boolean isValidArray(String s) {
        if (s.length() % 2 != 0) return false;

        char[] stack = new char[s.length()];
        int top = 0;
        Map<Character, Character> mapping = new HashMap<>();
        mapping.put(')', '(');
        mapping.put('}', '{');
        mapping.put(']', '[');

        for (char c : s.toCharArray()) {
            if (mapping.containsKey(c)) {
                if (top == 0 || stack[top - 1] != mapping.get(c)) {
                    return false;
                }
                top--;
            } else {
                stack[top++] = c;
            }
        }

        return top == 0;
    }

    /**
     * Q5: Using switch for character matching
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public static boolean isValidSwitch(String s) {
        if (s.length() % 2 != 0) return false;

        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            switch (c) {
                case ')':
                    if (stack.isEmpty() || stack.pop() != '(') return false;
                    break;
                case '}':
                    if (stack.isEmpty() || stack.pop() != '{') return false;
                    break;
                case ']':
                    if (stack.isEmpty() || stack.pop() != '[') return false;
                    break;
                default:
                    stack.push(c);
            }
        }

        return stack.isEmpty();
    }

    /**
     * Q6: Using string contains for matching
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public static boolean isValidStringContains(String s) {
        Stack<Character> stack = new Stack<>();
        String opens = "({[";
        String closes = ")}]";

        for (char c : s.toCharArray()) {
            if (opens.indexOf(c) >= 0) {
                stack.push(c);
            } else {
                if (stack.isEmpty() || opens.indexOf(stack.pop()) != closes.indexOf(c)) {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }

    /**
     * Q7: Early termination with checks
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public static boolean isValidEarlyExit(String s) {
        if (s.length() % 2 != 0) return false;

        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else if (c == ')') {
                if (stack.isEmpty() || stack.pop() != '(') return false;
            } else if (c == '}') {
                if (stack.isEmpty() || stack.pop() != '{') return false;
            } else if (c == ']') {
                if (stack.isEmpty() || stack.pop() != '[') return false;
            }
        }

        return stack.isEmpty();
    }

    /**
     * Q8: Optimized with HashMap initialization
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public static boolean isValidOptimized(String s) {
        if (s.length() % 2 != 0) return false;

        Stack<Character> stack = new Stack<>();
        int[] map = new int[256];
        map[')'] = '(';
        map['}'] = '{';
        map[']'] = '[';

        for (char c : s.toCharArray()) {
            if (c == ')' || c == '}' || c == ']') {
                if (stack.isEmpty() || stack.pop() != (char) map[c]) {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }

        return stack.isEmpty();
    }

    /**
     * Q9: Replacing pairs iteratively
     *
     * Time Complexity: O(n^2)
     * Space Complexity: O(n)
     */
    public static boolean isValidReplace(String s) {
        while (s.contains("()") || s.contains("[]") || s.contains("{}")) {
            s = s.replace("()", "").replace("[]", "").replace("{}", "");
        }
        return s.isEmpty();
    }

    /**
     * Q10: Clean and simple
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public static boolean isValidClean(String s) {
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) return false;

                char top = stack.pop();
                if ((c == ')' && top != '(') ||
                    (c == ']' && top != '[') ||
                    (c == '}' && top != '{')) {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }

    // Test cases and main function
    public static void main(String[] args) {
        String[] testCases = {
                "()",
                "()[]{}",
                "(]",
                "([)]",
                "{[]}",
                "",
                "(",
                ")",
                "(((",
                ")))",
                "({[]})",
                "({[}])"
        };
        boolean[] expected = {
                true, true, false, false, true, true, false, false, false, false, true, false
        };

        java.lang.reflect.Method[] methods = ValidParentheses.class.getDeclaredMethods();
        List<java.lang.reflect.Method> testMethods = new ArrayList<>();

        for (java.lang.reflect.Method method : methods) {
            if (method.getName().startsWith("isValid") &&
                method.getReturnType() == boolean.class) {
                testMethods.add(method);
            }
        }

        Collections.sort(testMethods, Comparator.comparing(java.lang.reflect.Method::getName));

        int questionNum = 1;
        for (java.lang.reflect.Method method : testMethods) {
            System.out.println("\nQ" + questionNum + ": " + method.getName());
            System.out.println("-".repeat(70));

            boolean allPassed = true;
            for (int i = 0; i < testCases.length; i++) {
                try {
                    boolean result = (boolean) method.invoke(null, testCases[i]);
                    boolean passed = result == expected[i];
                    allPassed = allPassed && passed;
                    String status = passed ? "✓" : "✗";
                    System.out.println("  " + status + " isValid(\"" + testCases[i] +
                        "\") = " + result + " (expected: " + expected[i] + ")");
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
