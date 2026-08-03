
class Solution(object):
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = float("-inf")
            total = 0

            # Take 1, 2, or 3 stones
            for j in range(i, min(i + 3, n)):
                total += stoneValue[j]

                # Opponent's advantage is dp[j + 1]
                dp[i] = max(dp[i], total - dp[j + 1])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"

