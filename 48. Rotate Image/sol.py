class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        bot = len(matrix) - 1
        top = 0
        while (top < bot):
            matrix[bot], matrix[top] = matrix[top], matrix[bot]
            bot -= 1
            top +=1

        n = len(matrix) * len(matrix[0])
        x = len(matrix)
        y = len(matrix[0])
        i = 0 
        while i <= n :
            matrix[i//x][i%y], matrix[i%y][i//x] = matrix[i%y][i//x], matrix[i//x][i%y] 
            i += 1
            if  i % x == 0 :
                i += i // x