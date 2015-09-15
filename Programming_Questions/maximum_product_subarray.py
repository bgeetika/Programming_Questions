class Solution(object):
    def maxProduct(self, nums):
        max_product = nums[0]
        min_product = nums[0]
        res_last = nums[0]
        min_last = nums[0]
        
        
        for i in range(1, len(nums)):
            res_last_val = res_last
            min_last_val =  min_last
            res_last = (max(nums[i], res_last_val*nums[i], min_last_val*nums[i]))
            min_last = (min(nums[i], res_last_val*nums[i], min_last_val*nums[i]))
            max_product = max(max_product, res_last)
            min_product = min(min_product, min_last)
            print max_product, min_product
        return max(max_product, min_product)
        """
        :type nums: List[int]
        :rtype: int
