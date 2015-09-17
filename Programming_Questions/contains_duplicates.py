class Solution(object):
    def containsDuplicate(self, nums):
        numsSet =  set(nums)
        if len(nums) == len(numsSet):
            return False
        return True
