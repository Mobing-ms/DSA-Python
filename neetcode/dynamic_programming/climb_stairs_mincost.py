class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.extend([0])
        n = len(cost)
        if n == 2:
            return 0
        if n == 3:
            return min(cost[0], cost[1])

        dp = [0] * (n)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, n):
            option1 = dp[i - 1] + cost[i - 1]
            option2 = dp[i - 2] + cost[i - 2]
            dp[i] = min(option1, option2)

        return dp[-1]
