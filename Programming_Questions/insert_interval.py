# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge_intervals(self,intervals):
        res = []
        high = intervals[0].end
        lo = intervals[0].start
        flag = 0
        for i in range(0, len(intervals)):
            if i+1 < len(intervals) and intervals[i+1].start <= high:
                high = max(intervals[i+1].end, high)
                flag = 1
                continue
            else:
                new_inter = Interval(lo,high)
                res.append(new_inter)
                if i+1 < len(intervals):
                    lo = intervals[i+1].start
                    high = intervals[i+1].end
                flag = 0
        if flag == 1:
            res.append(lo,high)
        return res
            
            
    
    def find_location(self, intervals, start, end, val):
        if val <= intervals[0].start :
            return 0
        while start <= end:
            mid = (start + end)/2
            if intervals[mid].start >= val and (mid-1  == 0 or  intervals[mid-1].start <= val):
                return mid
            elif intervals[mid].start < val:
                start = mid + 1
            else:
                end = mid - 1
        
        
    
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        intervals = sorted(intervals, key=lambda interval: interval.start)
        res = []
        
        index = self.find_location(intervals, 0, len(intervals) -1,  newInterval.start)
        if index == None:
            intervals.append(newInterval)
        else:
            print index
            intervals.append(newInterval)
            for x in range(len(intervals) - 1, index -1 , -1):
                intervals[x] = intervals[x-1]
            intervals[index] = newInterval
        
        return self.merge_intervals(intervals)
        
        
        
