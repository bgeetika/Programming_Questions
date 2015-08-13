class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if len(nums) < 1:
            return nums
        if len(nums) == 1:
            return [str(nums[0])]
        else:   
            low = nums[0]
            high = None
            lis = []
            flag = 1
            for i in range(1, len(nums)):
                if nums[i] == nums[i-1] + 1:
                    high = nums[i]
                    flag = 1
                    continue
                else:
                    
                    if high:
                        st = str(low) + "->" + str(high)
                    else:
                        st = str(low)
                    high = None
                    lis.append(st)
                    low = nums[i]
            if flag:
                if high:
                    st = str(low) + "->" + str(high)
                else:
                    st = str(low)
                lis.append(st)
            return lis
            
    
        



