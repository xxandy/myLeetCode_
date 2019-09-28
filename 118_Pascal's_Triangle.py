def generate(numRows):
    if numRows==0:
        return []
    #init
    ans=[[1 for i in range(1,j+2)] for j in range(numRows)]
    for i in range(numRows):
        if i>1:
            for j in range(1,i):
                ans[i][j]=ans[i-1][j-1]+ans[i-1][j]
    return ans
