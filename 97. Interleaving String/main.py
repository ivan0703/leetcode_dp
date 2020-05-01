
class Solution:
    def dfs(self, i1: int, i2: int, i3: int) -> bool:
        if i3 == len(self.s3):
            return True
        
        if i1 < len(self.s1) and self.s1[i1]==self.s3[i3] and self.dfs(i1+1, i2, i3+1):
            return True
        if i2 < len(self.s2) and self.s2[i2]==self.s3[i3] and self.dfs(i1, i2+1, i3+1):
            return True
        return False

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

        return self.dfs(0, 0, 0)

if __name__ == "__main__":
    sol = Solution()
    print(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
    print(sol.isInterleave("aabcc", "dbbca", "aadbbbaccc"))
    print(sol.isInterleave("a", "b", "abc"))
    print(sol.isInterleave("ab", "a", "aba"))
    print(sol.isInterleave("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
        "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab", 
        "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"))