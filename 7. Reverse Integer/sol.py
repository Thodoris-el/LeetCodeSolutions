class Solution:
    def reverse(self, x: int) -> int:
        new_num = 0
        flag = False
        if x < 0 :
            x = 0 - x
            flag = True
        while(x != 0):
            new_num = new_num * 10 + x % 10
            x = x // 10   
        if new_num < -2147483648 or new_num > 2147483647:
            return 0
        if flag:
             return -1 * new_num
        return new_num