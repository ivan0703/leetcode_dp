class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        N = len(num)
        if k > N:
            return ""

        dp = [["" for _ in range(k+1)] for _ in range(N)]
        for i in range(N):
            dp[i][0] = num[i:]
        for i in range(N-2, -1, -1):
            for j in range(1,k+1):
                if j >= N-i:
                    continue
                dp[i][j] = min( dp[i+1][j-1], num[i] + dp[i+1][j] )

        ans = dp[0][k].lstrip("0")
        return ans if ans else "0"


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeKdigits("1432219", 3))
    print(sol.removeKdigits("10200", 1))
    print(sol.removeKdigits("10", 2))
    