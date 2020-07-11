class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == "":
            if p=="*" or p=="":
                return True
            else:
                return False

        M = len(p)
        N = len(s)

        dp = [[False for _ in range(N+1)] for _ in range(M+1)]
        dp[0][0] = True
        if M>0 and p[0]=='*':
            dp[1][0] = True

        for i in range(1, M+1):
            dp[i][0] = (p[i-1]=='*' and dp[i-1][0])
            for j in range(1, N+1):
                if p[i-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1] or dp[i-1][j-1]
                elif p[i-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = (p[i-1] == s[j-1] and dp[i-1][j-1])

        return dp[M][N]


if __name__ == "__main__":
    sol = Solution()
    # print(sol.isMatch("aa", "a"))
    # print(sol.isMatch("aa", "*"))
    # print(sol.isMatch("cb", "?a"))
    # print(sol.isMatch("adceb", "*a*b"))
    # print(sol.isMatch("acdcb", "a*c?b"))
    print(sol.isMatch("ho", "**ho"))
    print(sol.isMatch("aab", "c*a*b"))