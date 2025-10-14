/**
 * LeetCode 0003: Longest Substring Without Repeating Characters
 *
 * Problem Statement:
 * Given a string s, find the length of the longest substring without repeating characters.
 *
 * Example 1:
 * Input: s = "abcabcbb"
 * Output: 3
 * Explanation: The answer is "abc", with the length of 3.
 *
 * Example 2:
 * Input: s = "bbbbb"
 * Output: 1
 * Explanation: The answer is "b", with the length of 1.
 *
 * Example 3:
 * Input: s = "pwwkew"
 * Output: 3
 * Explanation: The answer is "wke", with the length of 3.
 * Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 *
 * Constraints:
 * - 0 <= s.length <= 5 * 10^4
 * - s consists of English letters, digits, symbols and spaces.
 */

import java.util.*;

public class LongestSubstringWithoutRepeatingCharacters {

    // Q1: What's the brute force approach and its time complexity?
    // A1: Check all substrings and verify each is unique. Time: O(n^3), Space: O(min(n,m))
    public int lengthOfLongestSubstringBruteForce(String s) {
        int maxLength = 0;
        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 1; j <= s.length(); j++) {
                if (hasUniqueChars(s.substring(i, j))) {
                    maxLength = Math.max(maxLength, j - i);
                }
            }
        }
        return maxLength;
    }

    private boolean hasUniqueChars(String substring) {
        Set<Character> chars = new HashSet<>();
        for (char c : substring.toCharArray()) {
            if (chars.contains(c)) {
                return false;
            }
            chars.add(c);
        }
        return true;
    }

    // Q2: How can we optimize using the sliding window technique with a set?
    // A2: Use two pointers and expand/shrink window. Time: O(2n) = O(n), Space: O(min(n,m))
    public int lengthOfLongestSubstringSet(String s) {
        Set<Character> charSet = new HashSet<>();
        int left = 0;
        int maxLength = 0;

        for (int right = 0; right < s.length(); right++) {
            // Remove characters from left until no duplicate
            while (charSet.contains(s.charAt(right))) {
                charSet.remove(s.charAt(left));
                left++;
            }

            charSet.add(s.charAt(right));
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }

    // Q3: Can we optimize further with a hash map to avoid shrinking one by one?
    // A3: Store character indices and jump left pointer. Time: O(n), Space: O(min(n,m))
    public int lengthOfLongestSubstringOptimized(String s) {
        Map<Character, Integer> charIndex = new HashMap<>();
        int maxLength = 0;
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            char currentChar = s.charAt(right);

            // If character is in window, jump left pointer
            if (charIndex.containsKey(currentChar) && charIndex.get(currentChar) >= left) {
                left = charIndex.get(currentChar) + 1;
            }

            charIndex.put(currentChar, right);
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }

    // Q4: What if we need to return the actual substring instead of just length?
    // A4: Keep track of the start and end indices of the longest substring
    public String longestSubstringWithoutRepeating(String s) {
        Map<Character, Integer> charIndex = new HashMap<>();
        int maxLength = 0;
        int maxStart = 0;
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            char currentChar = s.charAt(right);

            if (charIndex.containsKey(currentChar) && charIndex.get(currentChar) >= left) {
                left = charIndex.get(currentChar) + 1;
            }

            charIndex.put(currentChar, right);

            if (right - left + 1 > maxLength) {
                maxLength = right - left + 1;
                maxStart = left;
            }
        }

        return s.substring(maxStart, maxStart + maxLength);
    }

    // Q5: How would you handle the case with limited character set (e.g., only ASCII)?
    // A5: Use array instead of hash map for O(1) access with fixed space
    public int lengthOfLongestSubstringArray(String s) {
        // Assuming ASCII charset (128 characters)
        int[] charIndex = new int[128];
        Arrays.fill(charIndex, -1);
        int maxLength = 0;
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            char currentChar = s.charAt(right);
            if (charIndex[currentChar] >= left) {
                left = charIndex[currentChar] + 1;
            }

            charIndex[currentChar] = right;
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }

    // Q6: What if we need to find all substrings with maximum length?
    // A6: Store all substrings that match the maximum length
    public List<String> allLongestSubstrings(String s) {
        Map<Character, Integer> charIndex = new HashMap<>();
        int maxLength = 0;
        List<String> results = new ArrayList<>();
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            char currentChar = s.charAt(right);

            if (charIndex.containsKey(currentChar) && charIndex.get(currentChar) >= left) {
                left = charIndex.get(currentChar) + 1;
            }

            charIndex.put(currentChar, right);
            int currentLength = right - left + 1;

            if (currentLength > maxLength) {
                maxLength = currentLength;
                results.clear();
                results.add(s.substring(left, right + 1));
            } else if (currentLength == maxLength) {
                results.add(s.substring(left, right + 1));
            }
        }

        return results;
    }

    // Q7: What about edge cases we should consider?
    // A7: Empty string, single character, all same characters, all unique characters
    public int lengthOfLongestSubstringWithValidation(String s) {
        if (s == null || s.isEmpty()) {
            return 0;
        }
        if (s.length() == 1) {
            return 1;
        }

        Map<Character, Integer> charIndex = new HashMap<>();
        int maxLength = 0;
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            char currentChar = s.charAt(right);

            if (charIndex.containsKey(currentChar) && charIndex.get(currentChar) >= left) {
                left = charIndex.get(currentChar) + 1;
            }

            charIndex.put(currentChar, right);
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }

    // Q8: What's the space-time tradeoff analysis?
    /**
     * A8:
     * Brute Force: O(n^3) time, O(min(n,m)) space
     * Sliding Window (Set): O(2n) time, O(min(n,m)) space
     * Sliding Window (HashMap): O(n) time, O(min(n,m)) space
     * Array-based (fixed charset): O(n) time, O(1) space (fixed 128 or 256)
     *
     * Where n is string length and m is charset size.
     * The optimized hash map approach is generally preferred.
     */

    // Q9: How would you solve this problem using StringBuilder?
    // A9: Use StringBuilder to track current window
    public int lengthOfLongestSubstringStringBuilder(String s) {
        StringBuilder window = new StringBuilder();
        int maxLength = 0;

        for (char c : s.toCharArray()) {
            int index = window.indexOf(String.valueOf(c));
            if (index != -1) {
                window.delete(0, index + 1);
            }
            window.append(c);
            maxLength = Math.max(maxLength, window.length());
        }

        return maxLength;
    }

    // Q10: What variations of this problem exist?
    /**
     * A10: Common variations include:
     * - Longest substring with at most K distinct characters
     * - Longest substring with at most 2 distinct characters
     * - Longest repeating character replacement
     * - Minimum window substring
     * - Longest substring with same letters after replacement
     * - Permutation in string
     * - Find all anagrams in string
     */

    public static void main(String[] args) {
        LongestSubstringWithoutRepeatingCharacters solution = new LongestSubstringWithoutRepeatingCharacters();

        // Test cases
        String[] testStrings = {
            "abcabcbb",
            "bbbbb",
            "pwwkew",
            "",
            "a",
            "abcdef",
            "au",
            "dvdf",
            "tmmzuxt"
        };

        int[] expected = {3, 1, 3, 0, 1, 6, 2, 3, 5};

        for (int i = 0; i < testStrings.length; i++) {
            int result = solution.lengthOfLongestSubstringOptimized(testStrings[i]);
            System.out.println("Input: s = \"" + testStrings[i] + "\"");
            System.out.println("Output: " + result + ", Expected: " + expected[i]);
            System.out.println("Correct: " + (result == expected[i]));
            System.out.println();
        }
    }
}
