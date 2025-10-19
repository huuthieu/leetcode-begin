/**
 * LeetCode 242: Valid Anagram
 *
 * Problem:
 * Given two strings s and t, return true if t is an anagram of s, and false otherwise.
 * An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
 * typically using all the original letters exactly once.
 *
 * Example:
 * s = "anagram", t = "nagaram" => true
 * s = "rat", t = "car" => false
 */

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class ValidAnagram {

    // Approach 1: Sorting
    public static boolean isAnagram_Sorting(String s, String t) {
        /**
         * Convert strings to char arrays, sort them, and compare
         * Time: O(n log n), Space: O(1) - not counting output
         */
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();
        Arrays.sort(sArray);
        Arrays.sort(tArray);
        return Arrays.equals(sArray, tArray);
    }

    // Approach 2: Hash Map
    public static boolean isAnagram_HashMap(String s, String t) {
        /**
         * Count characters in s, then subtract from t
         * Time: O(n), Space: O(k) where k = alphabet size
         */
        if (s.length() != t.length()) return false;

        Map<Character, Integer> charCount = new HashMap<>();

        for (char c : s.toCharArray()) {
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }

        for (char c : t.toCharArray()) {
            if (!charCount.containsKey(c)) return false;
            charCount.put(c, charCount.get(c) - 1);
            if (charCount.get(c) < 0) return false;
        }

        return true;
    }

    // Approach 3: Array (Fixed size for lowercase English)
    public static boolean isAnagram_Array(String s, String t) {
        /**
         * Use array of size 26 for lowercase letters
         * Time: O(n), Space: O(1) - fixed size array
         */
        if (s.length() != t.length()) return false;

        int[] count = new int[26];

        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }

        for (int c : count) {
            if (c != 0) return false;
        }

        return true;
    }

    // Approach 4: Two Hash Maps
    public static boolean isAnagram_TwoMaps(String s, String t) {
        /**
         * Create frequency maps for both strings and compare
         * Time: O(n), Space: O(k)
         */
        if (s.length() != t.length()) return false;

        Map<Character, Integer> countS = new HashMap<>();
        Map<Character, Integer> countT = new HashMap<>();

        for (char c : s.toCharArray()) {
            countS.put(c, countS.getOrDefault(c, 0) + 1);
        }

        for (char c : t.toCharArray()) {
            countT.put(c, countT.getOrDefault(c, 0) + 1);
        }

        return countS.equals(countT);
    }

    // Test Cases
    public static void main(String[] args) {
        String[][] testCases = {
            {"anagram", "nagaram"},
            {"rat", "car"},
            {"a", "b"},
            {"ab", "ba"},
            {"listen", "silent"},
            {"hello", "world"}
        };

        boolean[] expectedResults = {true, false, false, true, true, false};

        for (int i = 0; i < testCases.length; i++) {
            String s = testCases[i][0];
            String t = testCases[i][1];
            boolean expected = expectedResults[i];

            assert isAnagram_Sorting(s, t) == expected : "Sorting failed";
            assert isAnagram_HashMap(s, t) == expected : "HashMap failed";
            assert isAnagram_Array(s, t) == expected : "Array failed";
            assert isAnagram_TwoMaps(s, t) == expected : "TwoMaps failed";

            System.out.println("s=\"" + s + "\", t=\"" + t + "\" => " + expected + " ✓");
        }

        System.out.println("\nAll tests passed!");

        // Example usage
        System.out.println("\nValid Anagram Example: " + isAnagram_Array("anagram", "nagaram"));
    }
}
