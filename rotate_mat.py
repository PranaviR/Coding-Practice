class Solution:
    def rotate_mat(self, mat):
        N=len(mat)
        for i in range(int(N/2)):
            for j in range(i,N-1-i):
                #store top as temp
                temp=mat[i][j]
                #rotate left to top
                mat[i][j]=mat[N-j-1][i]
                #rotate bottom to left
                mat[N-j-1][i]=mat[N-i-1][N-j-1]
                #rotate right to bottom
                mat[N-i-1][N-j-1]=mat[j][N-i-1]
                print(mat[j][N-i-1])
                #rotate top to right
                mat[j][N-i-1]=temp
        return mat
                                                       
sol=Solution()
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result=sol.rotate_mat(mat)
print(result)