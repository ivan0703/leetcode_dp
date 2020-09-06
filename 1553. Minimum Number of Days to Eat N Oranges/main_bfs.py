class Solution:
    def minDays(self, n: int) -> int:
        if n <= 1:
            return n
        q = [n]
        ans = 0
        visited = [False] * n + [True]
        while q:
            size = len(q)
            for _ in range(size):
                i = q.pop(0)
                if i-1==0:
                    return ans + 1
                elif not visited[i-1]:
                    q.append(i-1)
                    visited[i-1] = True

                if i%2==0 and not visited[i//2]:
                    q.append(i//2)
                    visited[i//2] = True
                
                if i%3==0 and not visited[i - 2 * i//3]:
                    q.append(i-2*i//3)
                    visited[i-2*i//3] = True
            ans += 1

        return -1

if __name__ == '__main__':
    sol = Solution()
    # print(sol.minDays(10))
    # print(sol.minDays(6))
    # print(sol.minDays(1))
    # print(sol.minDays(56))
    # print(sol.minDays(9209408))
    print(sol.minDays(61455274))