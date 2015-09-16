class Solution(object):
    def productExceptSelf(self, nums):
        res  = []
        res.append(1)
        for i in range(1, len(nums)):
            res.append(nums[i-1]*res[i-1])
        print res
        cummulaitve_right = 1
        for i in range(len(nums)-2, -1,-1):
            cummulaitve_right *= nums[i+1]
            res[i] = res[i]*cummulaitve_right
        print res
        return res
        """
        :type nums: List[int]
        :rtype: List[int]
        """
