class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
       int  r = 1;
        for (int i = digits.size() - 1; i >= 0; i--){
            if ( r == 1){
                if (digits[i] == 9 ){
                    digits[i] = 0;
                    //res.insert(res.begin(), 0);
                    r = 1;
                }
                else{
                    digits[i] += 1;
                    //res.insert(res.begin(), digits[i] + 1);
                    r = 0;
                    break;
                }
            }
        }
        if (r == 1){
            digits.insert(digits.begin(), 1);
        }
        return digits;
    }
};