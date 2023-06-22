class Solution {
public:
    double myPow(double x, int n) {
        double res = 1;
        int p = abs(n);
        while(p > 0){
            if(p % 2 == 1){
                res = (res * x);
            }
            x = x * x;
            p = p / 2;
        }
        if (n < 0){
            return 1.0/res;
        }
        return res;
    }
};