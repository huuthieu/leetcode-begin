import java.util.*;

/**
 * LeetCode Problem 0030: Substring with Concatenation of All Words
 *
 * Problem:
 * You are given a string s and an array of strings words of the same length.
 * Return all starting indices of substring(s) in s that is a concatenation of
 * each word in words exactly once, in any order, and without overlapping.
 *
 * Examples:
 * 1. Input: s = "barfoothefoobarman", words = ["foo","bar"], Output: [0,9]
 * 2. Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"], Output: []
 */

public class SubstringWithConcatenation {

    // Q1: Sliding window with HashMap (optimal)
    public static List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<>();

        if (s == null || s.length() == 0 || words == null || words.length == 0) {
            return result;
        }

        int wordLen = words[0].length();
        int numWords = words.length;
        int windowSize = wordLen * numWords;
        Map<String, Integer> wordCount = new HashMap<>();

        for (String word : words) {
            wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
        }

        for (int i = 0; i <= s.length() - windowSize; i++) {
            String window = s.substring(i, i + windowSize);
            Map<String, Integer> windowWords = new HashMap<>();

            for (int j = 0; j < windowSize; j += wordLen) {
                String word = window.substring(j, j + wordLen);
                windowWords.put(word, windowWords.getOrDefault(word, 0) + 1);
            }

            if (windowWords.equals(wordCount)) {
                result.add(i);
            }
        }

        return result;
    }

    // Q2: Optimized sliding window
    public static List<Integer> findSubstringOptimized(String s, String[] words) {
        List<Integer> result = new ArrayList<>();

        if (s == null || s.length() == 0 || words == null || words.length == 0) {
            return result;
        }

        int wordLen = words[0].length();
        int numWords = words.length;
        int windowSize = wordLen * numWords;
        Map<String, Integer> wordCount = new HashMap<>();

        for (String word : words) {
            wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
        }

        for (int start = 0; start <= s.length() - windowSize; start++) {
            Map<String, Integer> seen = new HashMap<>();
            boolean valid = true;

            for (int j = 0; j < numWords; j++) {
                String word = s.substring(start + j * wordLen, start + (j + 1) * wordLen);

                if (!wordCount.containsKey(word)) {
                    valid = false;
                    break;
                }

                seen.put(word, seen.getOrDefault(word, 0) + 1);

                if (seen.get(word) > wordCount.get(word)) {
                    valid = false;
                    break;
                }
            }

            if (valid && seen.equals(wordCount)) {
                result.add(start);
            }
        }

        return result;
    }

    // Q3: Two-pointer approach
    public static List<Integer> findSubstringTwoPointer(String s, String[] words) {
        List<Integer> result = new ArrayList<>();

        if (s == null || s.length() == 0 || words == null || words.length == 0) {
            return result;
        }

        int wordLen = words[0].length();
        int numWords = words.length;
        int windowSize = wordLen * numWords;
        Map<String, Integer> wordCount = new HashMap<>();

        for (String word : words) {
            wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
        }

        for (int i = 0; i <= s.length() - windowSize; i++) {
            Map<String, Integer> currentCount = new HashMap<>();

            for (int j = i; j < i + windowSize; j += wordLen) {
                String word = s.substring(j, j + wordLen);
                currentCount.put(word, currentCount.getOrDefault(word, 0) + 1);
            }

            if (currentCount.equals(wordCount)) {
                result.add(i);
            }
        }

        return result;
    }

    // Q4: With early termination
    public static List<Integer> findSubstringEarlyTerm(String s, String[] words) {
        List<Integer> result = new ArrayList<>();

        if (s == null || s.length() == 0 || words == null || words.length == 0) {
            return result;
        }

        int wordLen = words[0].length();
        int numWords = words.length;
        int windowSize = wordLen * numWords;
        Map<String, Integer> wordCount = new HashMap<>();

        for (String word : words) {
            wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
        }

        for (int i = 0; i <= s.length() - windowSize; i++) {
            String window = s.substring(i, i + windowSize);
            Map<String, Integer> currentCount = new HashMap<>();
            boolean valid = true;

            for (int j = 0; j < windowSize; j += wordLen) {
                String word = window.substring(j, j + wordLen);

                if (!wordCount.containsKey(word)) {
                    valid = false;
                    break;
                }

                currentCount.put(word, currentCount.getOrDefault(word, 0) + 1);
            }

            if (valid && currentCount.equals(wordCount)) {
                result.add(i);
            }
        }

        return result;
    }

    public static void main(String[] args) {
        String s1 = "barfoothefoobarman";
        String[] words1 = {"foo", "bar"};
        System.out.println("Q1: findSubstring (Sliding Window)");
        System.out.println("  Result: " + findSubstring(s1, words1));

        String s2 = "barfoofoobarthefoobarman";
        String[] words2 = {"bar", "foo", "the"};
        System.out.println("\nQ2: findSubstring (Optimized)");
        System.out.println("  Result: " + findSubstringOptimized(s2, words2));

        System.out.println("\nQ3: findSubstring (Two-Pointer)");
        System.out.println("  Result: " + findSubstringTwoPointer(s1, words1));
    }
}
