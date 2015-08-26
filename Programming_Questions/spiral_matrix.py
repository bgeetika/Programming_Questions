def print_matrix_spiral(m, n , arr):
        k = 0
        l = 0
        while k < m and l < n: 
            for i in range(l,n):
                print arr[k][i]
            k = k + 1
            for i in range(k,m):
                print arr[i][n-1]
            n = n - 1
            for i in range(n-1, l-1 , -1):
                print arr[m-1][i]
            m = m - 1
            for i in range(m-1 , k-1 , -1):
                print arr[i][l]
            l = l + 1
arr = [[1,2,3],[4,5,6],[7,8,9]]
print_matrix_spiral(3, 3 , arr)
