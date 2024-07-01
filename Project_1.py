def searchMatrix(matrix, target):    
        for arr in matrix:
            if arr[0] > target:
                return 0
            for k in arr:
                if k > target:
                    break
                if k == target:
                    return 1
        return 0    
