class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # time = O(n+m) vertices and edges 
        #total course = numCourses
        # prereq = a,b take b in order to take a 
        # return ordering of courses you should take to finish all courses 
        # if more than one, choose any, if none return empty array 
        #e.g. = [1,0] [2,0] [3,1] [3,2] => 0<-1

        #courses are gonna be nodes 
        # use topological sort algo 
        #run dfs on all nodes 
        # before that we need adjacency list = list of neighbours 
        # this tells us prereq map, so the outgoing egdes from a node is it's prereqs form a hashmap for it 
        # run dfs of all nodes, until one node has no prereq, or no outgoing edges 
        # then add that to our list
        #remove that element from hashmap 
        #then repeat this until hashmap is empty
        # top sort is not unique so there can be multiple answers
        # if we detect cycle, return []
        #how to detect a cycle = if we come to a node we already started with, then its cycle and we stop 
        # use a hashset to remeber our current path 

        #building adjacency list of all nodes 
        prereq = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        output = [] * numCourses
        #for nodes that have been visited
        visited = set()
        #for nodes to detect if they're in cycle 
        cycle = set ()

        #helper function dfs 
        def dfs(crs):
            #if its in cycle, no order is possible 
            if crs in cycle:
                return False 
            #if it's in visited, we move on to next node 
            if crs in visited:
                return True 
            #added for this path to check if it's in cycle 
            cycle.add(crs)

            #for each prereq in hashmap run prereq on them and check if false
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False 
            visited.add(crs)
            cycle.remove(crs)
            output.append(crs)
            return True

        #now run dfs on all nodes 
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        # if its not a cycle 
        return output 


        