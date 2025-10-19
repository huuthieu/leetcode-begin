import java.util.*;

/**
 * LeetCode Problem 0022: Generate Parentheses
 *
 * Problem:
 * Given n pairs of parentheses, write a function to generate all combinations
 * of well-formed parentheses.
 *
 * Examples:
 * 1. Input: n = 3, Output: ["((()))","(()())","(())()","()(())","()()()"]
 * 2. Input: n = 1, Output: ["()"]
 */

public class GenerateParentheses {

    // Q1: Backtracking approach (optimal)
    public static List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        backtrack(result, "", 0, 0, n);
        return result;
    }

    private static void backtrack(List<String> result, String current, int opens, int closes, int n) {
        if (current.length() == 2 * n) {
            result.add(current);
            return;
        }

        if (opens < n) {
            backtrack(result, current + "(", opens + 1, closes, n);
        }

        if (closes < opens) {
            backtrack(result, current + ")", opens, closes + 1, n);
        }
    }

    // Q2: Dynamic programming approach
    public static List<String> generateParenthesisDp(int n) {
        List<List<String>> dp = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            dp.add(new ArrayList<>());
        }

        dp.get(0).add("");

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                for (String left : dp.get(j)) {
                    for (String right : dp.get(i - 1 - j)) {
                        dp.get(i).add("(" + left + ")" + right);
                    }
                }
            }
        }

        return dp.get(n);
    }

    // Q3: Stack-based approach
    public static List<String> generateParenthesisStack(int n) {
        List<String> result = new ArrayList<>();
        Stack<Object[]> stack = new Stack<>();
        stack.push(new Object[]{"", 0, 0});

        while (!stack.isEmpty()) {
            Object[] state = stack.pop();
            String current = (String) state[0];
            int opens = (int) state[1];
            int closes = (int) state[2];

            if (opens == n && closes == n) {
                result.add(current);
                continue;
            }

            if (opens < n) {
                stack.push(new Object[]{current + "(", opens + 1, closes});
            }

            if (closes < opens) {
                stack.push(new Object[]{current + ")", opens, closes + 1});
            }
        }

        return result;
    }

    public static void main(String[] args) {
        System.out.println("Q1: generateParenthesis (Backtracking)");
        System.out.println("  Result: " + generateParenthesis(3));

        System.out.println("\nQ2: generateParenthesis (DP)");
        System.out.println("  Result: " + generateParenthesisDp(3));

        System.out.println("\nQ3: generateParenthesis (Stack)");
        System.out.println("  Result: " + generateParenthesisStack(3));
    }
}
