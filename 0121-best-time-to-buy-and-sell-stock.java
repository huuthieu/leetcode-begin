/**
 * LeetCode 121: Best Time to Buy and Sell Stock
 *
 * Problem:
 * You are given an array prices where prices[i] is the price of a given stock on the ith day.
 * You want to maximize your profit by choosing a single day to buy one stock and a different day
 * in the future to sell that stock. Return the maximum profit you can achieve from this transaction.
 * If you cannot achieve any profit, return 0.
 *
 * Example:
 * prices = [7,1,5,3,6,4] => 5 (buy at 1, sell at 6)
 * prices = [7,6,4,3,2,1] => 0 (no transaction)
 */

public class BestTimeToBuyAndSellStock {

    // Approach 1: One Pass - Track Min Price and Max Profit
    public static int maxProfit_OnePass(int[] prices) {
        /**
         * Keep track of minimum price and maximum profit
         * For each price, calculate profit if we sell at that price
         * Time: O(n), Space: O(1)
         */
        if (prices.length < 2) return 0;

        int minPrice = prices[0];
        int maxProfit = 0;

        for (int i = 1; i < prices.length; i++) {
            int potentialProfit = prices[i] - minPrice;
            maxProfit = Math.max(maxProfit, potentialProfit);
            minPrice = Math.min(minPrice, prices[i]);
        }

        return maxProfit;
    }

    // Approach 2: Simplified One Pass
    public static int maxProfit_Simplified(int[] prices) {
        /**
         * Same logic but cleaner code
         * Time: O(n), Space: O(1)
         */
        int maxProfit = 0;
        int minPrice = Integer.MAX_VALUE;

        for (int price : prices) {
            minPrice = Math.min(minPrice, price);
            maxProfit = Math.max(maxProfit, price - minPrice);
        }

        return maxProfit;
    }

    // Approach 3: Two Pointer
    public static int maxProfit_TwoPointer(int[] prices) {
        /**
         * Left pointer tracks buy, right pointer tracks sell
         * Time: O(n), Space: O(1)
         */
        if (prices.length < 2) return 0;

        int left = 0;  // Buy
        int right = 1; // Sell
        int maxProfit = 0;

        while (right < prices.length) {
            if (prices[left] < prices[right]) {
                int profit = prices[right] - prices[left];
                maxProfit = Math.max(maxProfit, profit);
            } else {
                left = right;
            }
            right++;
        }

        return maxProfit;
    }

    // Approach 4: Brute Force (Not Optimal)
    public static int maxProfit_BruteForce(int[] prices) {
        /**
         * Check all possible pairs
         * Time: O(n^2), Space: O(1)
         */
        int maxProfit = 0;

        for (int i = 0; i < prices.length; i++) {
            for (int j = i + 1; j < prices.length; j++) {
                int profit = prices[j] - prices[i];
                maxProfit = Math.max(maxProfit, profit);
            }
        }

        return maxProfit;
    }

    // Test Cases
    public static void main(String[] args) {
        int[][] testCases = {
            {7, 1, 5, 3, 6, 4},
            {7, 6, 4, 3, 2, 1},
            {2, 4, 1},
            {1},
            {2, 1},
            {1, 2},
            {3, 2, 6, 5, 0, 3},
            {1, 1, 1, 1},
            {2, 1, 2, 0, 4, 4, 3}
        };

        int[] expectedResults = {5, 0, 2, 0, 1, 1, 4, 0, 4};

        for (int i = 0; i < testCases.length; i++) {
            int[] prices = testCases[i];
            int expected = expectedResults[i];

            assert maxProfit_OnePass(prices) == expected : "OnePass failed";
            assert maxProfit_Simplified(prices) == expected : "Simplified failed";
            assert maxProfit_TwoPointer(prices) == expected : "TwoPointer failed";
            assert maxProfit_BruteForce(prices) == expected : "BruteForce failed";

            System.out.println("Test case " + i + ": " + expected + " ✓");
        }

        System.out.println("\nAll tests passed!");

        // Example usage
        int[] example = {7, 1, 5, 3, 6, 4};
        System.out.println("\nBest Time to Buy and Sell Stock Example: " + maxProfit_OnePass(example));
    }
}
