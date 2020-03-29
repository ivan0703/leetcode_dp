class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        dp = [0] * len(s)
        res = 0
        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif len(stack) > 0 and stack[-1] != -1:
                dp[i] = i - stack[-1] + 1
                if stack[-1] > 0:
                    dp[i] = dp[i] + dp[stack[-1]-1]
                res = max(res, dp[i])
                stack.pop()
            else:
                stack.append(-1)

        return res

if __name__ == "__main__":
    s = '))((((((())((((())))))))(()'
    
    sol = Solution()
    print(sol.longestValidParentheses(s))