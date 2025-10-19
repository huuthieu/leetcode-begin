/**
 * LeetCode 322: Coin Change
 *
 * Problem:
 * You are given an integer array coins representing coins of different denominations
 * and an integer amount representing a total amount of money.
 *
 * Return the fewest number of coins that you need to make up that amount.
 * If that amount of money cannot be made up by any combination of the coins, return -1.
 *
 * Example:
 * coins = [1,2,5], amount = 5 => 1
 * coins = [2], amount = 3 => -1
 */

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;

public class CoinChange {

    // Approach 1: Dynamic Programming - Bottom-Up
    public static int coinChange_DP(int[] coins, int amount) {
        /**
         * dp[i] = minimum coins needed to make amount i
         * Time: O(amount * n), Space: O(amount)
         */
        if (amount == 0) return 0;

        int[] dp = new int[amount + 1];
        for (int i = 1; i <= amount; i++) {
            dp[i] = amount + 1; // Impossible value
        }

        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (coin <= i) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }

        return dp[amount] > amount ? -1 : dp[amount];
    }

    // Approach 2: BFS - Shortest Path
    public static int coinChange_BFS(int[] coins, int amount) {
        /**
         * Treat as shortest path problem
         * Time: O(amount * n), Space: O(amount)
         */
        if (amount == 0) return 0;

        Queue<int[]> queue = new LinkedList<>();
        boolean[] visited = new boolean[amount + 1];

        queue.offer(new int[]{amount, 0}); // {remaining amount, num_coins}
        visited[amount] = true;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int remaining = current[0];
            int numCoins = current[1];

            for (int coin : coins) {
                int newAmount = remaining - coin;

                if (newAmount == 0) {
                    return numCoins + 1;
                }

                if (newAmount > 0 && !visited[newAmount]) {
                    visited[newAmount] = true;
                    queue.offer(new int[]{newAmount, numCoins + 1});
                }
            }
        }

        return -1;
    }

    // Approach 3: Memoization - Top-Down
    public static int coinChange_Memo(int[] coins, int amount) {
        /**
         * Recursive solution with memoization
         * Time: O(amount * n), Space: O(amount)
         */
        int[] memo = new int[amount + 1];
        for (int i = 1; i <= amount; i++) {
            memo[i] = -2; // Unvisited
        }
        return dp(coins, amount, memo);
    }

    private static int dp(int[] coins, int remaining, int[] memo) {
        if (remaining == 0) return 0;
        if (remaining < 0) return -1;
        if (memo[remaining] != -2) return memo[remaining];

        int minCoins = Integer.MAX_VALUE;

        for (int coin : coins) {
            int result = dp(coins, remaining - coin, memo);
            if (result >= 0) {
                minCoins = Math.min(minCoins, result + 1);
            }
        }

        memo[remaining] = (minCoins == Integer.MAX_VALUE) ? -1 : minCoins;
        return memo[remaining];
    }

    // Test Cases
    public static void main(String[] args) {
        int[][] coins = {
            {1, 2, 5},
            {2},
            {10},
            {1, 3, 4},
            {3, 6, 9},
            {2, 5, 10},
            {1},
            {1}
        };

        int[] amounts = {5, 3, 10, 6, 12, 27, 0, 1};
        int[] expectedResults = {1, -1, 1, 2, 2, 4, 0, 1};

        for (int i = 0; i < coins.length; i++) {
            int expected = expectedResults[i];

            int result_dp = coinChange_DP(coins[i], amounts[i]);
            int result_bfs = coinChange_BFS(coins[i], amounts[i]);
            int result_memo = coinChange_Memo(coins[i], amounts[i]);

            assert result_dp == expected : "DP failed";
            assert result_bfs == expected : "BFS failed";
            assert result_memo == expected : "Memo failed";

            System.out.println("Test case " + i + ": " + expected + " ✓");
        }

        System.out.println("\nAll tests passed!");
    }
}
