class Solution(object):
    def maxSubArray(self, nums):
        temp = []
        max_num = float("-infinity")
        for i in range(0, len(nums)):
            temp.append(nums[i])
        for i in range(1, len(nums)):
            temp[i] = max(temp[i-1]+temp[i], temp[i])
        #print temp
        for i in range(0, len(nums)):
            max_num = max(max_num, temp[i])
            #print max_num
        return max_num
            
        """
        :type nums: List[int]
        :rtype: int
        """
