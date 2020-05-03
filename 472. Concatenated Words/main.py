from typing import List, Set

class Solution:
    def isConcat(self, target: str, uset: Set) -> bool:
        if len(uset) == 0:
            return False
        dp = [True] + [False] * len(target)
        for i in range(1,len(target)+1):
            for j in range(i):
                if dp[j] and (target[j:i] in uset):
                    dp[i] = True
                    break
        return dp[-1]

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        uset = set(words)
        ans = []
        for word in words:
            if word=="":
                continue
            uset.remove(word)
            if self.isConcat(word, uset):
                ans.append(word)
            uset.add(word)

        return ans


if __name__ == "__main__":
    words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    
    sol = Solution()
    ans = sol.findAllConcatenatedWordsInADict(words)
    for w in ans:
        print(w)
