class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        flag = 0
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            start = -1
            for j in range(0,len(nums)):
                if j + 1 < len(nums) and nums[j] == nums[j+1]:
                        flag = 1
                        continue
                else:
                    start = start + 1
                    nums[start] = nums[j]
                    flag = 0 
            if flag == 1 :
                start = start + 1
                nums[start] = nums[j+1]
                
            return start + 1
        
        



