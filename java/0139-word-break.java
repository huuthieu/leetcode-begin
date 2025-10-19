import java.util.*;

/**
 * LeetCode Problem 0139: Word Break
 *
 * Problem:
 * Given a string s and a dictionary of strings wordDict, return true if s can be
 * segmented into a space-separated sequence of one or more dictionary words.
 *
 * Examples:
 * 1. Input: s = "leetcode", wordDict = ["leet","code"], Output: true
 * 2. Input: s = "applepenapple", wordDict = ["apple","pen"], Output: true
 * 3. Input: s = "catsandog", wordDict = ["cat","cats","and","sand","dog"], Output: false
 */
public class WordBreak {

    /**
     * Q1: DP with set for O(1) lookup
     *
     * Time Complexity: O(N^2)
     * Space Complexity: O(N)
     */
    public static boolean wordBreakDP(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;

        for (int i = 1; i <= s.length(); i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && wordSet.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[s.length()];
    }

    /**
     * Q2: BFS approach
     *
     * Time Complexity: O(N^2)
     * Space Complexity: O(N)
     */
    public static boolean wordBreakBFS(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);
        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();

        queue.offer(0);
        visited.add(0);

        while (!queue.isEmpty()) {
            int start = queue.poll();

            if (start == s.length()) {
                return true;
            }

            for (int end = start + 1; end <= s.length(); end++) {
                if (!visited.contains(end) && wordSet.contains(s.substring(start, end))) {
                    visited.add(end);
                    queue.offer(end);
                }
            }
        }

        return false;
    }

    /**
     * Q3: Backtracking with memoization
     *
     * Time Complexity: O(N^2)
     * Space Complexity: O(N)
     */
    public static boolean wordBreakMemo(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);
        Map<Integer, Boolean> memo = new HashMap<>();
        return backtrack(s, wordSet, 0, memo);
    }

    private static boolean backtrack(String s, Set<String> wordSet, int index,
                                     Map<Integer, Boolean> memo) {
        if (memo.containsKey(index)) {
            return memo.get(index);
        }

        if (index == s.length()) {
            return true;
        }

        for (int end = index + 1; end <= s.length(); end++) {
            if (wordSet.contains(s.substring(index, end)) && backtrack(s, wordSet, end, memo)) {
                memo.put(index, true);
                return true;
            }
        }

        memo.put(index, false);
        return false;
    }

    /**
     * Q4: DP with word length optimization
     *
     * Time Complexity: O(N^2)
     * Space Complexity: O(N)
     */
    public static boolean wordBreakOptimized(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);
        int maxLen = wordDict.stream().mapToInt(String::length).max().orElse(0);
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;

        for (int i = 1; i <= s.length(); i++) {
            for (int j = Math.max(0, i - maxLen); j < i; j++) {
                if (dp[j] && wordSet.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[s.length()];
    }

    /**
     * Q5: DFS with memoization
     *
     * Time Complexity: O(N^2)
     * Space Complexity: O(N)
     */
    public static boolean wordBreakDFS(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);
        Map<Integer, Boolean> cache = new HashMap<>();
        return dfs(s, wordSet, 0, cache);
    }

    private static boolean dfs(String s, Set<String> wordSet, int index,
                              Map<Integer, Boolean> cache) {
        if (cache.containsKey(index)) {
            return cache.get(index);
        }

        if (index == s.length()) {
            return true;
        }

        for (int end = index + 1; end <= s.length(); end++) {
            if (wordSet.contains(s.substring(index, end))) {
                if (dfs(s, wordSet, end, cache)) {
                    cache.put(index, true);
                    return true;
                }
            }
        }

        cache.put(index, false);
        return false;
    }

    /**
     * Q6: Recursive with set pruning
     *
     * Time Complexity: O(N^2)
     * Space Complexity: O(N)
     */
    public static boolean wordBreakRecursive(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);
        return canBreak(s, wordSet);
    }

    private static boolean canBreak(String s, Set<String> wordSet) {
        if (s.isEmpty()) {
            return true;
        }

        for (String word : wordSet) {
            if (s.startsWith(word) && canBreak(s.substring(word.length()), wordSet)) {
                return true;
            }
        }

        return false;
    }

    /**
     * Q7: DP with explicit loop
     *
     * Time Complexity: O(N^2)
     * Space Complexity: O(N)
     */
    public static boolean wordBreakExplicit(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);
        int n = s.length();
        boolean[] dp = new boolean[n + 1];
        dp[0] = true;

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && wordSet.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[n];
    }

    /**
     * Q8: Clean and simple
     *
     * Time Complexity: O(N^2)
     * Space Complexity: O(N)
     */
    public static boolean wordBreakClean(String s, List<String> wordDict) {
        Set<String> dict = new HashSet<>(wordDict);
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;

        for (int i = 1; i <= s.length(); i++) {
            for (int j = 0; j < i && !dp[i]; j++) {
                if (dp[j] && dict.contains(s.substring(j, i))) {
                    dp[i] = true;
                }
            }
        }

        return dp[s.length()];
    }

    /**
     * Q9: Using startsWith optimization
     *
     * Time Complexity: O(N^2)
     * Space Complexity: O(N)
     */
    public static boolean wordBreakStartsWith(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;

        for (int i = 1; i <= s.length(); i++) {
            for (String word : wordSet) {
                if (word.length() <= i && dp[i - word.length()] &&
                    s.substring(i - word.length(), i).equals(word)) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[s.length()];
    }

    /**
     * Q10: Compact version
     *
     * Time Complexity: O(N^2)
     * Space Complexity: O(N)
     */
    public static boolean wordBreakCompact(String s, List<String> wordDict) {
        Set<String> set = new HashSet<>(wordDict);
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;

        for (int i = 1; i <= s.length(); i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && set.contains(s.substring(j, i))) dp[i] = true;
            }
        }

        return dp[s.length()];
    }

    // Test cases and main function
    public static void main(String[] args) {
        String[] testStrings = {"leetcode", "applepenapple", "catsandog", "ab", "a", "", "a"};
        List<String>[] testDicts = {
            Arrays.asList("leet", "code"),
            Arrays.asList("apple", "pen"),
            Arrays.asList("cat", "cats", "and", "sand", "dog"),
            Arrays.asList("a", "b"),
            Arrays.asList("b"),
            Arrays.asList("a"),
            Arrays.asList("a")
        };
        boolean[] expected = {true, true, false, true, false, false, true};

        java.lang.reflect.Method[] methods = WordBreak.class.getDeclaredMethods();
        List<java.lang.reflect.Method> testMethods = new ArrayList<>();

        for (java.lang.reflect.Method method : methods) {
            if (method.getName().startsWith("wordBreak") &&
                method.getReturnType() == boolean.class &&
                method.getParameterCount() == 2) {
                testMethods.add(method);
            }
        }

        Collections.sort(testMethods, Comparator.comparing(java.lang.reflect.Method::getName));

        int questionNum = 1;
        for (java.lang.reflect.Method method : testMethods) {
            System.out.println("\nQ" + questionNum + ": " + method.getName());
            System.out.println("-".repeat(70));

            boolean allPassed = true;
            for (int i = 0; i < testStrings.length; i++) {
                try {
                    boolean result = (boolean) method.invoke(null, testStrings[i], testDicts[i]);
                    boolean passed = result == expected[i];
                    allPassed = allPassed && passed;
                    String status = passed ? "✓" : "✗";
                    System.out.println("  " + status + " wordBreak(\"" + testStrings[i] +
                        "\", " + testDicts[i] + ") = " + result + " (expected: " + expected[i] + ")");
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
