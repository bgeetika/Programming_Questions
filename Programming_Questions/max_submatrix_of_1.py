matrix = [ [0 , 1 , 1,  0,  1 ],
   [1,  1,  1,  1,  0 ],
   [1 , 1,  1,  1,  0],
   [1 , 1 , 1 , 1 , 0],
   [1 , 1 , 1 , 1 , 1],
   [0 , 0  ,0  ,0  ,0]]




def max_1(matrix):
    m = len(matrix)
    n = len(matrix[0])
    res = [[0]*n for x in range(0, m)]
    for i in  range(0,n):
        res[0][i] = matrix[0][i]
    for i in range(0, m):
        res[i][0] = matrix[i][0]    
    
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 1:
                res[i][j] = min(res[i-1][j-1], res[i-1][j], res[i][j-1]) + 1
            else:
                res[i][j] = 0
    max_num = 0 
    
    for i in range(0, m):
        for j in range(0, n):
            if res[i][j] > max_num:
                max_num = res[i][j] 
            
    return max_num

print max_1(matrix)
