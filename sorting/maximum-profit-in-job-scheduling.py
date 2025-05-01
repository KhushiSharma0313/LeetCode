class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        #greedy way would be picking a job that's max every time 
        # doesn't work
        # we need to make decision at every step so that it's max
        # for each job decide if we're gonna include or not include
        # if include no -> move to next job 
        # if include yes -> pick that job, and its profit, and move to job that's start time >= end time of current job 
        # for maximum profit = max(cureent job + profit of next job with end time aligning, next job)
        # base case => if there's no job, then no profit 
        # sorting it based on start time 
        # if we sort all the lists, the mapping would be lost 
        #so we want to combine start, end, profit so that it's sorted by start time 

        intervals = zip(startTime, endTime, profit)
        intervals = sorted(intervals) #sort it based on start time 
        res = 0
        
        #we want to look through each interval to check profit 
        #helper function 
        def dfs(i):
            #use a hashmap to store the intervals traversed 
            cache = {} 

            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]

            #don't wanna include this interval 
            res = dfs(i+1) # recursive algo 

            #do wanna include 
            #we need to find start time of next interval that's greater or equal than end time of current interval 
            j = i+1
            while j < len(intervals):
                if intervals[i][1] <= intervals[j][0]:
                    break
                j+=1
            
            #store max profit in the cache 
            cache[i] = res = max(intervals[i][2] + dfs(j), dfs(i+1))
            return res

        return dfs(0)




# class Solution:
#     def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
#         #we want maximum profit
#         # no overlapping jobs
#         # greeady does not work 

#         # what are the subproblems here
#         # so either we include a job or we don't
#         # if we don't, then nothing changes
#         #if we do include, look for max profit for remaning ones now  
#         #base case, for no job, profit is 0
#         #sort the jobs by start time 
#         # keep track of i, and previous end time, so no overlapping 
#         # but if we do 2 parameters, caching or memoization becomes less effective 
#         # so clever sol is if you don't include job go to i+1, but if you do choose it, go to j, which is when jobs don't overlap 

#         #if we sort start time, we'll lose the mapping for start and end time, so we'll put in one array with 3 parameters each 
#         #let's optimize this further
#         #instead of looping trhough to find j(next start time)
#         #we can just look for it by using binary search 
#         intervals = zip(startTime, endTime, profit) #grouping all arrays together 
#         intervals = sorted(intervals) #it's important that you put startTime first, since that's the basisthat they'll be sorted
#         cache = {}

#         def dfs(i):
#             #base case
#             if i == len(intervals):
#                 return 0
#             if i in cache:
#                 return cache[i]

            
#             #don't include 
#             res = dfs(i+1)

#             # #include 
#             # #how do we find j 
#             # #initialize at i+1
#             # j = i+1
#             # while j < len(intervals):
#             #     #if current node end time is less than next nodes start time, break
#             #     if intervals[i][1] <= intervals[j][0]:
#             #         break
#             #     #otherwise increment 
#             #     j +=1
#             #use binary search to search for end time
#             j = bisect.bisect(intervals, (intervals[i][1],-1,-1))
#             cache [i] = res = max(res, intervals[i][2] + dfs(j))
#             return res
        
#         return dfs(0) #we start from end and move to first element 




        