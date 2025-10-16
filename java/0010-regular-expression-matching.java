/**
 * LeetCode 0010: Regular Expression Matching
 *
 * Problem Statement:
 * Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
 * - '.' Matches any single character.
 * - '*' Matches zero or more of the preceding element.
 * The matching should cover the entire input string (not partial).
 *
 * Example 1:
 * Input: s = "aa", p = "a"
 * Output: false
 * Explanation: "a" does not match the entire string "aa".
 *
 * Example 2:
 * Input: s = "aa", p = "a*"
 * Output: true
 *
 * Example 3:
 * Input: s = "aa", p = ".*"
 * Output: true
 * Explanation: ".*" means "zero or more (*) of any character (.)".
 *
 * Example 4:
 * Input: s = "ab", p = ".*"
 * Output: true
 *
 * Example 5:
 * Input: s = "aab", p = "c*a*b"
 * Output: true
 *
 * Constraints:
 * - 1 <= s.length <= 20
 * - 1 <= p.length <= 30
 * - s contains only lowercase English letters.
 * - p contains only lowercase English letters, '.', and '*'.
 * - For each appearance of the character '*', there will be a previous character in the pattern.
 */

import java.util.*;

public class RegularExpressionMatching {

    // Q1: What's the brute force approach?
    // A1: Try all possible matches recursively. Time: O(2^(m+n)), Space: O(m+n)
    public boolean isMatchBruteForce(String s, String p) {
        if (p.isEmpty()) {
            return s.isEmpty();
        }

        // Check if first character matches
        boolean firstMatch = !s.isEmpty() && (p.charAt(0) == s.charAt(0) || p.charAt(0) == '.');

        // If pattern has at least 2 characters and second is '*'
        if (p.length() >= 2 && p.charAt(1) == '*') {
            // Either match zero occurrences or one and recurse
            return (isMatchBruteForce(s, p.substring(2)) ||
                    (firstMatch && isMatchBruteForce(s.substring(1), p)));
        } else {
            // Move both pointers if first character matches
            return firstMatch && isMatchBruteForce(s.substring(1), p.substring(1));
        }
    }

    // Q2: How can we optimize with memoization?
    // A2: Cache results for (s_index, p_index) pairs. Time: O(m*n), Space: O(m*n)
    public boolean isMatchMemo(String s, String p) {
        Map<String, Boolean> memo = new HashMap<>();
        return dp(s, p, 0, 0, memo);
    }

    private boolean dp(String s, String p, int i, int j, Map<String, Boolean> memo) {
        String key = i + "," + j;
        if (memo.containsKey(key)) {
            return memo.get(key);
        }

        boolean result;

        // Base case: if pattern is empty
        if (j == p.length()) {
            result = i == s.length();
        } else {
            // Check if first character matches
            boolean firstMatch = i < s.length() && (p.charAt(j) == s.charAt(i) || p.charAt(j) == '.');

            // If next character is '*'
            if (j + 1 < p.length() && p.charAt(j + 1) == '*') {
                // Either skip the current pattern (match zero) or match current char
                result = dp(s, p, i, j + 2, memo) || (firstMatch && dp(s, p, i + 1, j, memo));
            } else {
                // Normal character matching
                result = firstMatch && dp(s, p, i + 1, j + 1, memo);
            }
        }

        memo.put(key, result);
        return result;
    }

