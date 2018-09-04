class Solution:
    def zero_mat(self, mat):
        row=[]
        col=[]
        M=len(mat)
        N=len(mat[0])
        for i in range(M):
            for j in range(N):
                if mat[i][j]==0:
                    row.append(i)
                    col.append(j)
        for i in range(M):
            for j in range(N):
                if i in row or j in col:
                    mat[i][j]=0
        return mat
sol=Solution()
mat=[[1,2,0,4],[5,6,7,8],[9,10,11,12],[13,0,15,16]]
result=sol.zero_mat(mat)
print(result)










    



        