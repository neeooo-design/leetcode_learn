# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
# 常规法
# class Solution:
#     def generateMatrix(self, n: int) -> list[list[int]]:
#         mat=[[0]*n for i in range(n)]
#         count=1
#         start_num=0
#         while start_num<n//2:
#             for j in range(start_num,n-1-start_num):
#                 mat[start_num][j]=count
#                 count+=1
#             for i in range(start_num,n-1-start_num):
#                 mat[i][n-1-start_num]=count
#                 count+=1
#             for j in range(n-1-start_num,start_num,-1):
#                 mat[n-1-start_num][j]=count
#                 count+=1
#             for i in range(n-1-start_num,start_num,-1):
#                 mat[i][start_num]=count
#                 count+=1
#             start_num+=1


#         if n%2==1:
#             mat[n//2][n//2]=n**2

#         return mat

        
# if __name__=='__main__':
#     s=Solution()
#     s.generateMatrix(5)



# 边界收缩法
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        mat=[[0]*n for i in range(n)]
        top=0
        left=0
        bottom=n-1
        right=n-1
        count=1
        while count<=n**2:
            for j in range(left,right+1):
                mat[top][j]=count
                count+=1
            top+=1
            for i in range(top,bottom+1):
                mat[i][right]=count
                count+=1
            right-=1
            for j in range(right,left-1,-1):
                mat[bottom][j]=count
                count+=1
            bottom-=1
            for i in range(bottom,top-1,-1):
                mat[i][left]=count
                count+=1
            left+=1
        return mat

if __name__=='__main__':
    s=Solution()
    s.generateMatrix(5)