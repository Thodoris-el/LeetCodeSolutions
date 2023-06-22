class Solution {
public:
    int romanToInt(string s) {
        //create a dict
        map<char, int> roman;
        int res = 0;
        bool checked = false;

        roman['I'] = 1;
        roman['V'] = 5;
        roman['X'] = 10;
        roman['L'] = 50;
        roman['C'] = 100;
        roman['D'] = 500;
        roman['M'] = 1000;
        
        for (int i = 0; i < s.length(); i++){
            if (checked){
                checked = false;
                continue;
            }
            if(i+1<s.length() && roman[s[i]] < roman[s[i+1]]){
                res = res + (roman[s[i+1]] - roman[s[i]]);
                checked = true;
            }else{
                res += roman[s[i]];
            }
        }
        return res;

    }
};