#include <iostream>

using namespace std;

class Solution {
public:
    bool divisorGame(int N) {
        /*
           +-----+---+---+---+---+---+---+---+---+---+---+---+---+---+--
           |  N  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| ...
           +-----+---+---+---+---+---+---+---+---+---+---+---+---+---+--
           | T/F | F | T | F | T | F | T | F | T | F | T | F | T | ...
           +-----+---+---+---+---+---+---+---+---+---+---+---+---+---+--
         */
        return N%2==0;
    }
};

int main()
{
    int N = 367;
    Solution sol;
    cout<<sol.divisorGame(N)<<endl;
    return 0;
}