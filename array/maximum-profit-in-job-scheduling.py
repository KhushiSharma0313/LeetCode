class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        #we want maximum profit
        # no overlapping jobs
        # greeady does not work 

        # what are the subproblems here
        # so either we include a job or we don't
        # if we don't, then nothing changes
        #if we do include, look for max profit for remaning ones now  
        #base case, for no job, profit is 0
        #sort the jobs by start time 
        # keep track of i, and previous end time, so no overlapping 
        # but if we do 2 parameters, caching or memoization becomes less effective 
        # so clever sol is if you don't include job go to i+1, but if you do choose it, go to j, which is when jobs don't overlap 

        #if we sort start time, we'll lose the mapping for start and end time, so we'll put in one array with 3 parameters each 
        #let's optimize this further
        #instead of looping trhough to find j(next start time)
        #we can just look for it by using binary search 
        intervals = zip(startTime, endTime, profit) #grouping all arrays together 
        intervals = sorted(intervals) #it's important that you put startTime first, since that's the basisthat they'll be sorted
        cache = {}

        def dfs(i):
            #base case
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]

            
            #don't include 
            res = dfs(i+1)

            # #include 
            # #how do we find j 
            # #initialize at i+1
            # j = i+1
            # while j < len(intervals):
            #     #if current node end time is less than next nodes start time, break
            #     if intervals[i][1] <= intervals[j][0]:
            #         break
            #     #otherwise increment 
            #     j +=1
            #use binary search to search for end time
            bisect.bisect(intervals, (intervals[i][1],-1,-1))
            cache [i] = res = max(res, intervals[i][2] + dfs(j))
            return res
        
        return dfs(0) #we start from end and move to first element 




        