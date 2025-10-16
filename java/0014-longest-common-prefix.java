import java.util.*;

/**
 * LeetCode Problem 0014: Longest Common Prefix
 *
 * Problem:
 * Write a function to find the longest common prefix string amongst an array of strings.
 * If there is no common prefix, return an empty string "".
 *
 * Examples:
 * 1. Input: strs = ["flower","flow","flight"], Output: "fl"
 * 2. Input: strs = ["dog","racecar","car"], Output: ""
 */
public class LongestCommonPrefix {

    /**
     * Q1: Horizontal scanning - compare first string with all others
     *
     * Time Complexity: O(n * m) where n is number of strings, m is min length
     * Space Complexity: O(1)
     */
    public static String longestCommonPrefixHorizontal(String[] strs) {
        if (strs == null || strs.length == 0) return "";

        String prefix = strs[0];

        for (int i = 1; i < strs.length; i++) {
            while (!strs[i].startsWith(prefix)) {
                prefix = prefix.substring(0, prefix.length() - 1);
                if (prefix.isEmpty()) return "";
            }
        }

        return prefix;
    }

    /**
     * Q2: Vertical scanning - compare characters column by column
     *
     * Time Complexity: O(n * m)
     * Space Complexity: O(1)
     */
    public static String longestCommonPrefixVertical(String[] strs) {
        if (strs == null || strs.length == 0) return "";

        for (int i = 0; i < strs[0].length(); i++) {
            char c = strs[0].charAt(i);
            for (int j = 1; j < strs.length; j++) {
                if (i >= strs[j].length() || strs[j].charAt(i) != c) {
                    return strs[0].substring(0, i);
                }
            }
        }

        return strs[0];
    }

    /**
     * Q3: Divide and conquer
     *
     * Time Complexity: O(n * m)
     * Space Complexity: O(m) for recursion stack
     */
    public static String longestCommonPrefixDivideConquer(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        return lcp(strs, 0, strs.length - 1);
    }

    private static String lcp(String[] strs, int left, int right) {
        if (left == right) return strs[left];

        int mid = left + (right - left) / 2;
        String lcpLeft = lcp(strs, left, mid);
        String lcpRight = lcp(strs, mid + 1, right);

        return common(lcpLeft, lcpRight);
    }

    private static String common(String left, String right) {
        int minLen = Math.min(left.length(), right.length());
        for (int i = 0; i < minLen; i++) {
            if (left.charAt(i) != right.charAt(i)) {
                return left.substring(0, i);
            }
        }
        return left.substring(0, minLen);
    }

    /**
     * Q4: Binary search on length
     *
     * Time Complexity: O(n * m * log(m))
     * Space Complexity: O(1)
     */
    public static String longestCommonPrefixBinarySearch(String[] strs) {
        if (strs == null || strs.length == 0) return "";

        int minLen = Integer.MAX_VALUE;
        for (String s : strs) {
            minLen = Math.min(minLen, s.length());
        }

        int left = 0, right = minLen;

        while (left < right) {
            int mid = left + (right - left + 1) / 2;
            if (isCommonPrefix(strs, mid)) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }

        return strs[0].substring(0, left);
    }

    private static boolean isCommonPrefix(String[] strs, int length) {
        String prefix = strs[0].substring(0, length);
        for (int i = 1; i < strs.length; i++) {
            if (!strs[i].startsWith(prefix)) {
                return false;
            }
        }
        return true;
    }

    /**
     * Q5: Character-by-character with early termination
     *
     * Time Complexity: O(n * m)
     * Space Complexity: O(1)
     */
    public static String longestCommonPrefixCharByChar(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        if (strs.length == 1) return strs[0];

        int minLen = Integer.MAX_VALUE;
        for (String s : strs) {
            minLen = Math.min(minLen, s.length());
        }

        for (int i = 0; i < minLen; i++) {
            char c = strs[0].charAt(i);
            for (int j = 1; j < strs.length; j++) {
                if (strs[j].charAt(i) != c) {
                    return strs[0].substring(0, i);
                }
            }
        }

        return strs[0].substring(0, minLen);
    }

