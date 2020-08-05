from typing import List
from functools import cmp_to_key

class Solution:
    def mycmp(self, t1, t2):
        if t1[0] != t2[0]:
            return t1[0] - t2[0]
        elif t1[1] != t2[1]:
            return t1[1] - t2[1]
        else:
            return t2[2] - t1[2]

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        h = len(startTime)
        jobs = []
        for i in range(h):
            jobs.append((startTime[i],endTime[i],profit[i]))
        jobs.sort(key=cmp_to_key(self.mycmp))

        dp = [0] * h
        for i in range(h-1, -1, -1):
            dp[i] = jobs[i][2]
            for j in range(i+1, h):
                if jobs[j][0] >= jobs[i][1]:
                    dp[i] = max(dp[i], jobs[i][2] + dp[j])
        return max(dp)

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

    startTime = [6,15,7,11,1,3,16,2]
    endTime = [19,18,19,16,10,8,19,8]
    profit = [2,9,1,19,5,7,3,19]
    print(sol.jobScheduling(startTime, endTime, profit))