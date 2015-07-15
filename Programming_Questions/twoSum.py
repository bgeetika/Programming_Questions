class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        temp = sorted(nums)
        start = 0
        end = len(temp) -1
        print temp
        while start <= end:
            if temp[start] + temp[end] == target:
                print temp[start], temp[end]
                if temp[start] == temp[end]:
                    x = nums.index(temp[start])
                    
                    return [x+1, nums[x+1:].index(temp[end])+1+x +1]
                return sorted([nums.index(temp[start])+1, ((nums.index(temp[end]))+1)])
            elif temp[start] + temp[end] < target:
                start = start + 1
            else:
                end = end - 1
