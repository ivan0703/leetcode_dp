from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wset = set(wordDict)
        dp = [True] + [False]*len(s)
        for i in range(1,len(s)+1):
            for j in range(i):
                dp[i] |= (dp[j] and (s[j:i] in wset))
        return dp[len(s)]


if __name__ == "__main__":
    sol = Solution()
    
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    print(sol.wordBreak(s1, wordDict1))

    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    print(sol.wordBreak(s2, wordDict2))

    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    print(sol.wordBreak(s3, wordDict3))