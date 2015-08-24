'''

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

'''


class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        sum1 = n*(n+1)/2
        sum2 = 0
        for  i in nums:
            sum2 = sum2 + i
        return sum1 - sum2
