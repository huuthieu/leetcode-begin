/**
 * LeetCode Problem 0028: Find the Index of the First Occurrence in a String
 *
 * Problem:
 * Given two strings needle and haystack, return the index of the first occurrence
 * of needle in haystack, or -1 if needle is not part of haystack.
 *
 * Examples:
 * 1. Input: haystack = "sadbutsad", needle = "sad", Output: 0
 * 2. Input: haystack = "leetcode", needle = "leeto", Output: -1
 * 3. Input: haystack = "a", needle = "a", Output: 0
 */

public class FirstOccurrence {

    // Q1: Built-in method
    public static int strStr(String haystack, String needle) {
        return haystack.indexOf(needle);
    }

    // Q2: Brute force approach
    public static int strStrBruteForce(String haystack, String needle) {
        if (needle.length() == 0) return 0;
        if (needle.length() > haystack.length()) return -1;

        for (int i = 0; i <= haystack.length() - needle.length(); i++) {
            if (haystack.substring(i, i + needle.length()).equals(needle)) {
                return i;
            }
        }

        return -1;
    }

    // Q3: Character-by-character comparison
    public static int strStrCharCompare(String haystack, String needle) {
        if (needle.length() == 0) return 0;

        for (int i = 0; i <= haystack.length() - needle.length(); i++) {
            boolean match = true;
            for (int j = 0; j < needle.length(); j++) {
                if (haystack.charAt(i + j) != needle.charAt(j)) {
                    match = false;
                    break;
                }
            }
            if (match) return i;
        }

        return -1;
    }

    // Q4: KMP Algorithm
    public static int strStrKMP(String haystack, String needle) {
        if (needle.length() == 0) return 0;
        if (needle.length() > haystack.length()) return -1;

        int[] prefix = buildPrefix(needle);
        int j = 0;

        for (int i = 0; i < haystack.length(); i++) {
            while (j > 0 && haystack.charAt(i) != needle.charAt(j)) {
                j = prefix[j - 1];
            }

            if (haystack.charAt(i) == needle.charAt(j)) {
                j++;
            }

            if (j == needle.length()) {
                return i - needle.length() + 1;
            }
        }

        return -1;
    }

    private static int[] buildPrefix(String s) {
        int[] prefix = new int[s.length()];
        int j = 0;

        for (int i = 1; i < s.length(); i++) {
            while (j > 0 && s.charAt(i) != s.charAt(j)) {
                j = prefix[j - 1];
            }

            if (s.charAt(i) == s.charAt(j)) {
                j++;
            }

            prefix[i] = j;
        }

        return prefix;
    }

    // Q5: Two-pointer sliding window
    public static int strStrTwoPointer(String haystack, String needle) {
        if (needle.length() == 0) return 0;

        for (int start = 0; start <= haystack.length() - needle.length(); start++) {
            int j = 0;
            for (j = 0; j < needle.length(); j++) {
                if (haystack.charAt(start + j) != needle.charAt(j)) {
                    break;
                }
            }
            if (j == needle.length()) {
                return start;
            }
        }

        return -1;
    }

    // Q6: Using startsWith
    public static int strStrStartsWith(String haystack, String needle) {
        if (needle.length() == 0) return 0;

        for (int i = 0; i <= haystack.length() - needle.length(); i++) {
            if (haystack.substring(i).startsWith(needle)) {
                return i;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        String[][] tests = {
            {"sadbutsad", "sad"},
            {"leetcode", "leeto"},
            {"a", "a"},
            {"ab", "ba"}
        };

        System.out.println("Q1: strStr (Built-in)");
        for (String[] test : tests) {
            System.out.println("  strStr(\"" + test[0] + "\", \"" + test[1] + "\") = " +
                strStr(test[0], test[1]));
        }

        System.out.println("\nQ2: strStr (Brute Force)");
        System.out.println("  strStr(\"sadbutsad\", \"sad\") = " +
            strStrBruteForce("sadbutsad", "sad"));

        System.out.println("\nQ3: strStr (KMP)");
        System.out.println("  strStr(\"sadbutsad\", \"sad\") = " +
            strStrKMP("sadbutsad", "sad"));
    }
}
