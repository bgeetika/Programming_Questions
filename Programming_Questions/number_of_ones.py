class Solution:
    # @param {integer} n
    # @return {integer}
    def length(self, n):
        temp = n
        l = 0
        while temp > 0 :
            temp = temp/10
            l = l+1
        return l
    
    def countDigit(self, n):
        x = 0
        t = 1
        arr = {}
        arr[0] = 0
        while t <= n:
            x = 10*arr[t-1] + pow(10, t-1)
            arr[t] = x
            t = t + 1 
        return arr
   
    def countDigitOne(self, num):
            if num <= 0:
                return 0
            n = self.length(num)
            arr = self.countDigit(n)
            x = 0
            return self.findnumber(num, arr)
    
    def findnumber(self, num, arr):
        x = 0
        while(num > 0):
            n = self.length(num)
            nth = num/pow(10, n-1)
            if nth == 0:
                num = num - nth*pow(10,n-1)
            if num < 1:
                return x
            if num <= 9:
                return  x + 1
            else:
                if nth == 1:

                    x = x +  (nth*arr[n-1] + (num-nth*pow(10, n-1)+1))
                    num = num - nth*pow(10,n-1)
                else:
                    x = x +   (nth*arr[n-1] + pow(10, n-1)) 
                    num = num - nth*pow(10,n-1)
        return x
        
