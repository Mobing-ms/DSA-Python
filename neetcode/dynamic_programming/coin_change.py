from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int):
        dp = [float('inf')] * (amount + 1)
        parent = [-1] * (amount + 1)
        coin_comb = []

        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    if dp[i - coin] + 1 < dp[i]:
                        dp[i] = dp[i - coin] + 1
                        parent[i] = coin

        # <-- Modified: Check whether the amount is reachable
        if dp[amount] == float('inf'):
            return []

        current_index = amount

        # <-- Modified: Reconstruct the coins used
        while current_index > 0:
            coin_comb.append(parent[current_index])
            current_index = current_index - parent[current_index]   # <-- Modified

        return coin_comb


if __name__ == "__main__":
    sol = Solution()
    out_list = sol.coinChange([1, 3, 4], 11)
    print(out_list)