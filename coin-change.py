class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()

        # dp[i] is minimum number of coins to reach i amount
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for i in range(1, len(dp)):
            minCoins = float("inf")
            for c in coins:
                # How much more we need
                diff = i - c

                # Coin is too large
                if diff < 0:
                    dp[i] = -1
                    break

                # If it is impossible to create the difference using the given coins
                if dp[diff] == -1:
                    continue

                # Update the minmum coins to reach i
                minCoins = min(minCoins, dp[diff] + 1)

            if minCoins == float("inf"):
                continue

            dp[i] = minCoins

        return dp[amount]
