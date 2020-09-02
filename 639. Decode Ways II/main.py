class Solution:
    def oneDigit(self, digit):
        if digit == '*':
            return 9
        elif digit == '0':
            return 0
        else:
            return 1

    def twoDigits(self, hi, lo):
        if hi > '2' or hi == '0':
            return 0
        elif hi == '*' and lo == '*':
            return 15
        elif hi == '*':
            return 1 if lo > '6' else 2
        elif lo == '*':
            return 9 if hi == '1' else 6
        else:
            return 1 if int(hi+lo) <= 26 else 0

    def numDecodings(self, s: str) -> int:
        N = len(s)
        if N == 0:
            return 0

        dp1 = [0] * (N+1)
        dp2 = [0] * (N+1)
        dp  = [1] + [0] * N
        M   = 1e9 + 7

        dp1[1] = self.oneDigit(s[0])
        for i in range(2,N+1):
            dp1[i] = self.oneDigit(s[i-1])
            dp2[i] = self.twoDigits(s[i-2],s[i-1])
        
        dp[1] = dp1[1]
        for i in range(2,N+1):
            dp[i] = (dp[i-1] * dp1[i] + dp[i-2] * dp2[i]) % M
        return int(dp[N])

if __name__ == "__main__":
    sol = Solution()
    print(sol.numDecodings("0"))
    print(sol.numDecodings("*"))
    print(sol.numDecodings("1*"))
    print(sol.numDecodings("**"))
    print(sol.numDecodings("*0"))
    print(sol.numDecodings("*1*1*0"))
    print(sol.numDecodings("3294"))
    