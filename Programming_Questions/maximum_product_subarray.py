class Solution(object):
    def maxProduct(self, nums):
        res = []
        res.append(nums[0])
        
        min_arr = []
        min_arr.append(nums[0])
        
        for i in range(1, len(nums)):
            res_last = res[-1]
            min_last =  min_arr[-1]
            res.append(max(nums[i], res_last*nums[i], min_last*nums[i]))
            min_arr.append( min( nums[i], min_last*nums[i], res_last*nums[i]))
        max_pro = float("-infinity")
        
        print min_arr
        for i in range(0, len(res)):
            max_pro = max(max_pro, res[i])
            
        return max_pro
        """
        :type nums: List[int]
        :rtype: int
        """
        
