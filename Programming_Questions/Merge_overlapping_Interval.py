
class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        if not intervals or len(intervals) == 1:
            return intervals
        temp = []
        intervals = sorted(intervals, key=lambda interval: interval.start)
        low = intervals[0].start
        high = intervals[0].end
        flag = 0
        #for x in intervals:
            #print x.start,x.end
        for i in range(0, len(intervals)):
            if i+1 < len(intervals) and intervals[i+1].start <= high:
                #print low,high
                high = max(intervals[i+1].end, high)
                flag = 1
                continue
            else:
                x = Interval(low,high)
                temp.append(x)
                if i+1 < len(intervals):
                    low = intervals[i+1].start
                    high = intervals[i+1].end
                flag = 0
        if flag == 1:
             temp.append(Interval(low,high)) 
        return temp


