class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> spiral;
        char dir = 'r';
        int tmpH = 0;
        int tmpV = 0;
        int countH = matrix.size();
        int countV = matrix[0].size();
        int countH1 = 0;
        int countV1 = -1;
        int size = countH * countV;
        for (int i = 0; i < size; i++){
            switch (dir){
                cout<<i;
                case 'r':
                    spiral.push_back(matrix[tmpH][tmpV]);
                    tmpV++;
                    if (tmpV == countV){
                        dir = 'd';
                        countV--;
                        tmpV--;
                        tmpH++;
                    }
                    break;
                case 'd':
                    spiral.push_back(matrix[tmpH][tmpV]);
                    tmpH++;
                    if (tmpH == countH){
                        dir = 'l';
                        countH--;
                        tmpH--;
                        tmpV--;
                    }
                    break;
                case 'l':
                    spiral.push_back(matrix[tmpH][tmpV]);
                    tmpV--;
                    if (tmpV == countV1){
                        dir = 'u';
                        countV1++;
                        tmpV++;
                        tmpH--;
                    }
                    break;
                case 'u':
                    spiral.push_back(matrix[tmpH][tmpV]);
                    tmpH--;
                    if (tmpH == countH1){
                        dir = 'r';
                        countH1++;
                        tmpH++;
                        tmpV++;
                    }
                    break;    
            }
        }
        return spiral;
        
    }
};