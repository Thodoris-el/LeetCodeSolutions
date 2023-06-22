class Solution {
public:
    string addBinary(string a, string b) {
        int r = 0;
        string res = "";
        if ( a.length() > b.length()){
            for(int i = b.length(); i < a.length(); i++){
                b = "0" + b;
            }
        }else if ( a.length() < b.length()){
            for(int i = a.length(); i < b.length(); i++){
                a = "0" + a;
            }
        }
        int tmp;
        for (int i = a.length() - 1; i >=0; i--){
            tmp = int(a[i]) - 48 + int(b[i]) - 48 + r;
            switch (tmp){
                case 0:
                    res = "0" + res;
                    break;
                case 1:
                    res = "1" + res;
                    r = 0;
                    break;
                case 2:
                    res = "0" + res;
                    r = 1;
                    break;
                case 3:
                    res = "1" +res;
                    r = 1;
                    break;
            }
        }

        if(r == 1){
            return "1" + res;
        }
        return res;
    }
};