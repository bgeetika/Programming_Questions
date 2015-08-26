def LIS(arr):
    temp = []
    n = len(arr)
    for i in range(0, n):
        temp.append(1)
    print temp
    for i in range(1, n):
        for j in range(0, i):
            if arr[j] < arr[i] and temp[i] < temp[j] + 1:
                temp[i] = temp[j] + 1
    return  max(temp)
        
        
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
LIS(arr)
