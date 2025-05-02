class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals = start time, end time in tuples
        # merges overlapping intervals and return array of non overlapping intervals 
        # [[1,3],[2,6]],[8,10],[15,18]]
        # sort by start time 
        # then check if overlapping, by checking most recent element's end value and current element start value 
        # if last > curr, set last one's end point to be max of current end point or last end point 
        # if not add it as is   
        n = len(intervals)

        if n == 0:
            return

        #sorting based on start time 
        intervals.sort( key = lambda i: i[0])

        #output
        res = [intervals[0]] # its start time will always be start time of intervals 

        #iterating through array from 1 index 
        for start, end in intervals[1:]:
            lastEnd = res[-1][1]
            if lastEnd >= start:
                res[-1][1] = max(end, lastEnd)
            else:
                res.append([start,end])
        return res

        