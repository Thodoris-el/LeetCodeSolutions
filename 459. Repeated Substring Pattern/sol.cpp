class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        string res = s + s;
        if(res.substr(1,res.size()-2).find(s) != -1){
            return true;
        }
        return false;
    }
};