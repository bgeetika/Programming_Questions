class Solution(object):
    def singleNumber(self, nums):
        
        xor2 = 0
        for num in nums:
            xor2 ^= num
        
        set_bit = xor2 & ~(xor2 - 1)
        
        x = 0
        y = 0
        for num in nums:
            if(num & set_bit):
                x ^= num
            else:
                y ^= num
                
        return [x,y]
        
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