    /**
     * Q6: Trie-based approach
     *
     * Time Complexity: O(n * m)
     * Space Complexity: O(n * m)
     */
    public static String longestCommonPrefixTrie(String[] strs) {
        if (strs == null || strs.length == 0) return "";

        class TrieNode {
            Map<Character, TrieNode> children = new HashMap<>();
            int count = 0;
        }

        TrieNode root = new TrieNode();

        // Build trie
        for (String word : strs) {
            TrieNode node = root;
            for (char c : word.toCharArray()) {
                node.children.putIfAbsent(c, new TrieNode());
                node = node.children.get(c);
                node.count++;
            }
        }

        // Find LCP
        StringBuilder result = new StringBuilder();
        TrieNode node = root;
        while (node.children.size() == 1) {
            char c = node.children.keySet().iterator().next();
            TrieNode child = node.children.get(c);
            if (child.count == strs.length) {
                result.append(c);
                node = child;
            } else {
                break;
            }
        }

        return result.toString();
    }

    /**
     * Q7: Using StringBuilder with comparison
     *
     * Time Complexity: O(n * m)
     * Space Complexity: O(m)
     */
    public static String longestCommonPrefixStringBuilder(String[] strs) {
        if (strs == null || strs.length == 0) return "";

        StringBuilder prefix = new StringBuilder();

        for (int i = 0; i < strs[0].length(); i++) {
            char c = strs[0].charAt(i);
            for (int j = 1; j < strs.length; j++) {
                if (i >= strs[j].length() || strs[j].charAt(i) != c) {
                    return prefix.toString();
                }
            }
            prefix.append(c);
        }

        return prefix.toString();
    }

    /**
     * Q8: Two-pointer scanning
     *
     * Time Complexity: O(n * m)
     * Space Complexity: O(1)
     */
    public static String longestCommonPrefixTwoPointer(String[] strs) {
        if (strs == null || strs.length == 0) return "";

        int col = 0;
        while (col < strs[0].length()) {
            char c = strs[0].charAt(col);
            for (int row = 1; row < strs.length; row++) {
                if (col >= strs[row].length() || strs[row].charAt(col) != c) {
                    return strs[0].substring(0, col);
                }
            }
            col++;
        }

        return strs[0];
    }

    /**
     * Q9: Iterative with substring comparisons
     *
     * Time Complexity: O(n * m)
     * Space Complexity: O(1)
     */
    public static String longestCommonPrefixIterative(String[] strs) {
        if (strs == null || strs.length == 0) return "";

        for (int i = 0; i < strs[0].length(); i++) {
            for (int j = 1; j < strs.length; j++) {
                if (i >= strs[j].length() ||
                    strs[0].charAt(i) != strs[j].charAt(i)) {
                    return strs[0].substring(0, i);
                }
            }
        }

        return strs[0];
    }

    /**
     * Q10: Using stream API
     *
     * Time Complexity: O(n * m)
     * Space Complexity: O(1)
     */
    public static String longestCommonPrefixStream(String[] strs) {
        if (strs == null || strs.length == 0) return "";

        for (int i = 0; i < strs[0].length(); i++) {
            final int index = i;
            char c = strs[0].charAt(index);

            boolean allMatch = Arrays.stream(strs, 1, strs.length)
                    .allMatch(s -> index < s.length() && s.charAt(index) == c);

            if (!allMatch) {
                return strs[0].substring(0, index);
            }
        }

        return strs[0];
    }

    // Test cases and main function
    public static void main(String[] args) {
        String[][] testCases = {
                {"flower", "flow", "flight"},
                {"dog", "racecar", "car"},
                {"ab"},
                {"a"},
                {"interspecies", "interstellar", "interstate"},
                {"abc"},
                {"abab", "aba", "abc"},
                {"a", "a", "a", "a"},
        };
        String[] expected = {"fl", "", "ab", "a", "inters", "abc", "ab", "a"};

        java.lang.reflect.Method[] methods = LongestCommonPrefix.class.getDeclaredMethods();
        List<java.lang.reflect.Method> testMethods = new ArrayList<>();

        for (java.lang.reflect.Method method : methods) {
            if (method.getName().startsWith("longestCommonPrefix") &&
                method.getReturnType() == String.class) {
                testMethods.add(method);
            }
        }

        Collections.sort(testMethods, Comparator.comparing(java.lang.reflect.Method::getName));

        int questionNum = 1;
        for (java.lang.reflect.Method method : testMethods) {
            System.out.println("\nQ" + questionNum + ": " + method.getName());
            System.out.println("-".repeat(60));

            boolean allPassed = true;
            for (int i = 0; i < testCases.length; i++) {
                try {
                    String result = (String) method.invoke(null, (Object) testCases[i]);
                    boolean passed = result.equals(expected[i]);
                    allPassed = allPassed && passed;
                    String status = passed ? "✓" : "✗";
                    System.out.println("  " + status + " longestCommonPrefix(" +
                        Arrays.toString(testCases[i]) + ") = \"" + result +
                        "\" (expected: \"" + expected[i] + "\")");
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
