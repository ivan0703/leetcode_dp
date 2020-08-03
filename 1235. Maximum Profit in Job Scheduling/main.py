from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        h = len(startTime)
        graph = [[] for _ in range(h)]
        for i in range(h):
            for j in range(h):
                if i == j:
                    continue
                if startTime[j] >= endTime[i]:
                    graph[i].append(j)

        dp = {}
        ret = -float('Inf')
        for i in range(h):
            ret = max(ret, self.profitStartFrom(i, graph, profit, dp))
        
        return ret

    def profitStartFrom(self, i, graph, profit, dp):
        if i in dp:
            return dp[i]
        if not graph[i]:
            return profit[i]
        ret = -float('Inf')
        for j in graph[i]:
            ret = max(ret, profit[i] + self.profitStartFrom(j, graph, profit, dp))
        dp[i] = ret
        return ret

if __name__ == "__main__":
    
    sol = Solution()

    startTime = [1,2,3,3]
    endTime = [3,4,5,6]
    profit = [50,10,40,70]
    print(sol.jobScheduling(startTime, endTime, profit))

    startTime = [1,2,3,4,6]
    endTime = [3,5,10,6,9]
    profit = [20,20,100,70,60]
    print(sol.jobScheduling(startTime, endTime, profit))

    startTime = [1,1,1]
    endTime = [2,3,4]
    profit = [5,6,4]
    print(sol.jobScheduling(startTime, endTime, profit))