    // Q3: How can we solve this with bottom-up dynamic programming?
    // A3: Build a table where dp[i][j] means s[0:i] matches p[0:j]. Time: O(m*n), Space: O(m*n)
    public boolean isMatchDP(String s, String p) {
        int m = s.length();
        int n = p.length();

        // dp[i][j] represents if s[0:i] matches p[0:j]
        boolean[][] dp = new boolean[m + 1][n + 1];

        // Empty string matches empty pattern
        dp[0][0] = true;

        // Handle patterns like a*, a*b*, a*b*c* which can match empty string
        for (int j = 2; j <= n; j++) {
            if (p.charAt(j - 1) == '*') {
                dp[0][j] = dp[0][j - 2];
            }
        }

        // Fill the dp table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p.charAt(j - 1) == '*') {
                    // '*' can match zero occurrences (take from dp[i][j-2])
                    // or one or more occurrences (take from dp[i-1][j])
                    dp[i][j] = dp[i][j - 2] ||
                               (dp[i - 1][j] && (p.charAt(j - 2) == s.charAt(i - 1) || p.charAt(j - 2) == '.'));
                } else {
                    // Regular character or '.'
                    dp[i][j] = dp[i - 1][j - 1] &&
                               (p.charAt(j - 1) == s.charAt(i - 1) || p.charAt(j - 1) == '.');
                }
            }
        }

        return dp[m][n];
    }

    // Q4: Can we optimize the space complexity?
    // A4: Yes, use two 1D arrays instead of 2D. Time: O(m*n), Space: O(n)
    public boolean isMatchSpaceOptimized(String s, String p) {
        int m = s.length();
        int n = p.length();

        boolean[] prev = new boolean[n + 1];
        boolean[] curr = new boolean[n + 1];

        // Empty string matches empty pattern
        prev[0] = true;

        // Handle patterns like a*, a*b*
        for (int j = 2; j <= n; j++) {
            if (p.charAt(j - 1) == '*') {
                prev[j] = prev[j - 2];
            }
        }

        // Fill the table
        for (int i = 1; i <= m; i++) {
            curr[0] = false;  // s[0:i] can never match empty pattern

            for (int j = 1; j <= n; j++) {
                if (p.charAt(j - 1) == '*') {
                    curr[j] = curr[j - 2] ||
                              (prev[j] && (p.charAt(j - 2) == s.charAt(i - 1) || p.charAt(j - 2) == '.'));
                } else {
                    curr[j] = prev[j - 1] &&
                              (p.charAt(j - 1) == s.charAt(i - 1) || p.charAt(j - 1) == '.');
                }
            }

            boolean[] temp = prev;
            prev = curr;
            curr = temp;
        }

        return prev[n];
    }

    // Q5: What if we need to match partial strings?
    // A5: Modify DP to check if pattern matches any substring
    public boolean isMatchPartial(String s, String p) {
        int m = s.length();
        int n = p.length();

        boolean[][] dp = new boolean[m + 1][n + 1];

        dp[0][0] = true;

        for (int j = 2; j <= n; j++) {
            if (p.charAt(j - 1) == '*') {
                dp[0][j] = dp[0][j - 2];
            }
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p.charAt(j - 1) == '*') {
                    dp[i][j] = dp[i][j - 2] ||
                               (dp[i - 1][j] && (p.charAt(j - 2) == s.charAt(i - 1) || p.charAt(j - 2) == '.'));
                } else {
                    dp[i][j] = dp[i - 1][j - 1] &&
                               (p.charAt(j - 1) == s.charAt(i - 1) || p.charAt(j - 1) == '.');
                }
            }
        }

        // Check if pattern matches any substring
        for (int i = 0; i <= m; i++) {
            if (dp[i][n]) {
                return true;
            }
        }
        return false;
    }

    // Q6: How do we handle edge cases?
    // A6: Empty string, empty pattern, only '*', only '.'
    public boolean isMatchWithValidation(String s, String p) {
        if (p == null || p.isEmpty()) {
            return s == null || s.isEmpty();
        }
        return isMatchDP(s, p);
    }

    // Q7: What's the time and space complexity analysis?
    /**
     * A7:
     * Brute Force: Time O(2^(m+n)), Space O(m+n) - exponential, impractical
     * Memoization: Time O(m*n), Space O(m*n) - each state computed once
     * DP (2D): Time O(m*n), Space O(m*n) - same as memoization
     * DP (1D): Time O(m*n), Space O(n) - optimized space
     */

    // Q8: How would you trace through an example?
    /**
     * A8: For s = "aab", p = "c*a*b"
     * dp[0][0] = true (empty matches empty)
     * dp[0][1] = false (c can't match empty)
     * dp[0][2] = true (c* can match empty - zero c's)
     * dp[0][3] = false
     * dp[0][4] = true (c*a* can match empty - zero c's and zero a's)
     * dp[0][5] = false
     * ...
     * Then fill row by row checking character matches and '*' patterns
     * Final answer: dp[3][5] = true
     */

    // Q9: What are common variations of this problem?
    /**
     * A9:
     * - Wildcard Matching (with ? and *)
     * - Simplified regex (only specific patterns)
     * - Match with groups
     * - Match with backreferences
     * - Pattern matching in multiple strings
     */

    // Q10: How would you implement without using built-in regex?
    /**
     * A10: This solution already doesn't use built-in regex.
     * It manually implements a regex engine using dynamic programming.
     * This is often asked to test if candidates understand DP and pattern matching.
     */

    public static void main(String[] args) {
        RegularExpressionMatching solution = new RegularExpressionMatching();

        // Test cases
        String[] testStrings = {"aa", "aa", "ab", "aab", "mississippi", "", "a", "aaa", "aaaa"};
        String[] testPatterns = {"a", "a*", ".*", "c*a*b", "mis*is*p*.", "", ".", "a*a*a*a*a*b", "***a"};
        boolean[] expected = {false, true, true, true, false, true, true, false, false};

        System.out.println("Testing all approaches:\n");

        for (int i = 0; i < testStrings.length; i++) {
            String s = testStrings[i];
            String p = testPatterns[i];
            boolean exp = expected[i];

            boolean dpResult = solution.isMatchDP(s, p);
            boolean memoResult = solution.isMatchMemo(s, p);
            boolean spaceOptResult = solution.isMatchSpaceOptimized(s, p);

            System.out.println("s = \"" + s + "\", p = \"" + p + "\"");
            System.out.println("Expected: " + exp + ", DP: " + dpResult +
                             ", Memo: " + memoResult + ", Space Opt: " + spaceOptResult);

            assert dpResult == exp : "DP failed for s=" + s + ", p=" + p;
            assert memoResult == exp : "Memo failed for s=" + s + ", p=" + p;
            assert spaceOptResult == exp : "Space opt failed for s=" + s + ", p=" + p;

            System.out.println("✓ Passed\n");
        }

        System.out.println("All tests passed!");
    }
}
