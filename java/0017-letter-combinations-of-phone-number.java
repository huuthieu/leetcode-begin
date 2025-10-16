import java.util.*;

/**
 * LeetCode Problem 0017: Letter Combinations of a Phone Number
 *
 * Problem:
 * Given a string containing digits from 2-9 inclusive, return all possible letter
 * combinations that the number could represent.
 *
 * Digit mapping:
 * 2 -> "abc", 3 -> "def", 4 -> "ghi", 5 -> "jkl",
 * 6 -> "mno", 7 -> "pqrs", 8 -> "tuv", 9 -> "wxyz"
 *
 * Examples:
 * 1. Input: digits = "23", Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
 * 2. Input: digits = "", Output: []
 */
public class LetterCombinationsPhoneNumber {

    /**
     * Q1: Recursive backtracking
     *
     * Time Complexity: O(4^n)
     * Space Complexity: O(4^n)
     */
    public static List<String> letterCombinationsBacktrack(String digits) {
        List<String> result = new ArrayList<>();
        if (digits == null || digits.length() == 0) return result;

        String[] mapping = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        backtrack(digits, 0, "", result, mapping);
        return result;
    }

    private static void backtrack(String digits, int index, String current,
                                  List<String> result, String[] mapping) {
        if (index == digits.length()) {
            result.add(current);
            return;
        }

        String letters = mapping[digits.charAt(index) - '0'];
        for (char letter : letters.toCharArray()) {
            backtrack(digits, index + 1, current + letter, result, mapping);
        }
    }

    /**
     * Q2: Iterative approach
     *
     * Time Complexity: O(4^n)
     * Space Complexity: O(4^n)
     */
    public static List<String> letterCombinationsIterative(String digits) {
        List<String> result = new ArrayList<>();
        if (digits == null || digits.length() == 0) return result;

        String[] mapping = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        result.add("");

        for (char digit : digits.toCharArray()) {
            List<String> temp = new ArrayList<>();
            String letters = mapping[digit - '0'];

            for (String combo : result) {
                for (char letter : letters.toCharArray()) {
                    temp.add(combo + letter);
                }
            }

            result = temp;
        }

        return result;
    }

    /**
     * Q3: BFS with queue
     *
     * Time Complexity: O(4^n)
     * Space Complexity: O(4^n)
     */
    public static List<String> letterCombinationsBFS(String digits) {
        List<String> result = new ArrayList<>();
        if (digits == null || digits.length() == 0) return result;

        String[] mapping = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        Queue<String> queue = new LinkedList<>();
        queue.offer("");

        for (char digit : digits.toCharArray()) {
            int size = queue.size();
            String letters = mapping[digit - '0'];

            for (int i = 0; i < size; i++) {
                String combo = queue.poll();
                for (char letter : letters.toCharArray()) {
                    queue.offer(combo + letter);
                }
            }
        }

        result.addAll(queue);
        return result;
    }

    /**
     * Q4: Using HashMap
     *
     * Time Complexity: O(4^n)
     * Space Complexity: O(4^n)
     */
    public static List<String> letterCombinationsHashMap(String digits) {
        List<String> result = new ArrayList<>();
        if (digits == null || digits.length() == 0) return result;

        Map<Character, String> map = new HashMap<>();
        map.put('2', "abc");
        map.put('3', "def");
        map.put('4', "ghi");
        map.put('5', "jkl");
        map.put('6', "mno");
        map.put('7', "pqrs");
        map.put('8', "tuv");
        map.put('9', "wxyz");

        result.add("");

        for (char digit : digits.toCharArray()) {
            List<String> temp = new ArrayList<>();
            String letters = map.get(digit);

            for (String combo : result) {
                for (char letter : letters.toCharArray()) {
                    temp.add(combo + letter);
                }
            }

            result = temp;
        }

        return result;
    }

    /**
     * Q5: DFS with helper function
     *
     * Time Complexity: O(4^n)
     * Space Complexity: O(4^n)
     */
    public static List<String> letterCombinationsDFS(String digits) {
        List<String> result = new ArrayList<>();
        if (digits == null || digits.length() == 0) return result;

        String[] mapping = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        dfs(digits, 0, "", result, mapping);
        return result;
    }

    private static void dfs(String digits, int index, String current,
                            List<String> result, String[] mapping) {
        if (index == digits.length()) {
            result.add(current);
            return;
        }

        String letters = mapping[digits.charAt(index) - '0'];
        for (char letter : letters.toCharArray()) {
            dfs(digits, index + 1, current + letter, result, mapping);
        }
    }

    /**
     * Q6: StringBuilder approach
     *
     * Time Complexity: O(4^n)
     * Space Complexity: O(4^n)
     */
    public static List<String> letterCombinationsStringBuilder(String digits) {
        List<String> result = new ArrayList<>();
        if (digits == null || digits.length() == 0) return result;

        String[] mapping = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        helper(digits, 0, new StringBuilder(), result, mapping);
        return result;
    }

