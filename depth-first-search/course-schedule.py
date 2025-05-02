class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # time = O(n+p) -> move along every singe node and every single edge 
        #numCourses 0 to n-1 
        #prereq = a,b -> must take b to finish a 
        # all pairs are unique 
        #represent [a,b]  as an edge of graph going outward from a to b and numCourse is number of edges 
        #if node doesn't have outward edges, it's possible to take the course
        #we can use dfs/bfs for this problem
        #we'll use dfs 
        #base case - nodes who don't have any prereq, or node with no outward edge 
        #we can use adjacency list to figure it out 
        # use hashmap to represent it key = course, val = prereq 
        # run dfs on each node in order 0, n-1
        # do it recursiverly using hashmap info for prereq
        # for nodes with no pre req, mark them as done, and move back to course req only this as prereq, mark that as done and so on
        #marking done meaning remove prereq for courses, if their prereq can be ocmpletedd
        # if each val is emptly at the end, it's successful 

        #how to detect cycle in graph 
        # use data strcuture set, it's gonna contain list of courses in our dfs 
        # if prereq of some node is alrrady in set, it means it has a prereq too and we're stuck in a cycle 
        # so we need to return false 

        # decalre hashmap 
        preMap = { i: [] for i in range(numCourses)}

        #fill up the hashmap with all courses as keys and prereq its val 
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        #declare set 
        visited = set()

        #recursive dfs 
        def dfs(crs):
            #if there's a cycle, course can't be scheduled
            if crs in visited:
                return False 
            
            # if course has no prereq, it is true
            if preMap[crs] == []:
                return True
            
            #add this course to visited
            visited.add(crs)

            #for each prereq
            for pre in preMap[crs]:
                #if dfs returns false, we return false 
                if not dfs(pre): return False
            #done with prereq then remove the course and null its prereq
            visited.remove(crs)
            preMap[crs] = []
            return True
        
        #now run dfs on all nodes 
        for crs in range(numCourses):
            #if dfs is false for any course, we retrun false
            if not dfs(crs): return False 
        return True
