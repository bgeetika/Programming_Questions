
class Solution(object):
    
    def find_row(self, matrix, m, n, target):
        start = 0
        end = n-1
        while start <= end and start >= 0 and end < n:
            mid = (start+end)/2
            #print mid
            if matrix[mid][m - 1] >= target and  ((mid - 1) < 0 or  matrix[mid-1][m-1] < target):
                index = mid
                return index
            elif matrix[mid][m-1] < target:
                start = mid + 1
            else:
                end = mid - 1
        return None
        

    def find_column(self, matrix,m, target, row_index):
        start = 0
        end = m - 1
        print row_index
        while start <= end and start >= 0 and end < m:
            mid = (start+end)/2
            print mid
            if matrix[row_index][mid] == target:
                return True
            elif matrix[row_index][mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False
        
    def check(self, matrix, m , n, target):
        row_index = self.find_row(matrix, m, n, target)
        if row_index is None:
            return False
        else:
            return self.find_column(matrix,m,target, row_index)
        
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        return self.check(matrix, m , n, target)
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
