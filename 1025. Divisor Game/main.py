class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0

if __name__ == '__main__':
    sol = Solution()
    print('{}'.format(sol.divisorGame(33)))