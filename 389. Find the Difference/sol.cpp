class Solution {
public:
    char findTheDifference(string s, string t) {
        int count = 0;
        for( unsigned int i = 0; i < t.length(); i++){
            count += int(t[i]);
        }
        for( unsigned int i = 0; i < s.length(); i++){
            count -= int(s[i]);
        }
        
        return char(count);
    }
};