    private static void helper(String digits, int index, StringBuilder current,
                               List<String> result, String[] mapping) {
        if (index == digits.length()) {
            result.add(current.toString());
            return;
        }

        String letters = mapping[digits.charAt(index) - '0'];
        for (char letter : letters.toCharArray()) {
            current.append(letter);
            helper(digits, index + 1, current, result, mapping);
            current.deleteCharAt(current.length() - 1);
        }
    }

    /**
     * Q7: Stream-based approach
     *
     * Time Complexity: O(4^n)
     * Space Complexity: O(4^n)
     */
    public static List<String> letterCombinationsStream(String digits) {
        List<String> result = new ArrayList<>();
        if (digits == null || digits.length() == 0) return result;

        String[] mapping = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        result.add("");

        for (char digit : digits.toCharArray()) {
            String letters = mapping[digit - '0'];
            result = result.stream()
                    .flatMap(combo -> letters.chars()
                            .mapToObj(c -> combo + (char) c))
                    .collect(java.util.stream.Collectors.toList());
        }

        return result;
    }

    /**
     * Q8: Array-based mapping
     *
     * Time Complexity: O(4^n)
     * Space Complexity: O(4^n)
     */
    public static List<String> letterCombinationsArray(String digits) {
        List<String> result = new ArrayList<>();
        if (digits == null || digits.length() == 0) return result;

        String[] mapping = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        backtrackArray(digits, 0, new char[digits.length()], result, mapping);
        return result;
    }

    private static void backtrackArray(String digits, int index, char[] current,
                                       List<String> result, String[] mapping) {
        if (index == digits.length()) {
            result.add(new String(current));
            return;
        }

        String letters = mapping[digits.charAt(index) - '0'];
        for (char letter : letters.toCharArray()) {
            current[index] = letter;
            backtrackArray(digits, index + 1, current, result, mapping);
        }
    }

    /**
     * Q9: Loop with list manipulation
     *
     * Time Complexity: O(4^n)
     * Space Complexity: O(4^n)
     */
    public static List<String> letterCombinationsLoop(String digits) {
        List<String> result = new ArrayList<>();
        if (digits == null || digits.length() == 0) return result;

        String[] mapping = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        result.add("");

        for (int i = 0; i < digits.length(); i++) {
            String letters = mapping[digits.charAt(i) - '0'];
            int size = result.size();

            for (int j = 0; j < size; j++) {
                String combo = result.remove(0);
                for (char letter : letters.toCharArray()) {
                    result.add(combo + letter);
                }
            }
        }

        return result;
    }

    /**
     * Q10: Optimized with capacity pre-allocation
     *
     * Time Complexity: O(4^n)
     * Space Complexity: O(4^n)
     */
    public static List<String> letterCombinationsOptimized(String digits) {
        List<String> result = new ArrayList<>();
        if (digits == null || digits.length() == 0) return result;

        String[] mapping = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

        int capacity = 1;
        for (char digit : digits.toCharArray()) {
            capacity *= mapping[digit - '0'].length();
        }

        result.add("");

        for (char digit : digits.toCharArray()) {
            String letters = mapping[digit - '0'];
            int size = result.size();
            result.ensureCapacity(size * letters.length());

            for (int i = 0; i < size; i++) {
                String combo = result.get(i);
                for (int j = 1; j < letters.length(); j++) {
                    result.add(combo + letters.charAt(j));
                }
                result.set(i, combo + letters.charAt(0));
            }
        }

        return result;
    }

    // Test cases and main function
    public static void main(String[] args) {
        String[] testCases = {"23", "", "2", "234", "42"};
        int[] expectedSizes = {9, 0, 3, 27, 9};

        java.lang.reflect.Method[] methods = LetterCombinationsPhoneNumber.class.getDeclaredMethods();
        List<java.lang.reflect.Method> testMethods = new ArrayList<>();

        for (java.lang.reflect.Method method : methods) {
            if (method.getName().startsWith("letterCombinations") &&
                method.getReturnType() == List.class) {
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
                    List<String> result = (List<String>) method.invoke(null, testCases[i]);
                    boolean passed = result.size() == expectedSizes[i];
                    allPassed = allPassed && passed;
                    String status = passed ? "✓" : "✗";
                    String display = result.size() <= 5 ? result.toString() :
                            "[" + result.get(0) + ", " + result.get(1) + ", ..., " + result.get(result.size() - 1) + "]";
                    System.out.println("  " + status + " letterCombinations(\"" + testCases[i] +
                        "\") = " + display + " (size: " + result.size() + ")");
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
