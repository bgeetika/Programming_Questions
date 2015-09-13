class Solution(object):
    def searchInsert(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start+end)/2
            print mid
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if mid == 0:
                    return 0
                if nums[mid - 1] < target:
                     return mid
                else:
                    end = mid - 1
            else:
                if mid == len(nums) - 1:
                    return mid + 1
                start = mid + 1
                
            
        
    
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
