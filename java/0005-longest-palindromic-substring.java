/**
 * LeetCode 0005: Longest Palindromic Substring
 *
 * Problem Statement:
 * Given a string s, return the longest palindromic substring in s.
 *
 * Example 1:
 * Input: s = "babad"
 * Output: "bab"
 * Explanation: "aba" is also a valid answer.
 *
 * Example 2:
 * Input: s = "cbbd"
 * Output: "bb"
 *
 * Constraints:
 * - 1 <= s.length <= 1000
 * - s consist of only digits and English letters.
 */

public class LongestPalindromicSubstring {

    // Q1: What's the brute force approach and its time complexity?
    // A1: Check all possible substrings for palindrome. Time: O(n^3), Space: O(1)
    public String longestPalindrome_bruteForce(String s) {
        int n = s.length();
        String longest = "";

        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                String substr = s.substring(i, j + 1);
                if (isPalindrome(substr) && substr.length() > longest.length()) {
                    longest = substr;
                }
            }
        }

        return longest;
    }

    private boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    // Q2: Can we optimize by expanding around centers?
    // A2: Yes! Expand around each center. Time: O(n^2), Space: O(1)
    public String longestPalindrome_expandAroundCenter(String s) {
        if (s == null || s.length() < 1) {
            return "";
        }

        int start = 0;
        int maxLen = 0;

        for (int i = 0; i < s.length(); i++) {
            // Odd length palindromes (center is a single character)
            int len1 = expandAroundCenter(s, i, i);
            // Even length palindromes (center is between two characters)
            int len2 = expandAroundCenter(s, i, i + 1);

            int currentLen = Math.max(len1, len2);

            if (currentLen > maxLen) {
                maxLen = currentLen;
                start = i - (currentLen - 1) / 2;
            }
        }

        return s.substring(start, start + maxLen);
    }

    private int expandAroundCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }

    // Q3: How does dynamic programming help solve this?
    // A3: Build table where dp[i][j] = true if s[i:j+1] is palindrome. Time: O(n^2), Space: O(n^2)
    public String longestPalindrome_dp(String s) {
        int n = s.length();
        if (n < 2) {
            return s;
        }

        boolean[][] dp = new boolean[n][n];

        // Every single character is a palindrome
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
        }

        int start = 0;
        int maxLen = 1;

        // Check for two-character palindromes
        for (int i = 0; i < n - 1; i++) {
            if (s.charAt(i) == s.charAt(i + 1)) {
                dp[i][i + 1] = true;
                start = i;
                maxLen = 2;
            }
        }

        // Check for palindromes of length 3 and more
        for (int length = 3; length <= n; length++) {
            for (int i = 0; i <= n - length; i++) {
                int j = i + length - 1;

                if (s.charAt(i) == s.charAt(j) && dp[i + 1][j - 1]) {
                    dp[i][j] = true;
                    start = i;
                    maxLen = length;
                }
            }
        }

        return s.substring(start, start + maxLen);
    }

    // Q4: What's Manacher's algorithm and how does it work?
    // A4: Linear time algorithm using symmetry. Time: O(n), Space: O(n)
    public String longestPalindrome_manacher(String s) {
        if (s == null || s.length() == 0) {
            return "";
        }

        // Transform string to handle even and odd length palindromes
        String T = preprocessString(s);
        int n = T.length();
        int[] P = new int[n];
        int C = 0; // Center
        int R = 0; // Right boundary

        for (int i = 1; i < n - 1; i++) {
            int mirror = 2 * C - i;

            if (i < R) {
                P[i] = Math.min(R - i, P[mirror]);
            }

            // Try to expand palindrome centered at i
            try {
                while (T.charAt(i + 1 + P[i]) == T.charAt(i - 1 - P[i])) {
                    P[i]++;
                }
            } catch (StringIndexOutOfBoundsException e) {
                // Do nothing
            }

            // If palindrome centered at i extends past R, adjust C and R
            if (i + P[i] > R) {
                C = i;
                R = i + P[i];
            }
        }

        // Find the maximum element in P
        int maxLen = 0;
        int centerIndex = 0;
        for (int i = 1; i < n - 1; i++) {
            if (P[i] > maxLen) {
                maxLen = P[i];
                centerIndex = i;
            }
        }

        int start = (centerIndex - maxLen) / 2;
        return s.substring(start, start + maxLen);
    }

    private String preprocessString(String s) {
        StringBuilder sb = new StringBuilder();
        sb.append('^');
        for (int i = 0; i < s.length(); i++) {
            sb.append('#').append(s.charAt(i));
        }
        sb.append('#').append('$');
        return sb.toString();
    }

    // Q5: How to count all palindromic substrings?
    // A5: Similar to expand around center but count all palindromes
    public int countPalindromicSubstrings(String s) {
        int total = 0;
        for (int i = 0; i < s.length(); i++) {
            total += countPalindromesAroundCenter(s, i, i);     // Odd length
            total += countPalindromesAroundCenter(s, i, i + 1); // Even length
        }
        return total;
    }

    private int countPalindromesAroundCenter(String s, int left, int right) {
        int count = 0;
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            count++;
            left--;
            right++;
        }
        return count;
    }

    // Q6: How do we handle edge cases?
    // A6: Empty strings, single character, entire string is palindrome
    public String longestPalindrome_withValidation(String s) {
        if (s == null || s.isEmpty()) {
            return "";
        }

        if (s.length() == 1) {
            return s;
        }

        // Check if entire string is palindrome
        if (isPalindrome(s)) {
            return s;
        }

        return longestPalindrome_expandAroundCenter(s);
    }

    // Q7: What's the space-time tradeoff analysis?
    /**
     * A7: Different approaches and their complexities:
     *
     * 1. Brute Force:
     *    - Time: O(n^3) - O(n^2) substrings, O(n) to check each
     *    - Space: O(1)
     *
     * 2. Dynamic Programming:
     *    - Time: O(n^2)
     *    - Space: O(n^2) - for DP table
     *
     * 3. Expand Around Center:
     *    - Time: O(n^2) - O(n) centers, O(n) expansion each
     *    - Space: O(1)
     *    - Best practical approach for most cases
     *
     * 4. Manacher's Algorithm:
     *    - Time: O(n)
     *    - Space: O(n)
     *    - Optimal complexity but more complex to implement
     */

    // Q8: Can we optimize the expand around center approach?
    // A8: We can track indices instead of creating substrings
    public String longestPalindrome_optimized(String s) {
        if (s == null || s.length() < 1) {
            return "";
        }

        int start = 0;
        int end = 0;

        for (int i = 0; i < s.length(); i++) {
            int len1 = expandAroundCenter(s, i, i);
            int len2 = expandAroundCenter(s, i, i + 1);
            int len = Math.max(len1, len2);

            if (len > end - start) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }

        return s.substring(start, end + 1);
    }

    // Q9: How to implement with early termination optimization?
    // A9: If remaining string can't exceed current max, stop early
    public String longestPalindrome_earlyTermination(String s) {
        if (s == null || s.length() < 1) {
            return "";
        }

        int start = 0;
        int maxLen = 1;

        for (int i = 0; i < s.length(); i++) {
            // Early termination: if remaining string can't beat current max
            if (s.length() - i <= maxLen / 2) {
                break;
            }

            int len1 = expandAroundCenter(s, i, i);
            int len2 = expandAroundCenter(s, i, i + 1);
            int currentLen = Math.max(len1, len2);

            if (currentLen > maxLen) {
                maxLen = currentLen;
                start = i - (currentLen - 1) / 2;
            }
        }

        return s.substring(start, start + maxLen);
    }

    // Q10: What are common variations and related problems?
    /**
     * A10: Common variations include:
     *
     * 1. Palindrome Permutation: Check if string can be rearranged to form palindrome
     * 2. Valid Palindrome: Check if string is palindrome (ignoring non-alphanumeric)
     * 3. Valid Palindrome II: Allow deleting at most one character
     * 4. Palindromic Substrings: Count all palindromic substrings
     * 5. Shortest Palindrome: Add minimum characters to make palindrome
     * 6. Palindrome Partitioning: Partition string so each substring is palindrome
     * 7. Longest Palindromic Subsequence: Similar but non-contiguous
     *
     * Key insights:
     * - Expand around center is most practical
     * - DP good for learning but uses more space
     * - Manacher's for optimal complexity when needed
     * - Understanding palindrome properties is crucial
     */

    // Main method for testing
    public static void main(String[] args) {
        LongestPalindromicSubstring solution = new LongestPalindromicSubstring();

        // Test cases
        String[][] testCases = {
            {"babad", "bab"},  // "aba" is also valid
            {"cbbd", "bb"},
            {"a", "a"},
            {"ac", "a"},       // or "c"
            {"racecar", "racecar"},
            {"noon", "noon"},
            {"aaaa", "aaaa"},
            {"abacabad", "abacaba"}
        };

        System.out.println("Testing Expand Around Center Solution (Recommended):");
        for (String[] testCase : testCases) {
            String input = testCase[0];
            String result = solution.longestPalindrome_expandAroundCenter(input);
            System.out.println("Input: s = \"" + input + "\"");
            System.out.println("Output: \"" + result + "\"");
            System.out.println("Length: " + result.length());
            System.out.println();
        }

        System.out.println("\nTesting Manacher's Algorithm (O(n) time):");
        for (int i = 0; i < Math.min(5, testCases.length); i++) {
            String input = testCases[i][0];
            String result = solution.longestPalindrome_manacher(input);
            System.out.println("Input: \"" + input + "\" -> Output: \"" + result + "\"");
        }

        System.out.println("\nCounting palindromic substrings:");
        String[] countTests = {"abc", "aaa", "noon"};
        for (String s : countTests) {
            int count = solution.countPalindromicSubstrings(s);
            System.out.println("Input: \"" + s + "\" has " + count + " palindromic substrings");
        }
    }
}
