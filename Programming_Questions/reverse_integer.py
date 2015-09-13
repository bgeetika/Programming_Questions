class Solution(object):
    def reverse(self, x):
        if x == 0:
            return 0
        temp = abs(x)
        num = 0
        while temp != 0 :
            rem = temp % 10
            num = num*10 + rem
            temp = temp/10
        if num > (2**32)/2 -1:
            return 0
        elif x > 0:
            return num
        else:
            return -1*num
            
            
        """
        :type x: int
        :rtype: int
        """
        
