#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<string> subBreak(string s, vector<string> &wordDict, unordered_map<string, vector<string>> &umap) {
        if(umap.find(s)!=umap.end())
            return umap[s];
        if(s=="")
            return {""};
        
        vector<string> res;
        for(string w : wordDict) {
            if(s.substr(0, w.size()) != w)
                continue;

            vector<string> tmp = subBreak(s.substr(w.size()), wordDict, umap);
            for(string s : tmp) {
                string item = w + (s == "" ? s : (" " + s));
                res.push_back(item);
            }
        }

        umap[s] = res;
        return res;
    }

    vector<string> wordBreak(string s, vector<string>& wordDict) {
        unordered_map<string, vector<string>> umap;
        return subBreak(s, wordDict, umap);
    }
};

int main()
{
    //string s = "catsanddog";
    //vector<string> wordDict = {"cat", "cats", "and", "sand", "dog"};
    
    //string s = "pineapplepenapple";
    //vector<string> wordDict = {"apple", "pen", "applepen", "pine", "pineapple"};
    
    //string s = "catsandog";
    //vector<string> wordDict = {"cats", "dog", "sand", "and", "cat"};
    
    string s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    vector<string> wordDict = {"a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"};

    Solution sol;
    vector<string> res  = sol.wordBreak(s, wordDict);
    for(string s : res) {
        cout<<s<<endl;
    }

    return 0;
}