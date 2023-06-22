class Solution {
public:
    bool judgeCircle(string moves) {
        int x = 0;
        int y = 0;
        for (int i = 0; i < moves.length(); i++){
            switch (moves[i]){
                case 'U':
                    x++;
                    break;
                case 'D':
                    x--;
                    break;
                case 'L':
                    y++;
                    break;
                case 'R':
                    y--;
                    break;        
            }
        }
        if(x==0 && y==0){
            return true;
        }
        return false;
    }
};
